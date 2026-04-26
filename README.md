# Car Dealership Full Stack Application

A full-stack web application for a car dealership built with Django (backend) and React (frontend), using MongoDB for data storage.

## Features

- **Backend (Django)**:
  - REST API for dealers, reviews, and cars
  - User authentication and registration
  - Admin interface
  - Sentiment analysis for reviews
  - MongoDB integration

- **Frontend (React)**:
  - User registration component
  - Responsive design

- **Static Pages**:
  - About Us page
  - Contact Us page

- **CI/CD**:
  - GitHub Actions workflow for automated testing and deployment

## Project Structure

```
capstonefullstack/
├── server/                 # Django backend
│   ├── dealers/           # Dealers app
│   ├── reviews/           # Reviews app
│   ├── cars/              # Cars app
│   ├── authentication/    # Authentication app
│   └── frontend/
│       └── static/        # Static HTML pages
├── frontend/              # React frontend
│   └── src/
│       └── components/
│           └── Register/  # Registration component
└── .github/
    └── workflows/         # CI/CD workflows
```

## Setup Instructions

### Prerequisites

- Python 3.9+
- Node.js 16+
- MongoDB

### Backend Setup

1. Navigate to the server directory:
   ```bash
   cd server
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Populate the database with sample data:
   ```bash
   python manage.py populate_db
   ```

7. Run the Django server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

## API Endpoints

### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `POST /api/auth/logout/` - User logout

### Dealers
- `GET /api/dealerships/` - Get all dealers
- `GET /api/dealerships/<id>/` - Get dealer by ID
- `GET /api/dealerships/state/<state>/` - Get dealers by state

### Reviews
- `GET /api/reviews/<dealer_id>/` - Get reviews for a dealer
- `POST /api/reviews/analyze/` - Analyze sentiment of review text

### Cars
- `GET /api/cars/makes/` - Get all car makes

## Admin Interface

Access the Django admin at `http://localhost:8000/admin/` using the superuser credentials.

## Static Pages

- About Us: `http://localhost:8000/about/`
- Contact Us: `http://localhost:8000/contact/`

## Testing

Run tests with:
```bash
cd server
python manage.py test
```

## Deployment

The project includes a GitHub Actions workflow for CI/CD. The workflow runs tests and builds the application on every push to the main branch.

## Technologies Used

- **Backend**: Django, Django REST Framework, MongoDB, PyMongo
- **Frontend**: React, Bootstrap
- **Authentication**: Django's built-in authentication
- **Styling**: Bootstrap CSS
- **CI/CD**: GitHub Actions