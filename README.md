## User Registration with Profile Picture Upload

his feature enhances the user registration process by allowing users to upload a profile picture during registration. The system supports:

-  **Accepted image types:** JPEG, PNG, WebP
-  **Maximum file size:** 2MB

---

### Headers
---

**PUT** `/api/auth/profile`  
**Content-Type:** `form-data`

| Field           | Type   | Description                                 |
|----------------|--------|---------------------------------------------|
| `username`      | Text   | The username of the new user                |
| `password`      | Text   | The password for the new user               |
| `email`         | Text   | User's email address                        |
| `bio`           | Text   | Short bio (optional)                        |
| `profile_picture` | File | Profile image (JPEG, PNG, or WebP under 2MB) |

>  Set the `profile_picture` field type to **File** in Postman, not Text.

### Successful Response

**HTTP 201 Created**

```json
{
  "id": 3,
  "username": "testuser3",
  "email": "testuser3@example.com",
  "bio": "This is my test bio.",
  "profile_picture": "http://localhost:8000/media/profile_pics/example.jpg"
}


### Error Response

**HTTP 201 Created**

```json
{
  "profile_picture": ["Unsupported file extension. Use JPG, PNG, or WebP."]
}

**File Size Too Large**
**HTTP 400 Bad Request**

```json
{
  "profile_picture": ["Unsupported file extension. Use JPG, PNG, or WebP."]
}

