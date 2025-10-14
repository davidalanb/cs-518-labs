Mapping user_api to new REST API (v1 and v2)

| user_api               | v1                    | v2                              | returns          |
|------------------------|---------------------  |-------------------------        |------------------|
| read_by_id(id)         | GET /users/?id=x      | GET /users/{user_id}            | User             |
| read_all()             | GET /users/           | GET /users/                     | UserCollection   |
| read({'username':un})  | GET /users/{username} | GET /users/?username=username   | User (v1), UserCollection (v2) |

Notes:

* v2 is better because 
    - it is idiomatic for the path param to be an id
    - it's better if we want to allow for changing usernames
    - GET /users/ always returns a UserCollection

---

What functions are being used by accounts routes?

flask route             user_api / client       restAPI 
POST /users/create      create                  POST /users

POST /users/            read_all                GET /users/

GET /users/<username>     read_by_username        GET /users/{un}
POST /users/<username>    update(id,update)            PUT /users/?id={id}

POST /users/delete/all  delete_all              DELETE /users/all    
POST /users/delete/<username> delete(query)   DELETE /users/{un}

POST /login             authenticate(query)     POST /users/authenticate