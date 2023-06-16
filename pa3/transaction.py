'''
Tracks finances with persistence in SQL database

Author: Nathan Tran
'''
import sqlite3

def to_dict(row):
    '''
    Return a dictionary entry for each row 
    row = (item #, amount, category, date, description)
    '''
    transaction = {
        'item_number':row[0], 
        'amount':row[1], 
        'category':row[2], 
        'date':row[3], 
        'description':row[4]
    }
    return transaction

class Transaction():
    def __init__(self, filename):
        '''
        Initializes Transaction Class with db file location
        '''
        self.conn = sqlite3.connect(filename)
        self.cur = self.conn.cursor()
        self.cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER,
            amount FLOAT,
            category TEXT,
            date DATE,
            description TEXT
            )
            '''
        )
        self.conn.commit()
    
    def print_menu(self):
        '''
        Prints a menu of all available commands
        '''
        print(
            '''
            1. show categories
            2. add category
            3. modify category
            4. show transactions
            5. add transaction
            6. delete transaction
            7. summarize transactions by date
            8. summarize transactions by month
            9. summarize transactions by year
            10. summarize transactions by category
            '''
        )

    def show_categories(self):
        '''
        Shows the distict categories stored in the db
        '''
        self.cur.execute("SELECT * FROM transactions")
        rows = self.cur.fetchall()
        categories = [row[0] for row in rows]
        return categories

    def add_category(self, cat):
        '''
        Adds a category to the database
        '''
        self.cur.execute("INSERT INTO transactions (item) VALUES (?)", (cat))
        self.conn.commit()

    def modify_category(self, old, new):
        '''
        Modifies category to new category
        '''
        self.cur.execute("UPDATE transactions SET category=? WHERE category=?", (new, old))
        self.conn.commit()

    def show_transactions(self):
        '''
        Returns all transactions
        '''
        self.cur.execute("SELECT * FROM transactions")
        rows = self.cur.fetchall()
        transactions = [to_dict(row) for row in rows]
        return transactions

    def add_transaction(self, t):
        '''
        Adds a transaction to the database
        '''
        self.cur.execute(
            "INSERT INTO transactions VALUES(?,?,?,?,?)", 
            (t['item_number'], t['amount'], t['category'], t['date'], t['description'])
        )
        self.conn.commit()

    def delete_transaction(self, id):
        '''
        Deletes a transaction with id
        '''
        self.cur.execute("DELETE FROM transactions WHERE id=?", (id))
        self.conn.commit()

    def sum_date(self):
        '''
        Summarizes transactions by date
        Dates formatted MM-DD-YYYY
        '''
        self.cur.execute('SELECT date, SUM(amount) FROM transactions GROUP BY date')
        rows = self.cur.fetchall()
        sum = [{'date': row[0], 'total': row[1]} for row in rows]
        return sum

    def sum_month(self): 
        '''
        Summarizes transactions by month
        '''
        self.cur.execute('SELECT SUBSTR(date, 1, 2) AS month, SUM(amount) FROM transactions GROUP BY month')
        rows = self.cur.fetchall()
        sum = [{'month': row[0], 'total': row[1]} for row in rows]
        return sum
    
    def sum_year(self):   
        '''
        Summarizes transactions by year
        '''
        self.cur.execute('SELECT SUBSTR(date, 7, 10) AS year, SUM(amount) FROM transactions GROUP BY year')
        rows = self.cur.fetchall()
        sum = [{'year': row[0], 'total': row[1]} for row in rows]
        return sum
    
    def sum_category(self): 
        '''
        Summarizes transactions by categpory
        '''
        self.cur.execute('SELECT category, SUM(amount) FROM transactions GROUP BY category')
        rows = self.cur.fetchall()
        sum = [{'category': row[0], 'total': row[1]} for row in rows]
        return sum
    

  