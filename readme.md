# Expense Tracking System

A full-stack expense tracking application that allows users to manage their daily expenses with analytics and reporting features. Built with FastAPI backend, Streamlit frontend, and MySQL database.

## What is this project?

This expense tracking system helps you record, manage, and analyze your daily expenses. The application features:
- Add and update expenses by date
- Categorize expenses for better organization
- View detailed analytics and expense breakdowns
- Interactive web interface for easy data entry
- RESTful API for expense management

## Project Structure

```
project-expense-tracking/
├── readme.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── backend/                     # FastAPI backend server
│   ├── server.py               # Main FastAPI application
│   ├── db_helper.py            # Database connection and operations
│   ├── logging_setup.py        # Logging configuration
│   └── server.log              # Application logs
├── frontend/                   # Streamlit frontend application
│   ├── app.py                  # Main Streamlit app
│   ├── form_tab.py             # Expense entry form
│   └── analytics_tab.py        # Analytics and reporting
└── test/                       # Test suite
    ├── conftest.py             # Test configuration
    ├── backend/
    │   └── test_db_helper.py   # Backend tests
    └── frontend/               # Frontend tests
```

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- MySQL Server
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/t3tobi00/expense-tracking.git
cd expense-tracking
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Database Setup
1. Install and start MySQL Server
2. Create a database named `expense_manager`
3. Update database credentials in `backend/db_helper.py` if needed:
   ```python
   # Update these values to match your MySQL setup
   host='localhost'
   user='root'
   password='your_password'
   database='expense_manager'
   ```

### 4. Run the Backend Server
```bash
cd backend
uvicorn server:app --reload --port 8000
```
The API will be available at `http://localhost:8000`

### 5. Run the Frontend Application
Open a new terminal:
```bash
cd frontend
streamlit run app.py
```
The web application will open in your browser at `http://localhost:8501`

### 6. Running Tests
```bash
pytest test/
```

## Usage

1. **Adding Expenses**: Use the "Add/Update" tab to enter your daily expenses with amount, category, and notes
2. **Analytics**: View the "Analytics" tab to see expense summaries and category breakdowns
3. **API Access**: The backend provides RESTful endpoints for programmatic access to expense data

## API Endpoints

- `GET /expenses/{date}` - Retrieve expenses for a specific date
- `POST /expenses/{date}` - Add or update expenses for a date
- `POST /analytics/` - Get expense analytics for a date range

## Technologies Used

- **Backend**: FastAPI, MySQL, Pydantic
- **Frontend**: Streamlit, Pandas
- **Testing**: Pytest
- **Database**: MySQL Connector