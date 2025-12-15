# Productify

A full-stack web application for product management, built with FastAPI (backend) and React (frontend). This application allows users to perform CRUD operations on products, including viewing, adding, updating, and deleting product information.

## Features

- **Backend (FastAPI)**:
  - RESTful API for product management
  - PostgreSQL database integration with SQLAlchemy
  - CORS support for frontend communication
  - Automatic database initialization with sample data

- **Frontend (React)**:
  - Modern React application
  - Axios for API communication
  - Responsive UI components

## Tech Stack

- **Backend**: FastAPI, SQLAlchemy, PostgreSQL, Pydantic, Uvicorn
- **Frontend**: React, Axios
- **Database**: PostgreSQL

## Project Structure

```
productify/
├── main.py                 # FastAPI application entry point
├── models.py               # Pydantic models
├── database.py             # Database configuration
├── database_models.py      # SQLAlchemy models
├── requirements.txt        # Backend dependencies
├── FastAPI.md              # API documentation
├── frontend/               # React frontend
│   ├── package.json
│   ├── public/
│   │   ├── index.html
│   │   └── manifest.json
│   └── src/
│       ├── App.js
│       ├── App.css
│       ├── index.js
│       ├── index.css
│       ├── TaglineSection.js
│       └── TaglineSection.css
└── README.md               # This file
```

## Installation and Setup

### Prerequisites

- Python 3.8+
- Node.js 14+
- PostgreSQL database

### Backend Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/pranavkavade20/productify.git
   cd productify
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL database**:
   - Create a PostgreSQL database
   - Update database connection details in `database.py` if necessary

5. **Run the backend**:
   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
   npm start
   ```

   The frontend will be available at `http://localhost:3000`

## API Endpoints

The FastAPI backend provides the following endpoints:

- `GET /` - Welcome message
- `GET /products` - Retrieve all products
- `GET /products/{id}` - Retrieve a specific product by ID
- `POST /products` - Create a new product
- `PUT /products/{id}` - Update an existing product
- `DELETE /products/{id}` - Delete a product

### API Documentation

When the backend is running, you can access:
- Interactive API docs: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`

## Usage

1. Start both backend and frontend servers as described above
2. Open your browser and navigate to `http://localhost:3000`
3. Use the React frontend to interact with the product management system
4. The frontend communicates with the FastAPI backend via HTTP requests

## Development

- Backend code is in `main.py`, `models.py`, `database.py`, and `database_models.py`
- Frontend code is in the `frontend/src/` directory
- Modify the code and restart the respective servers to see changes

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the license file for details.