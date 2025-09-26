from fastapi import FastAPI, HTTPException
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date

app = FastAPI()

@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Error fetching expenses")
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses: List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)

    for exp in expenses:
        db_helper.insertexpense(expense_date, exp.amount, exp.category, exp.notes)
    return {"message": "Expenses added/updated successfully"}


@app.post("/analytics/")
def get_analytics(dateRange: DateRange):
    summary = db_helper.fetch_expense_summary(dateRange.start_date, dateRange.end_date)
    if summary is None:
        raise HTTPException(status_code=500, detail="Error fetching analytics")
    
    total = sum(item['total'] for item in summary)
    breakdown = {}
    for item in summary:
        item['percentage'] = (item['total'] / total * 100) if total != 0 else 0
        breakdown[item['category']] = {
            'total': item['total'],
            'percentage': item['percentage']
        }
    return breakdown