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
        print("Sweet already exist, try adding new one.")

def delete(name):
    try:
        conn = connection()
        cur = conn.cursor()
        cur.execute("DELETE from incubyte where name = %s",(name,))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("This sweet is not in stock.")
        
def show():
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT name,category,price,quantity FROM incubyte")
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return rows
    
def purchase(name,quantity):
    try:
        conn = connection()
        cur = conn.cursor()
        cur.execute("UPDATE incubyte SET quantity = quantity - %s WHERE name = %s",(quantity,name,))
        conn.commit()
        cur.close()
        conn.close()
    except:
        print("Your desiderd sweet has low stock than your need.")

def restock(name,quantity):
    conn = connection()
    cur = conn.cursor()
    cur.execute("UPDATE incubyte SET quantity = quantity +  %s WHERE name = %s",(quantity,name,))
    conn.commit()
    cur.close()
    conn.close()
    
def search(name):
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT name,category,price,quantity FROM incubyte where name ILIKE %s OR category ILIKE %s OR CAST(price AS TEXT) ILIKE %s",(name,name,name))
    rows = cur.fetchall()
    for row in rows:
        return row
    conn.commit()
    cur.close()
    conn.close()

def sort(field,type):
    conn = connection()
    cur = conn.cursor()
    value = ["name","category","price"]
    mode = ["asc","desc"]
    if field not in value:
        print("Please select from list.")
    elif type not in mode:
        print("Please select from list.")
    cur.execute(f"SELECT name,category,price,quantity FROM incubyte ORDER BY {field} {type.upper()}")
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return rows