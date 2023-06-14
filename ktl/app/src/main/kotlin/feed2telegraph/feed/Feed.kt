package feed2telegraph

import com.rometools.rome.feed.synd.SyndFeed
import com.rometools.rome.feed.synd.SyndEntry
import com.rometools.rome.io.SyndFeedInput
import com.rometools.rome.io.XmlReader
import java.net.URL

// 5 parameters
data class Feed(
    val link:  String,
    val title: String,
    val lang:  String,
    val channelId: String,
    val translated: Int,
) {
    var entriesNew: MutableList<SyndEntry> = mutableListOf()
    
    fun parse() {
        // Create a new instance of the feed parser
        val input = SyndFeedInput()
        // Parse the feed
        val feed = input.build(XmlReader(URL(link))) as SyndFeed

        println("-".repeat(10))
        // Print the feed information
        println("Feed Title: ${feed.title}")
        println("Feed Description: ${feed.description}")
        println("Feed Link: ${feed.link}")
        println("Feed Language: ${feed.language}")
        
        // println(feed.entries.first()::class.java.typeName)
        println("-".repeat(10))

        entriesNew = feed.entries
        // Print the feed entries
        feed.entries.forEach { entry ->
            println("Entry Title: ${entry.title}")
            println("Entry Published Date: ${entry.publishedDate}")
            // println("Entry Link: ${entry.link}")
            // println("Entry Author: ${entry.author}")

            var desc = entry.description?.value
            val content = entry.contents
                .takeIf { it.isNotEmpty() }
                ?.let { it.joinToString("\n") { it.value } }
            // println("Entry desc: ${desc}")
            // println("Entry content: ${content}")

            val article = Article(
                title = entry.title,
                link  = entry.link,
                contents = desc!!,
                telegraphLink = null,
                authors       = null,
                tags          = null,
                feedName=title,
                feedLink=link,
                lang = lang,
                channelId = channelId,
                translated = translated,
            )

            article.write2sqlite()

            println("~".repeat(10))
        }
    }
    
    fun write2sqlite() {
        // if database not exist
        println(dbPath)
        val conn = createConnection(dbPath)
        createTable(conn!!, sql_create_feeds_table)
        // conn.close()
        // if database exist

        val temp = listOf(title, link, lang, channelId).joinToString("','")
        insertItem(conn,
            table=feed_table_name,
            template="title, link, language, channel, translated",
            values= "'$temp', $translated",
        )
    }
}