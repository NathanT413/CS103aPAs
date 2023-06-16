'''
A file to test the functionality of transaction.py
'''
import sqlite3
import pytest

from transaction import Transaction

@pytest.fixture
def example_data():
    '''
    A few data entries to assist in the test of application functionality.

    Author: Brandon J. Lacy (AG3NTZ3R0), Eric Wang
    '''
    return [
        (1, 9.99, 'food', '2023-03-23', 'fast-food'),
        (2, 99.99, 'food', '2023-03-28', 'groceries'),
        (4, 12.99, 'McDonalds', '2023-03-23', 'food'),
        (5, 120450.99, 'MercedesACLass', '2019-04-23', 'Vehical'),
        (6, 5040.0, 'MacbookPro', '2019-05-19', 'computer'),
        (7, 1250.0, 'Ipad', '2019-05-19', 'tablet')
    ]


@pytest.fixture
def example_data_dict(example_data):
    '''
    The dictionary representation of the example_data.
    
    Author: Brandon J. Lacy (AG3NTZ3R0)
    '''
    result = []
    for tup in example_data:
        cols = ['id', 'amount', 'category', 'date', 'description']
        example_dict = {}
        # for i in range(len(tup)):
        for i, j in enumerate(tup):
            # example_dict[cols[i]] = tup[i]
            example_dict[cols[i]] = tup[i]
        result.append(example_dict)
    return result


