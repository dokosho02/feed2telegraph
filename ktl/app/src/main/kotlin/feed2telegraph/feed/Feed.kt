package feed2telegraph

import com.rometools.rome.feed.synd.SyndFeed
import com.rometools.rome.feed.synd.SyndEntry
import com.rometools.rome.io.SyndFeedInput
import com.rometools.rome.io.XmlReader
import java.net.URL


public data class Feed(
    val link:  String,
    val title: String,
    val lang:  String,
    val channelId: String,
    val translated: Boolean,
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
            println("Entry Link: ${entry.link}")
            println("Entry Author: ${entry.author}")
        }
    }
    
    // fun write2sqlite() {
        
    // }
}