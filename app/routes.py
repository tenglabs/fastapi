from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from . import database
from . import schemas
from . import users


router = APIRouter(
    prefix="/users",
    tags=['users'])


@router.post("/create-user", status_code=201)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return users.create_user(request, db)


@router.put("/update-password/{id}", status_code=200)
def update_password(id, request: schemas.UserUpdate, db: Session = Depends(database.get_db)):
    return users.update_password(id, request, db)


@router.delete("/delete-user/{id}", status_code=200)
def delete_user(id, db: Session = Depends(database.get_db)):
    return users.delete_user(id, db)


@router.get("/get-user-list", response_model=List[schemas.ShowUser])
def get_user_list(db: Session = Depends(database.get_db)):
    return users.get_all(db)


@router.get("/search/{name}", response_model=schemas.ShowUser)
def search(username, db: Session = Depends(database.get_db)):
    return users.search_user(username, db)
