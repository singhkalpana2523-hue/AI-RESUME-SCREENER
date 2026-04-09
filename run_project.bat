@echo off
echo ===============================
echo Starting AI Resume Screener...
echo ===============================

echo.
echo [1] Starting Backend...
cd backend

IF NOT EXIST venv (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate

echo Installing backend dependencies...
python -m pip install -r requirements.txt

start cmd /k "venv\Scripts\activate && uvicorn app.main:app --reload"

cd ..

echo.
echo [2] Starting Frontend...
cd frontend\resume-ui

echo Installing frontend dependencies...
npm install

start cmd /k "npm run dev"

echo.
echo ===============================
echo App is starting...
echo Open: http://localhost:5173
echo ===============================

pause