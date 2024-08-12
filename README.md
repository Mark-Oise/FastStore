# FastStore

This project is a simple iPhone product store built with FastAPI for the backend and React for the frontend. It allows users to browse iPhone products, add them to a cart, and place orders.

## Features

- Product listing with filtering and sorting options
- Product detail view
- Shopping cart functionality
- Coupon application
- Order placement

## Project Structure

```
faststore/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   └── database.py
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   └── .env
└── requirements.txt


```

## Prerequisites

- Python 3.7+
- Node.js 12+
- npm 6+

## Setup

### Backend

1. Navigate to the backend directory:
   ```
   cd faststore/backend
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your database connection in the `.env` file:
   ```
   DATABASE_URL=sqlite:///./test.db
   ```

5. Run the FastAPI server:
   ```
   uvicorn app.main:app --reload
   ```

### Frontend

1. Navigate to the frontend directory:
   ```
   cd faststore/frontend
   ```

2. Install the required packages:
   ```
   npm install
   ```

3. Start the React development server:
   ```
   npm start
   ```

## Usage

After starting both the backend and frontend servers, you can access the application by opening a web browser and navigating to `http://localhost:3000`.

## API Documentation

FastAPI automatically generates API documentation. You can view it by navigating to `http://localhost:8000/docs` when the backend server is running.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.