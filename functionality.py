from connection import connection

def add(name,category,price,quantity):
    try:
        conn = connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO incubyte (name,category,price,quantity) VALUES (%s, %s, %s, %s)", (name,category,price,quantity))
        conn.commit()
        cur.close()
        conn.close()
    except:
        print("Product already exist, try restocking or adding new one.")

def delete(name):
    try:
        conn = connection()
        cur = conn.cursor()
        cur.execute("DELETE from incubyte where name = %s",(name,))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("This is product is not in stock.")
        
def show():
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT name,category,price,quantity FROM incubyte")
    rows = cur.fetchall()
    for row in rows:
        return row 
    conn.commit()
    cur.close()
    conn.close()