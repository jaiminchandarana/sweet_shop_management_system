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
