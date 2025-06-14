# FastAPI Login/Signup Example

This project is a FastAPI server with two pages:
- **/login**: Login page
- **/signup**: Signup page (stores username and password in SQLite)

## How to run

1. Install dependencies:
   ```sh
   pip install fastapi uvicorn jinja2 sqlalchemy
   ```
2. Start the server:
   ```sh
   uvicorn main:app --reload
   ```
3. Open your browser at http://127.0.0.1:8000/signup or /login
