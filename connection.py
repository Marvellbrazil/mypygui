import mariadb as db

__DB_HOST__ = "localhost"
__DB_USN__ = "root"
__DB_PASS__ = ""
__DB_PORT__ = 3306
__DB_NAME__ = "db_mypygui"  # The name of the database

DB_CONFIG = {
    "host": __DB_HOST__,
    "user": __DB_USN__,
    "password": __DB_PASS__,
    "port": __DB_PORT__,
    "database": __DB_NAME__,
}


# Function to get connection from the database
def get_conn():
    try:
        conn = db.connect(**DB_CONFIG)
        return conn
    except db.Error as e:
        print(f"Failed to connect to the Database:\n{e}")
        return None


# INIT the database
def init_db():
    conn = get_conn()
    if conn is None:
        return

    cur = conn.cursor()
    query = """
                CREATE TABLE IF NOT EXISTS user (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(100),
                    age INT(3),
                    email VARCHAR(100)
                )
                """
    cur.execute(query)
    conn.commit()
    conn.close()
