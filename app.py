import streamlit as st
from functionality import add, delete, show, restock, purchase, search, sort
import pandas as pd

st.title("Sweet Shop Management System")

menu = ["Add Sweet", "View Sweets", "Purchase Sweet", "Restock Sweet", "Delete Sweet", "Sort Sweets", "Search Sweet"]
choice = st.sidebar.selectbox("Select Action", menu)

if choice == "Add Sweet":
    st.header("Add New Sweet")
    name = st.text_input("Sweet Name")
    category = st.text_input("Category")
    price = st.number_input("Price", step=0.01)
    quantity = st.number_input("Quantity", step=1)

    if st.button("Add Sweet"):
        add(name, category, price, quantity)
        st.success(f"Sweet '{name}' added successfully!")

elif choice == "View Sweets":
    st.header("Current Inventory")
    data = show()

    if data:
        df = pd.DataFrame(data, columns=["Name", "Category", "Price", "Quantity"])
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No inventory records found.")

elif choice == "Purchase Sweet":
    st.header("Purchase Sweet")
    pname = st.text_input("Enter Sweet Name to Purchase")
    qty = st.number_input("Quantity to Purchase", step=1)

    if st.button("Purchase"):
        purchase(pname, qty)
        st.success(f"{qty} Purchased of {pname}.")

elif choice == "Restock Sweet":
    st.header("Restock Sweet")
    pname = st.text_input("Enter Sweet Name to Restock")
    qty = st.number_input("Quantity to Add", step=1)

    if st.button("Restock"):
        restock(pname, qty)
        st.success(f"{qty} Restocked of {pname}.")

elif choice == "Delete Sweet":
    st.header("Delete Sweet")
    pname = st.text_input("Enter Sweet Name to Delete")
    if st.button("Delete"):
        delete(pname)
        st.success(f"Sweet {pname} Deleted.")

elif choice == "Sort Sweets":
    st.header("Sort Sweet")
    sort_field = st.selectbox("Sort by", ["name", "category", "price"])
    sort_order = st.selectbox("Order", ["asc", "desc"])
    
    if st.button("Sort"):
        sorted_data = sort(sort_field, sort_order)
        df = pd.DataFrame(sorted_data, columns=["Name", "Category", "Price", "Quantity"])
        st.dataframe(df, use_container_width=True)

elif choice == "Search Sweet":
    st.header("Search Sweet")
    search_term = st.text_input("Enter Sweet to search")
    if st.button("Search"):
        result = search(f"%{search_term}%")
        if result:
            st.success("Sweet found:")
            st.write(result)
        else:
            st.warning("No sweet found.")