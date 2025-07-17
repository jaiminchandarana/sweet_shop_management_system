## Prerequisites

  

1.  **Install Python**:

- Download Python from [Microsoft Store](https://www.microsoft.com/store/productId/9NCVDN91XZQP?ocid=pdpshare) or from the [official Python website](https://www.python.org/downloads/).


2.  **Add Python to System Path**:

- Ensure Python is added to your system path. By default, Python is usually located at:

```

C:\Users\[Your Username]\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts

```

- To add Python to your path:

- Open **Environment Variables** > **System Variables** > **Path** > **Edit**.

- Add the path to your Python directory containing `ipython.exe` (usually in the folder listed above).

- Click **OK** to save.



## Running the sweet shop management system



1.  **Set Up Your Environment**:

- Create or use an existing folder, and place all files from this repository into it.
  

2.  **Install Dependencies**:

- Open Command Prompt in the folder where you saved the files.
- Run:

```bash

pip install -r requirements.txt

```


3.  **Run `app.py`**:

- Open your IDE and execute `streamlit run app.py` in terminal to run sweet shop management system.



## Test report



1.  **`Test_add`**:

- Adds a test sweet to inventory.
- **Test result** : Test add successful !


2.  **`Test_delete`**:
- Deletes the test sweet from inventory.
- **Test result** : Test delete successful !


3.  **`Test_show`**:
- Displays all sweets from inventory.
- **Test result** : Test show successful !


4.  **`Test_purchase`**:
- Purchases specified quantity of sweet.
- **Test result** : Test purchase successful !

  
5.  **`Test_restock`**:
- Restocks specified quantity of sweet.
- **Test result** : Test restock successful !


6.  **`Test_search`**:
- Searches for sweet in inventory.
- **Test result** : Test search successful !


7.  **`Test_sort`**:
- Sorts inventory by sweet name, category or price.
- **Test result** : Test sort successful !
