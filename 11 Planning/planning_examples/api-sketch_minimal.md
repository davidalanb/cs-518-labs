## Data model:

```python

class Adventure:

    # set after DB insertion
    id: Optional[str]

    # user who created this adventure
    user_id: str
    username: str

    # name and description
    adv_name: str
    adv_desc: str

class AdventureUpdate:

    id: str

    # TODO: add any Adventure fields that can be modified

```

## API 

### client function signatures:

```python
create_adventure(adv: dict) -> str
read_adventure(id: str) -> dict
update_adventure(id: str, update: dict) -> int
delete_adventure(id) -> int
```

You should also specify exceptions.

### REST API endpoints

```
POST /adventures/
    body: Adventure
GET /adventures/{id}
    returns: Adventure
PUT /adventures/{id}
    body: AdventureUpdate
DELETE /adventures/{id}
```