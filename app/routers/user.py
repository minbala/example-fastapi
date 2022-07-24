from app import models
from app.database import get_db
from fastapi import  Response,status,HTTPException,Depends,APIRouter
from app.schemas import UserCreate,UserOut
from typing import List
from sqlalchemy.orm import Session
from app.utils import hash

router =APIRouter(prefix="/users",tags=['Users'])

@router.get('/',response_model= List[UserOut])
def get_users(db: Session= Depends(get_db)):
    return db.query(models.User).all()

@router.get('/{id}', response_model= UserOut)
def get_user(id: int, db: Session =Depends(get_db)):
    user=db.query(models.User).filter(models.User.id== id).first()
    
    if user is None:
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {id} was not found")
    return user

@router.post("/",status_code=status.HTTP_201_CREATED,response_model= UserOut)
def create_user(user: UserCreate,db: Session= Depends(get_db)):
    user.password =hash(user.password)
    new_user =models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session= Depends(get_db)):
    user_query=db.query(models.User).filter(models.User.id== id)
    if user_query.first() is None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= f'user with id: {id} was not found')
    user_query.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code= status.HTTP_204_NO_CONTENT)

@router.put("/{id}",)
def update_user(id: int, user: UserCreate, db: Session =Depends(get_db)):
    user_query= db.query(models.User).filter(models.User.id== id)
    if user_query.first() is None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
                            detail= f'user with id: {id} was not found')
    user_query.update(user.dict(), synchronize_session= False)
    
    return user_query.first()