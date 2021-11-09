from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from . import models
from . import schemas


def get_all(db: Session):
    users = db.query(models.User).all()
    return users


def create_user(request: schemas.User, db: Session):
    new_user = models.User(email=request.email,
                           username=request.username,
                           password=request.password
                           )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def update_password(id: int, request: schemas.UserUpdate, db: Session):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

    user.update(request.dict())
    db.commit()
    return 'updated'


def delete_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if user:
        db.delete(user)
        db.commit()
        return 'success'
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Users not found')


def search_user(username, db: Session):
    user = db.query(models.User).filter(models.User.username == username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

    return user
