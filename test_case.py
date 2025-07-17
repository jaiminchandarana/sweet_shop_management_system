from functionality import add,delete,show,purchase,restock,search,sort

def test_add():
    try:
        add("test","test",10,12)
        print("Test add successful!")
    except:
        print("Test add failed.")
        
def test_delete():
    try:
        delete("test")
        print("Test delete successful!")
    except:
        print("Test delete failed.")
        