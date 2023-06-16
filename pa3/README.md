# Project Transcript

## Brandon J. Lacy (AG3NTZ3R0)
### Show Transactions
(venv) brandonlacy@Brandons-MBP pa03 % python tracker.py --show-trans
{'id': 1, 'amount': 9.99, 'category': 'food', 'date': '2023-03-24', 'description': 'fast-food'}
{'id': 2, 'amount': 9.99, 'category': 'food', 'date': '2023-03-24', 'description': 'fast-food'}

### Add Transaction
(venv) brandonlacy@Brandons-MBP pa03 % python tracker.py --add-trans 3 0.99 food 2023-03-29 gum
Completed.
(venv) brandonlacy@Brandons-MBP pa03 % python tracker.py --show-trans                          
{'id': 1, 'amount': 9.99, 'category': 'food', 'date': '2023-03-24', 'description': 'fast-food'}
{'id': 2, 'amount': 9.99, 'category': 'food', 'date': '2023-03-24', 'description': 'fast-food'}
{'id': 3, 'amount': 0.99, 'category': 'food', 'date': '2023-03-29', 'description': 'gum'}

### PyLint
#### Tracker.py
(venv) brandonlacy@Brandons-MBP pa03 % pylint tracker.py 

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

#### Transaction.py
(venv) brandonlacy@Brandons-MBP pa03 % pylint transaction.py 

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

####
(venv) brandonlacy@Brandons-MBP pa03 % pylint test_transaction.py 
************* Module test_transaction
test_transaction.py:23:22: W0621: Redefining name 'example_data' from outer scope (line 10) (redefined-outer-name)
test_transaction.py:34:15: W0612: Unused variable 'j' (unused-variable)
test_transaction.py:42:19: W0621: Redefining name 'example_data' from outer scope (line 10) (redefined-outer-name)
test_transaction.py:70:20: W0621: Redefining name 'transaction_db' from outer scope (line 42) (redefined-outer-name)
test_transaction.py:70:36: W0621: Redefining name 'example_data_dict' from outer scope (line 23) (redefined-outer-name)
test_transaction.py:83:13: W0621: Redefining name 'transaction_db' from outer scope (line 42) (redefined-outer-name)
test_transaction.py:83:29: W0621: Redefining name 'example_data_dict' from outer scope (line 23) (redefined-outer-name)

------------------------------------------------------------------
Your code has been rated at 8.11/10 (previous run: 8.11/10, +0.00)

