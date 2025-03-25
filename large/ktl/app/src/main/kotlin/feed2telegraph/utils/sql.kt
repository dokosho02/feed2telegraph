package feed2telegraph

import java.sql.DriverManager
import java.sql.SQLException
import java.sql.Connection
import java.io.File

val odf = System.getenv("odf")  // OneDrive folder path
    // pdf apps/feed2tele
val pathParts = listOf(odf, "apps", "feed2tele", "myfeeds.db")
val dbPath = pathParts.joinToString(separator = File.separator)

val feed_table_name    = "feeds"
val article_table_name = "articles"

val sql_create_feeds_table = """CREATE TABLE IF NOT EXISTS $feed_table_name (
    id integer PRIMARY KEY,
    title text NOT NULL,
    link text NOT NULL,
    language text,
    channel text,
    translated integer
);"""

val sql_create_articles_table = """CREATE TABLE IF NOT EXISTS $article_table_name (
    id integer PRIMARY KEY,
    title text,
    link text,
    date text,
    contents text,
    authors text,
    language text,
    tags text,
    type text,
    kakasi text,
    translation text,
    feed_name text,
    feed_link text,
    feed_id integer,
    read integer,
    starred integer,
    FOREIGN KEY (feed_id) REFERENCES feeds (id)
);"""

val select_feed_sql = """SELECT * FROM ${feed_table_name} WHERE link="""

fun createConnection(dbPath: String): Connection? {
    val url = "jdbc:sqlite:${dbPath}"
    var conn: Connection? = null
    try {
        // connect to the database
        conn = DriverManager.getConnection(url)
    } catch (e: SQLException) {
        e.printStackTrace()
    }
    return conn
}

fun createTable(conn: Connection, sql: String) {
    try {
        conn.createStatement().execute(sql)
    } catch (e: SQLException) {
        e.printStackTrace()
    }
}

fun insertItem(conn: Connection, table: String, template: String, values: String) {
    val sql = """INSERT INTO $table ($template) VALUES ($values)"""
    try {
        conn.createStatement().execute(sql)
    } catch (e: SQLException) {
        e.printStackTrace()
    }
}

fun selectAllItemsInTable(conn: Connection,table: String) {
    val select = "SELECT * FROM $table"
    try {
        val resultSet = conn.createStatement().executeQuery(select)
        while (resultSet.next()) {
            println("---")
        }
    } catch (e: SQLException) {
        e.printStackTrace()
    }
}

fun selectItemsByProperty(conn: Connection, table: String, p: String, v:String) {
    // Execute a SELECT statement to retrieve items by a specific property
    val stmt = conn.prepareStatement("SELECT * FROM $table WHERE $p = ?")
    stmt.setString(1, v)
    val rs = stmt.executeQuery()
}


// fun main() {
    

//     try {
//         // connect to the database
//         conn = DriverManager.getConnection(url)

//         // create a table
//         val sql = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT);"
//         conn.createStatement().execute(sql)

//         // insert some data
//         val insert = "INSERT INTO users (name, email) VALUES ('John Doe', 'johndoe@example.com')"
//         conn.createStatement().execute(insert)

//         // select data
//         val select = "SELECT * FROM users"
//         val resultSet = conn.createStatement().executeQuery(select)
//         while (resultSet.next()) {
//             val id = resultSet.getInt("id")
//             val name = resultSet.getString("name")
//             val email = resultSet.getString("email")
//             println("id = $id, name = $name, email = $email")
//         }
//     } catch (e: SQLException) {
//         e.printStackTrace()
//     } finally {
//         // close the connection
//         conn?.close()
//     }
// }









