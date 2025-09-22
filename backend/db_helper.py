import mysql.connector
from contextlib import contextmanager
import os
import sys

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root292511',
        database='expense_manager'
    )

    if connection.is_connected():
        print("Connected to MySQL database")

    cursor = connection.cursor(dictionary=True)

    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()


def fetch_expenses_for_date(expense_date):
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses
    
def delete_expenses_for_date(expense_date):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,)) 

def insertexpense(expense_date, amount, category, notes):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )

def fetch_expense_summary(start_date, end_date):
    with get_db_cursor() as cursor:
        cursor.execute(
            '''
            SELECT category, SUM(amount) as total
            FROM expenses
            WHERE expense_date BETWEEN %s AND %s
            GROUP BY category
            ''', 
            (start_date, end_date)
        )
        summary = cursor.fetchall()
        return summary

if __name__ == "__main__":
    # exp = fetch_expenses_for_date('2024-08-01')
    # print(exp)
    # print(fetch_expense_summary('2024-08-01', '2024-08-31') )

    p
      