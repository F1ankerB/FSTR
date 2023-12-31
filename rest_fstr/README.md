
# REST API for SkillFactory's FSTR Mountain Pass Database Project

## Overview
This REST API is part of a collaborative project for the Federation of Sport Tourism of Russia (FSTR) by SkillFactory students. The goal is to replace the current cumbersome process of submitting and verifying mountain pass traversals, which is currently managed via email and Google Sheets, with a streamlined mobile application and database system. This API provides backend functionality for the mobile app, allowing tourists to submit pass data and view the verification status.

## Installation and Setup
1. **Clone the Repository**: Clone this repo to your local machine.
2. **Install Dependencies**: Install required Python packages and Django.
3. **Environment Variables**: Set up your database using environment variables. Create a `.env` file in your project root with the following keys:
   - `FSTR_DB_LOGIN`: Your database login.
   - `FSTR_DB_PASS`: Your database password.
   - `FSTR_DB_HOST`: Database host (usually localhost for development).
   - `FSTR_DB_PORT`: Database port.

## Running the Server
Execute `python manage.py runserver` to start the Django server on localhost. The API will be accessible at `http://localhost:8000/`.

## API Endpoints

### Submit Pass Data
- **POST** `/api/submit-data/`
  - Description: Submit new mountain pass data.
  - Request Body: JSON with pass data.
  - Response: Confirmation of submission.

### User Management
- **POST** `/api/user/`
  - Description: Create a new user.
  - Request Body: JSON with user details.
  - Response: User details.

- **GET** `/api/user/<int:id>/`
  - Description: Retrieve user details.
  - Response: User details.

### Coordinate Management
- **POST** `/api/coords/`
  - Description: Add new coordinates.
  - Request Body: JSON with latitude, longitude, and height.
  - Response: Coordinate details.

- **GET** `/api/coords/<int:id>/`
  - Description: Get specific coordinates.
  - Response: Coordinate details.

### Mountain Pass Images
- **POST** `/api/pereval-images/`
  - Description: Upload a new image for a pass.
  - Request Body: Binary image data.
  - Response: Confirmation of upload.

- **GET** `/api/pereval-images/<int:id>/`
  - Description: Retrieve a specific image.
  - Response: Image data.

### Other Endpoints
- Implement similar POST and GET requests for `PerevalAreas` and `SprActivitiesTypes`.

## Sample Requests
Here are some examples of requests you can make to the API when running on localhost:

**Add User**
```http
POST http://localhost:8000/api/user/
Content-Type: application/json

{
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+123456789"
}
```

**Get User**
```http
GET http://localhost:8000/api/user/1/
```

**Add Coordinates**
```http
POST http://localhost:8000/api/coords/
Content-Type: application/json

{
    "latitude": 43.349,
    "longitude": 42.455,
    "height": 1500
}
```
