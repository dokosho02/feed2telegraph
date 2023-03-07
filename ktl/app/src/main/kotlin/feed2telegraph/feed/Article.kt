package feed2telegraph

data class Article(
    val title: String,
    val link: String,
    val contents: String,
    val telegraphLink: String,
    val authors: List<String>?,
    val tags: List<String>?,
    val feedName: String,
    val feedLink: String,
    val lang:  String,
    val channelId: String,
    val translated: Boolean,
) {

}