import psycopg2

def connection():
    conn = psycopg2.connect(
        host = "localhost",
        database = "INCUBYTE",
        user = "",
        password = "",
        port = 5432
    )
    return conn
