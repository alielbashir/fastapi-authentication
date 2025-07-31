# FastAPI Authentication

A FastAPI application demonstrating JWT-based authentication with user registration and login.

## Quick Start

### Using uv (Recommended)

```bash
# Clone and setup
git clone <your-repo-url>
cd fastapi-authentication

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv sync

# Run the application
fastapi dev src/main.py
```

### Using pip

```bash
# Clone and setup
git clone <your-repo-url>
cd fastapi-authentication

# Create virtual environment and install dependencies
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .

# Run the application
fastapi dev src/main.py
```

## API Endpoints

- `POST /register` - Register a new user
- `POST /login` - Login and receive JWT token
- `GET /protected` - Protected endpoint (requires JWT token)
- `GET /unprotected` - Public endpoint

**API Documentation**: http://localhost:8000/docs

## Usage

```bash
# Register
curl -X POST "http://localhost:8000/register" \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "testpass"}'

# Login
curl -X POST "http://localhost:8000/login" \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "testpass"}'

# Access protected endpoint
curl -X GET "http://localhost:8000/protected" \
     -H "Authorization: Bearer YOUR_JWT_TOKEN_HERE"
```