from fastapi import FastAPI, HTTPException, status, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

users = {
    1: {"name": "Lena Oxton", "hero": "Tracer", "role": "damage", "age": 28},
    2: {"name": "Angela Ziegler", "hero": "Mercy", "role": "support", "age": 39},
    3: {"name": "Jack Morrison", "hero": "Soldier: 76", "role": "damage", "age": 58},
    4: {"name": "Gabriel Reyes", "hero": "Reaper", "role": "damage", "age": 58},
    5: {"name": "Hanzo Shimada", "hero": "Hanzo", "role": "damage", "age": 38},
    6: {"name": "Genji Shimada", "hero": "Genji", "role": "damage", "age": 35},
    7: {"name": "Torbjörn Lindholm", "hero": "Torbjörn", "role": "damage", "age": 57},
    8: {"name": "Mei-Ling Zhou", "hero": "Mei", "role": "damage", "age": 31},
    9: {"name": "Jesse McCree", "hero": "McCree", "role": "damage", "age": 37},
    10: {"name": "Fareeha Amari", "hero": "Pharah", "role": "damage", "age": 32},
    11: {"name": "Amélie Lacroix", "hero": "Widowmaker", "role": "damage", "age": 33},
    12: {"name": "Winston", "hero": "Winston", "role": "tank", "age": 29},
    13: {"name": "Reinhardt Wilhelm", "hero": "Reinhardt", "role": "tank", "age": 63},
    14: {"name": "Mako Rutledge", "hero": "Roadhog", "role": "tank", "age": 48},
    15: {"name": "Jamison Fawkes", "hero": "Junkrat", "role": "damage", "age": 25},
    16: {"name": "Zarya", "hero": "Zarya", "role": "tank", "age": 28},
    17: {"name": "Bastion", "hero": "Bastion", "role": "damage", "age": 30},
    18: {"name": "Sombra", "hero": "Sombra", "role": "damage", "age": 30},
    19: {"name": "Lucio Correia dos Santos", "hero": "Lúcio", "role": "support", "age": 26},
    20: {"name": "Zenyatta", "hero": "Zenyatta", "role": "support", "age": 20},
    21: {"name": "Symmetra", "hero": "Symmetra", "role": "damage", "age": 28},
}

class User(BaseModel):
    name: str
    hero: str
    role: str
    age: int

class UpdateUser(BaseModel):
    name: Optional[str] = None
    hero: Optional[str] = None
    role: Optional[str] = None
    age: Optional[int] = None

#Get users
@app.get("/users/{user_id}")
def get_user(user_id:int = Path(...,description="User ID", gt=0, lt=100 )):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

#Create user
@app.post("/users/{user_id}", status_code=status.HTTP_201_CREATED)
def create_user(user_id:int ,user: User):
    if user_id in users:
        raise HTTPException(status_code=409, detail="User already exists")
    users[user_id] = user.model_dump()
    return user

#Update user
@app.put("/users/{user_id}")
def update_user(user_id: int, user: UpdateUser):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    stored_user = users[user_id]
    update_data = user.dict(exclude_unset=True)

    stored_user.update(update_data)
    users[user_id] = stored_user
    return stored_user


#Delete user
@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user = users.pop(user_id)
    return {"message": "User has been deleted","deleted_user": deleted_user}


#Search for a user
@app.get("/users/search/")
def search_by_name(name:Optional[str] = None):
    if not name:
        return {"message": "Name required"}

    for user in users.values():
        if user["name"] == name:
            return user

    raise HTTPException(status_code=404, detail="User not found")