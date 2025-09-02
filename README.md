# WhatBytesInternshipAssignment

## 🏥 Healthcare Backend API

A comprehensive Django REST Framework backend for a healthcare application with JWT authentication, PostgreSQL database, and complete CRUD operations for patients, doctors, and patient-doctor mappings.

## 📋 Project Overview

This project implements a secure healthcare backend system that allows:

- User registration and authentication
- Patient management (CRUD operations)
- Doctor management (CRUD operations)
- Patient-Doctor relationship mapping
- JWT-based security
- PostgreSQL database integration

## 🛠️ Technologies Used

- **Backend Framework**: Django 5.1.1
- **API Framework**: Django REST Framework 3.15.2
- **Authentication**: JWT (djangorestframework-simplejwt 5.3.1)
- **Database**: PostgreSQL
- **Environment Management**: python-dotenv
- **Database Driver**: psycopg2-binary

## 📁 Project Structure

```
healthcare/
├── healthcare/                 # Main Django project
│   ├── __init__.py
│   ├── settings.py            # Project settings with PostgreSQL config
│   ├── urls.py                # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── users/                     # User authentication app
│   ├── models.py
│   ├── serializers.py         # Register/Login serializers
│   ├── views.py               # Auth views
│   └── urls.py                # Auth URL patterns
├── patients/                  # Patient management app
│   ├── models.py              # Patient & Mapping models
│   ├── serializers.py         # Patient & Mapping serializers
│   ├── views.py               # Patient & Mapping views
│   └── urls.py                # Patient & Mapping URL patterns
├── doctors/                   # Doctor management app
│   ├── models.py              # Doctor model
│   ├── serializers.py         # Doctor serializer
│   ├── views.py               # Doctor views
│   └── urls.py                # Doctor URL patterns
├── .env                       # Environment variables
├── manage.py                  # Django management script
└── requirements.txt           # Python dependencies
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)

### 1. Clone & Navigate

```bash
cd healthcare
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create `.env` file in the healthcare directory:

```env
SECRET_KEY=your-secret-key-here
DB_NAME=healthcare_db
DB_USER=your-postgres-username
DB_PASSWORD=your-postgres-password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Database Setup

```bash
# Create PostgreSQL database
createdb healthcare_db

# Run migrations
python manage.py migrate
```

### 6. Start Development Server

```bash
python manage.py runserver
```

**Server will be available at:** `http://127.0.0.1:8000/`

## 🔐 API Endpoints

### Authentication Endpoints

#### 1. User Registration

```http
POST /api/auth/register/
Content-Type: application/json

{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepassword123"
}
```

**Response (201 Created):**

```json
{
  "message": "User registered successfully"
}
```

#### 2. User Login

```http
POST /api/auth/login/
Content-Type: application/json

{
    "username": "john@example.com",
    "password": "securepassword123"
}
```

**Response (200 OK):**

```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Patient Management Endpoints

#### 3. Create Patient

```http
POST /api/patients/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "first_name": "Alice",
    "last_name": "Smith",
    "age": 30,
    "gender": "Female"
}
```

#### 4. List User's Patients

```http
GET /api/patients/
Authorization: Bearer <access_token>
```

#### 5. Get Specific Patient

```http
GET /api/patients/{id}/
Authorization: Bearer <access_token>
```

#### 6. Update Patient

```http
PUT /api/patients/{id}/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "first_name": "Alice",
    "last_name": "Johnson",
    "age": 31,
    "gender": "Female"
}
```

#### 7. Delete Patient

```http
DELETE /api/patients/{id}/
Authorization: Bearer <access_token>
```

### Doctor Management Endpoints

#### 8. Create Doctor

```http
POST /api/doctors/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "first_name": "Dr. Sarah",
    "last_name": "Johnson",
    "specialization": "Cardiology",
    "email": "sarah@hospital.com",
    "phone": "+1234567890"
}
```

#### 9. List All Doctors

```http
GET /api/doctors/
Authorization: Bearer <access_token>
```

#### 10. Get Specific Doctor

```http
GET /api/doctors/{id}/
Authorization: Bearer <access_token>
```

#### 11. Update Doctor

```http
PUT /api/doctors/{id}/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "first_name": "Dr. Sarah",
    "last_name": "Smith",
    "specialization": "Cardiology",
    "email": "sarah@hospital.com",
    "phone": "+1234567890"
}
```

#### 12. Delete Doctor

```http
DELETE /api/doctors/{id}/
Authorization: Bearer <access_token>
```

### Patient-Doctor Mapping Endpoints

#### 13. Create Patient-Doctor Mapping

```http
POST /api/patients/mappings/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "patient": 1,
    "doctor": 1
}
```

#### 14. List All Mappings

```http
GET /api/patients/mappings/
Authorization: Bearer <access_token>
```

#### 15. Get Doctors for Specific Patient

```http
GET /api/patients/mappings/{patient_id}/
Authorization: Bearer <access_token>
```

#### 16. Delete Mapping

```http
DELETE /api/patients/mappings/delete/{mapping_id}/
Authorization: Bearer <access_token>
```

## 🧪 API Testing Guide

### Using Postman

1. **Set Base URL**: `http://127.0.0.1:8000`
2. **Set Content-Type**: `application/json` for all requests
3. **Authentication**: Use Bearer Token for protected endpoints

