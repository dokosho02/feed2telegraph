package feed2telegraph

data class Article(
    val title: String,
    val link: String,
    val contents: String,
    val telegraphLink: String?,
    val authors: List<String>?,
    val tags: List<String>?,
    val feedName: String,
    val feedLink: String,
    val lang:  String,
    val channelId: String,
    val translated: Int,
) {
    val date = ""
    val type = "text"
    val kakasi = ""
    val translation = ""
    val read = 0
    val starred = 0

    fun write2sqlite() {
        val conn = createConnection(dbPath)
        createTable(conn!!, sql_create_articles_table)
        // conn.close()
        val temp = listOf(title, link, date, contents, authors,lang, tags, type, kakasi, translation, feedName, feedLink, feed_id, read, starred).joinToString("','")
        insertItem(conn,
            table=feed_table_name,
            template="title, link, date, contents, authors,language, tags, type, kakasi, translation, feed_name, feed_link, feed_id, read, starred",
            values= "'$temp', $translated",
        )
    }
}