# Python Backend Testing

A simple REST API built with Flask, similar to Express.js in Node.js.

## Project Structure

```
app.py                  # Main application entry point
requirements.txt        # Project dependencies
app/
  controllers/          # Business logic
    user_controller.py  # User-related API logic
  models/               # Data models
    user.py             # User model definition
  routes/               # API route definitions
    user_routes.py      # User-related routes
```

## Getting Started

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Installation

1. Clone the repository
2. Set up a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

```
python app.py
```

The API will be available at: http://127.0.0.1:5000

## API Endpoints

### Users

- **GET /api/users** - Get all users
- **POST /api/users** - Create a new user
  - Body: `{ "name": "John Doe", "email": "john@example.com" }`
- **GET /api/users/:id** - Get a specific user by ID
- **PUT /api/users/:id** - Update a user
  - Body: `{ "name": "Updated Name", "email": "updated@example.com" }`
- **DELETE /api/users/:id** - Delete a user

## Example Usage

### Creating a User

```bash
curl -X POST http://127.0.0.1:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```

### Getting all Users

```bash
curl http://127.0.0.1:5000/api/users
```

## Extending the API

To add new API resources:

1. Create a new model in `app/models/`
2. Create a controller in `app/controllers/`
3. Define routes in `app/routes/` 
4. Register the routes in `app.py`

