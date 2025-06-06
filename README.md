# Recipes CRUD Operations

This API allows authenticated users to Create, Read, Update, and Delete recipes.
Authentication Required — Bearer Token (JWT)

---

### Create a New Recipe

**POST** `/api/recipes/`  
**Content-Type:** `application/json`

#### Request Body

```json
{
  "title": "Chocolate Cake",
  "ingredients": "flour, sugar, cocoa powder, eggs",
  "instructions": "Mix ingredients. Bake for 30 mins.",
  "image": "image.png",
  "category": 1
}
```

#### Success Response:
#### Code: 200 OK

```json
{
  "id": 1,
  "title": "Chocolate Cake",
  "ingredients": "flour, sugar, cocoa powder, eggs",
  "instructions": "Mix ingredients. Bake for 30 mins.",
  "image": "image.png",
  "category": 1,
  "user": 2
}
```

### List of All Recipes

**GET** `/api/recipes/`  

#### Success Response:
#### Code: 200 OK

```json
[
  {
    "id": 1,
    "title": "Chocolate Cake",
    "ingredients": "flour, sugar, cocoa powder, eggs",
    "instructions": "Mix ingredients. Bake for 30 mins.",
    "category": 1,
    "image": "image.png",
    "user": 2
  },
  ...
]
```

### Retrieve a single recipe by ID
**GET** `/api/recipes/1/`  

#### Success Response:
#### Code: 200 OK

```json
{
  "id": 1,
  "title": "Chocolate Cake",
  "ingredients": "flour, sugar, cocoa powder, eggs",
  "instructions": "Mix ingredients. Bake for 30 mins.",
  "image": "image.png",
  "category": 1,
  "user": 2
}
```

### Update recipe
**PATCH** `/api/recipes/1/`  

#### Request Body

```json
{
  "title": "Vanilla Cake",
  "ingredients": "flour, sugar, eggs, vanilla",
  "instructions": "Whisk and bake for 25 mins.",
  "image": "image.png",
  "category": 2
}
```

#### Success Response:
#### Code: 200 OK

```json
{
  "id": 1,
  "title": "Vanilla Cake",
  "ingredients": "flour, sugar, eggs, vanilla",
  "instructions": "Whisk and bake for 25 mins.",
  "category": 2,
  "user": 2
}
```

### Delete recipe
**DELETE** `/api/recipes/1/`

#### Success Response:

```json
  No Content
```

















