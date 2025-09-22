from fastapi import FastAPI
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

app = FastAPI()

@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses: List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)

    for exp in expenses:
        db_helper.insertexpense(expense_date, exp.amount, exp.category, exp.notes)
    return {"message": "Expenses added/updated successfully"}