@pytest.fixture
def transaction_db(example_data, test_db='test_tracker.db'):
    '''
    Create the table for the tests and add the data.

    Author: Brandon J. Lacy (AG3NTZ3R0)
    '''
    con = sqlite3.connect(test_db)
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS transactions 
        (id INT, amount FLOAT, category TEXT, date DATE, description TEXT)'''
    )

    for tup in example_data:
        cur.execute("INSERT INTO transactions VALUES(?, ?, ?, ?, ?)", tup)

    con.commit()

    test_trans_orm = Transaction(test_db)

    yield test_trans_orm

    cur.execute("DROP TABLE transactions")
    con.commit()
    # con.close()


def test_select_all(transaction_db, example_data_dict):
    '''
    Test the ability to select all of the transactions in the database.
    
    Author: Brandon J. Lacy (AG3NTZ3R0)
    '''
    trans_orm = transaction_db

    results = trans_orm.select_all(())

    assert results == example_data_dict


def test_add(transaction_db, example_data_dict):
    '''
    Test the ability to add a transaction to the database.
    
    Author: Brandon J. Lacy (AG3NTZ3R0)
    '''
    trans_orm = transaction_db

    tup = (3, 0.99, 'food', '2023-03-29', 'gum')
    updated_example_data_dict = example_data_dict
    updated_example_data_dict.append({
        'id': tup[0],
        'amount': tup[1],
        'category': tup[2],
        'date': tup[3],
        'description': tup[4]
    })

    trans_orm.add(tup)

    results = trans_orm.select_all(())

    assert results == updated_example_data_dict

def test_del(transaction_db, example_data_dict):
    '''
    Test the ability to delete a transaction from the database.
    
    Author: Eric Wang
    '''
    trans_orm = transaction_db

    tup = (1, 9.99, 'food', '2023-03-23', 'fast-food')
    updated_example_data_dict = example_data_dict
    updated_example_data_dict.remove({
        'id': tup[0],
        'amount': tup[1],
        'category': tup[2],
        'date': tup[3],
        'description': tup[4]
    })

    trans_orm.delete(str(tup[0]))

    results = trans_orm.select_all(())

    assert results == updated_example_data_dict

def test_sum_date(transaction_db):
    '''
    Test the ability to find transaction given the date.
    
    Author: Eric Wang
    '''
    trans_orm = transaction_db
    tup1 = (1, 9.99, 'food', '2023-03-23', 'fast-food')
    tup2 = (4, 12.99, 'McDonalds', '2023-03-23', 'food')
    expect = []
    expect.append({
        'id': tup1[0],
        'amount': tup1[1],
        'category': tup1[2],
        'date': tup1[3],
        'description': tup1[4]
    })
    expect.append({
        'id': tup2[0],
        'amount': tup2[1],
        'category': tup2[2],
        'date': tup2[3],
        'description': tup2[4]
    })

    results = trans_orm.sum_date(['2023-03-23'])

    assert results == expect

def test_sum_month(transaction_db):
    '''
    Test the ability to find transaction given the year and month.
    
    Author: Eric Wang
    '''
    trans_orm = transaction_db
    tup1 = (1, 9.99, 'food', '2023-03-23', 'fast-food')
    tup2 = (4, 12.99, 'McDonalds', '2023-03-23', 'food')
    tup3 = (2, 99.99, 'food', '2023-03-28', 'groceries')
    expect = []
    expect.append({
        'id': tup3[0],
        'amount': tup3[1],
        'category': tup3[2],
        'date': tup3[3],
        'description': tup3[4]
    })
    expect.append({
        'id': tup1[0],
        'amount': tup1[1],
        'category': tup1[2],
        'date': tup1[3],
        'description': tup1[4]
    })
    expect.append({
        'id': tup2[0],
        'amount': tup2[1],
        'category': tup2[2],
        'date': tup2[3],
        'description': tup2[4]
    })
   
    results = trans_orm.sum_month(['2023-03'])

    assert results == expect

def test_sum_year(transaction_db):
    '''
    Test the ability to find transaction given the year.
        
    Author: Eric Wang
    '''
    trans_orm = transaction_db

    tup2 = (5, 120450.99, 'MercedesACLass', '2019-04-23', 'Vehical')
    tup3 =(6, 5040.0, 'MacbookPro', '2019-05-19', 'computer')
    tup1 = (7, 1250.0, 'Ipad', '2019-05-19', 'tablet')
    expect = []
    expect.append({
        'id': tup3[0],
        'amount': tup3[1],
        'category': tup3[2],
        'date': tup3[3],
        'description': tup3[4]
    })
    expect.append({
        'id': tup1[0],
        'amount': tup1[1],
        'category': tup1[2],
        'date': tup1[3],
        'description': tup1[4]
    })
    expect.append({
        'id': tup2[0],
        'amount': tup2[1],
        'category': tup2[2],
        'date': tup2[3],
        'description': tup2[4]
    })
    
    results = trans_orm.sum_month(['2019'])

    assert results == expect
        
def test_sum_category(transaction_db):
    '''
    Test the ability to find transaction given the category.

    Author Grace Hu
    '''
    trans_orm = transaction_db
    tup1 = (1, 9.99, 'food', '2023-03-23', 'fast-food')
    tup2 = (2, 99.99, 'food', '2023-03-28', 'groceries')
    expect = []
    expect.append({
        'id': tup1[0],
        'amount': tup1[1],
        'category': tup1[2],
        'date': tup1[3],
        'description': tup1[4]
    })
    expect.append({
        'id': tup2[0],
        'amount': tup2[1],
        'category': tup2[2],
        'date': tup2[3],
        'description': tup2[4]
    })

    results = trans_orm.sum_category(['food'])

    assert results == expect

def test_add_category(transaction_db):
    '''
    Test the ability to add a category to the database.

    Author Grace Hu
    '''
    trans_orm = transaction_db
    tup = (1, 9.99, 'food', '2023-03-23', 'fast-food', 'cash')
    updated_example_data_dict = example_data_dict
    updated_example_data_dict.append({
        'id': tup[0],
        'amount': tup[1],
        'category': tup[2],
        'date': tup[3],
        'description': tup[4],
        'payment': tup[5]
    })

    trans_orm.add(tup)

    results = trans_orm.select_all(())

    assert results == updated_example_data_dict


def test_add(transaction_db, example_data_dict):
    '''
    Test adding a transaction to db
    
    Author: Nathan Tran
    '''
    trans_orm = transaction_db

    tup = (8, 200.0, 'bike', '2023-04-13', 'transportation')
    updated_example_data_dict = example_data_dict
    updated_example_data_dict.append({
        'id': tup[0],
        'amount': tup[1],
        'category': tup[2],
        'date': tup[3],
        'description': tup[4]
    })

    trans_orm.add(tup)

    results = trans_orm.select_all(())

    assert results == updated_example_data_dict

def test_del(transaction_db, example_data_dict):
    '''
    Test deleting a transaction from db
    
    Author: Nathan Tran
    '''
    trans_orm = transaction_db

    tup = (7, 1250.0, 'Ipad', '2019-05-19', 'tablet')
    updated_example_data_dict = example_data_dict
    updated_example_data_dict.remove({
        'id': tup[0],
        'amount': tup[1],
        'category': tup[2],
        'date': tup[3],
        'description': tup[4]
    })

    trans_orm.delete(str(tup[0]))

    results = trans_orm.select_all(())

    assert results == updated_example_data_dict
