#  Rate Limiting

This project implements a custom rate-limiting decorator that restricts how many times a user or client can access a given view within a defined time window.

---

### First 5 Requests (within 60s)

**GET** `/api/recipes/`  

#### Success Response:
#### Code: 200 OK

```json
    {
      (recipe details)
    }
```

### 6 or more Requests (within 60s)

#### Error Response:
#### Code: 429 Too Many Requests

```json
    {
       "detail": "Too many requests. Please try again later."
    }
```