### Testing Sequence

1. **Register User** → Get user credentials
2. **Login** → Get JWT access token
3. **Create Doctor** → Get doctor ID
4. **Create Patient** → Get patient ID
5. **Create Mapping** → Link patient and doctor
6. **Test all CRUD operations**

### Sample Test Data

**Doctor:**

```json
{
  "first_name": "Dr. Sarah",
  "last_name": "Johnson",
  "specialization": "Cardiology",
  "email": "sarah@hospital.com",
  "phone": "+1234567890"
}
```

**Patient:**

```json
{
  "first_name": "Alice",
  "last_name": "Smith",
  "age": 30,
  "gender": "Female"
}
```

**Mapping:**

```json
{
  "patient": 1,
  "doctor": 1
}
```

## 🔒 Security Features

- **JWT Authentication**: Secure token-based authentication
- **User-specific Data**: Patients are filtered by the authenticated user
- **Permission Classes**: All endpoints require authentication
- **Environment Variables**: Sensitive data stored securely
- **Input Validation**: Comprehensive validation using Django forms

## 🗄️ Database Models

### User Model

- Extends Django's built-in User model
- Email used as username for authentication

### Patient Model

```python
class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
```

### Doctor Model

```python
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
```

### PatientDoctorMapping Model

```python
class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('patient', 'doctor')
```

## 📊 Response Examples

### Successful Patient Creation

```json
{
  "id": 1,
  "first_name": "Alice",
  "last_name": "Smith",
  "age": 30,
  "gender": "Female",
  "created_at": "2025-09-01T23:35:09.123456Z",
  "added_by": 1
}
```

### Doctor List Response

```json
[
  {
    "id": 1,
    "first_name": "Dr. Sarah",
    "last_name": "Johnson",
    "specialization": "Cardiology",
    "email": "sarah@hospital.com",
    "phone": "+1234567890",
    "created_at": "2025-09-01T23:07:20.123456Z"
  }
]
```

### Mapping Creation Response

```json
{
  "id": 1,
  "patient": 1,
  "doctor": 1,
  "patient_name": "Alice Smith",
  "doctor_name": "Dr. Sarah Johnson",
  "assigned_at": "2025-09-01T23:47:42.123456Z"
}
```

## 🚨 Error Handling

### Authentication Error

```json
{
  "detail": "Authentication credentials were not provided."
}
```

### Validation Error

```json
{
  "age": ["Ensure this value is less than or equal to 150."],
  "gender": ["\"Invalid\" is not a valid choice."]
}
```

### Not Found Error

```json
{
  "detail": "Not found."
}
```

## 🧪 Running Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test patients
python manage.py test doctors
python manage.py test users
```

## 📝 Additional Notes

- **Database**: Uses PostgreSQL for production-ready data storage
- **Migrations**: All database migrations are included
- **Environment**: Configured for both development and production
- **CORS**: Ready for frontend integration
- **Documentation**: Complete API documentation included

## 🎯 Project Status

✅ **COMPLETED FEATURES:**

- User registration and JWT authentication
- Complete patient CRUD operations
- Complete doctor CRUD operations
- Patient-doctor relationship mapping
- PostgreSQL database integration
- Environment variable configuration
- Input validation and error handling
- Comprehensive API testing

## 📞 Support

For any issues or questions:

1. Check the server logs for detailed error messages
2. Verify JWT token is valid and not expired
3. Ensure all required fields are provided in requests
4. Check database connectivity

---

**🚀 Project successfully implemented and tested! All APIs are working perfectly.**
