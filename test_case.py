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
        
def test_show():
    try:
        show()
        print("Test show successful!")
    except:
        print("Test show failed.")
        
def test_purchase():
    try:
        purchase("test",12)
        print("Test purchase successful!")
    except:
        print("Test purchase failed.")
        
def test_restock():
    try:
        restock("test",12)
        print("Test restock successful!")
    except:
        print("Test restock failed.")
        
def test_search():
    try:
        search("test")
        print("Test search successful!")
    except:
        print("Test search failed.")

def test_sort():
    try:
        sort('name','desc')
        print("Test sort successful!")
    except:
        print("Test sort failed.")
        
if __name__ == "__main__":
    test_add()
    test_purchase()
    test_restock()
    test_search()
    test_show()
    test_sort()
    test_delete()