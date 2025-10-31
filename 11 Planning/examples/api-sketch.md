## Data model:

```python
class Difficulty(int, Enum):
    VERY_EASY = 1
    EASY = 2
    MODERATE = 3
    DIFFICULT = 4
    VERY_DIFFICULT = 5

class Adventure:

    # set after DB insertion
    id: str

    # required at creation
    user_id: str
    username: str
    adv_name: str

    # can be specified later
    required_gear: list[str]
    max_group_size: int
    difficulty: Difficulty
    reg_deadline: datetime
    location_lat: float
    location_long: float
    start_dt: datetime
    end_dt: datetime

class AdventureUpdate:
    '''
    You can do collection operations like this (below), or you can do them like we did in class.
    '''

    # TODO: add any Adventure fields that can be modified

    # Fields for collection operations
    gear_to_add: Optional[list[str]]    
    gear_to_remove: Optional[list[str]] set
    gear_to_replace: Optional[list[str]] 
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