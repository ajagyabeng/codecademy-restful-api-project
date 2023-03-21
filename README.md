# API REFERENCE
---
## Getting Started

Base URL: http://127.0.0.1:8080/api
Authentication: This version of the applications does not require authentication or API keys.

### Endpoints

# Users

### GET /users
- General:
  - Returns a list of user objects.
- Sample: `requests.get("http://127.0.0.1:8080/api/users")`
  
```
[  
{
  "user": {
    "email": "jack@mail.cm",
    "id": 1,
    "public_id": "b2083940-a152-462b-ba17-bd93c42cba81",
    "registered_on": "Fri, 17 Mar 2023 16:28:04 -0000",
    "username": "jack_harlow"
  }
},
{
  "user": {
    "email": "yak@mail.com",
    "id": 2,
    "public_id": "d8474b75-475a-4205-bc7c-6b4bc5dbc9b3",
    "registered_on": "Fri, 17 Mar 2023 17:14:49 -0000",
    "username": "yakubu"
  }
}
]
```

### GET /users/primary-key
- General:
  - Returns a user object with the primary key provided
- Sample: `requests.get("http://127.0.0.1:8080/api/users/1")`
```
{
  "user": {
    "email": "jack@mail.com",
    "id": 1,
    "public_id": "b2083940-a152-462b-ba17-bd93c42cba81",
    "registered_on": "Fri, 17 Mar 2023 16:28:04 -0000",
    "username": "jack_harlow"
  }
}
```

### POST /users
- General:
  - Creates a new user using the submitted username, email, and password.
  - Returns a success message.
- Sample: `requests.post("http://127.0.0.1:8080/api/users", headers={"Content-Type": "application/json", "X-CSRFToken": csrf_token}, json={"username": "Jonjo", "email": "jonjon@gmail.com", "password": "xxxxxxxxxxx"})`

```
{
  "message": "Success! The user has been added to the database."
}
```

### PUT /users/primary-key
- General:
  - Updates the username of the user with the primary key provided.
  - Returns a user object with the primary key provided.
- Sample: `requests.put("http://127.0.0.1:8080/api/users/1", headers={"Content-Type": "application/json"}, json={"username": "jacko"})`
```
{
  "user": {
    "email": "jack@mail.com",
    "id": 1,
    "public_id": "b2083940-a152-462b-ba17-bd93c42cba81",
    "registered_on": "Fri, 17 Mar 2023 16:28:04 -0000",
    "username": "jacko"
  }
}
```

# Venues

### GET /venues

- General:
  - Returns a list of venue objects.
- Sample: `requests.get("http://127.0.0.1:8080/api/venues")`
  
```
[
    {
        "venue": {
            "id": 1,
            "name": "Vida E caffe",
            "address": "Cedi St."
        }
    },
    {
        "venue": {
            "id": 2,
            "name": "KFC",
            "address": "Maranatha St."
        }
    }
]
```

### GET venues/primary-key
- General:
  - Returns a venue object with the primary key provided.
- Sample: `requests.get("http://127.0.0.1:8080/api/venues/1")`
```
{
    "venue": {
        "address": "Cedi St.",
        "id": 1,
        "name": "Vida E caffe"
    }
}
```

### POST /venues
- General:
  - Creates a new user using the submitted username, email, and password.
  - Returns a success message.
- Sample: `requests.post("http://127.0.0.1:8080/api/venues", headers={"Content-Type": "application/json"}, json={"name": "KFC", "address": "Cedi St."})`

```
{
  "message": "Success! Thevenue has been added to the database."
}
```

### PUT /venues/primary-key
- General:
  - Updates the name and/or address of a venue with the primary key.
  - Returns a venue object with the primary key provided.
- Sample: `requests.put("http://127.0.0.1:8080/api/venues/1", headers={"Content-Type": "application/json"}, json={"name": "Burger King"})`

```
{
    "venue": {
        "id": 1,
        "name": "Burger King",
        "address": "Cedi St."
    }
}
```

### DELETE venues/primary-key
- General:
  - Deletes the venue with the primary key.
  - Returns a success message.
- Sample: `requests.delete("http://127.0.0.1:8080/api/venues/1")`

```
{
  "message": "The venue has been deleted."
}
```

<!-- *Italics*

**Bold text**

[Link](http://google.com) -->