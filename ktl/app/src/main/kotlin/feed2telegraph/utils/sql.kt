package feed2telegraph

import java.sql.DriverManager
import java.sql.SQLException
import java.sql.Connection
import java.io.File

fun main() {
    val odf = System.getenv("odf")  // OneDrive folder path
    // pdf apps/feed2tele
    val pathParts = listOf(odf, "apps", "feed2tele", "mydatabase.db")
    val dbPath = pathParts.joinToString(separator = File.separator)


    val url = "jdbc:sqlite:${dbPath}"
    var conn: Connection? = null
    try {
        // connect to the database
        conn = DriverManager.getConnection(url)

        // create a table
        val sql = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT);"
        conn.createStatement().execute(sql)

        // insert some data
        val insert = "INSERT INTO users (name, email) VALUES ('John Doe', 'johndoe@example.com')"
        conn.createStatement().execute(insert)

        // select data
        val select = "SELECT * FROM users"
        val resultSet = conn.createStatement().executeQuery(select)
        while (resultSet.next()) {
            val id = resultSet.getInt("id")
            val name = resultSet.getString("name")
            val email = resultSet.getString("email")
            println("id = $id, name = $name, email = $email")
        }
    } catch (e: SQLException) {
        e.printStackTrace()
    } finally {
        // close the connection
        conn?.close()
    }
}









