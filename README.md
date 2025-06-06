## Recipedia
Recipedia is a RESTful API built using Django and Django REST Framework that enables authenticated users to create, manage, and explore cooking recipes. It includes full CRUD support, user authentication, bookmarking functionality, profile image handling, and a custom rate-limiting mechanism.

---

## Features
User registration and login with JWT authentication

CRUD operations for recipes, categories, and bookmarks

Profile image upload with validation and auto-cropping

Rate limiting via custom decorator

Token refresh endpoint


## Installation

### Clone the repository

bash
git clone https://github.com/EliziahPadullon/recipedia.git
cd recipedia

### Set up a virtual environment

bash
python -m venv venv
source venv/bin/activate

### Install dependencies

bash
pip install -r requirements.txt

### Run migrations

bash
python manage.py makemigrations
python manage.py migrate

### Start the development server
bash
python manage.py runserver

## API Endpoints

### Authentication
Method	Endpoint	Description
POST	/api/auth/register/	Register a new user
POST	/api/auth/login/	Obtain JWT access and refresh tokens
POST	/api/auth/token/refresh/	Refresh the access token

### Recipes CRUD
**Method	Endpoint	Description**
GET	/api/recipes/	List all recipes
POST	/api/recipes/	Create a new recipe
GET	/api/recipes/<id>/	Retrieve a recipe
PUT	/api/recipes/<id>/	Update a recipe
PATCH	/api/recipes/<id>/	Partially update a recipe
DELETE	/api/recipes/<id>/	Delete a recipe

**Sample Request Body (POST / PUT / PATCH)**
{
  "title": "Pasta Carbonara",
  "ingredients": "Pasta, Eggs, Cheese, Bacon",
  "instructions": "Boil pasta. Mix with other ingredients."
}

**Expected Response (201 Created)**
{
  "id": 1,
  "title": "Pasta Carbonara",
  "ingredients": "Pasta, Eggs, Cheese, Bacon",
  "instructions": "Boil pasta. Mix with other ingredients.",
  "author": "testuser"
}

### Bookmarks
**Method	Endpoint	Description**
POST	/api/recipes/bookmarks/	Create a bookmark
GET	/api/recipes/bookmarks/	List user bookmarks
DELETE	/api/recipes/bookmarks/<id>/	Remove a bookmark

**Sample Request Body (POST)**
{
  "recipe": 1
}

### Categories
**Method	Endpoint	Description**
GET	/api/recipes/categories/	List all categories
POST	/api/recipes/categories/	Create a new category
GET	/api/recipes/categories/<id>/	Retrieve a category
PUT	/api/recipes/categories/<id>/	Update a category
DELETE	/api/recipes/categories/<id>/	Delete a category

**Sample Request Body (POST)**
{
  "name": "Desserts"
}

### Profile Picture Upload
**Field: profile_picture**

Accepted formats: .jpg, .jpeg, .png, .webp

Max size: 2MB

Automatically cropped to a 1:1 aspect ratio on upload

Upload via multipart/form-data

### Rate Limiting
A custom decorator limits the number of API requests allowed within a specified time window (e.g., 5 requests per minute).

If the rate limit is exceeded:

**Response (429 Too Many Requests)**
{
  "error": "Rate limit exceeded. Try again later."
}


# License
This project is licensed under the MIT License.
