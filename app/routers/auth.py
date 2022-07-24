from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import Token
from app import models,utils,oauth2
from fastapi.security import OAuth2PasswordRequestForm

router =APIRouter(prefix='/login',tags=['Authentication'])

@router.post('/',response_model=Token)
def login(user_credentials: OAuth2PasswordRequestForm =Depends(),db: Session=Depends(get_db)):
    user =db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= 'Invalid Credentials')
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Wrong Password')
    
    access_token =oauth2.create_access_token(data={"user_id" :user.id})
    return {"access_token" :access_token,"token_type": "bearer"}
    
