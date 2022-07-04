#!/usr/bin/python3
# -*- coding: utf-8 -*-

# pip install uvicorn
# pip install fastapi hypercorn
# pip install bcrypt
# pip install pyjwt
# pip install python-multipart
# pip install passlib
# pip install pydantic[email]
# pip install sqlalchemy
# pip install python-jose[cryptography]
# python -m uvicorn main:app --reload

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
# import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from passlib.hash import bcrypt

# CORS
from fastapi.middleware.cors import CORSMiddleware

# Local imports from same folder
from src import crud, models, schemas
from src.authentication import authenticate_user
from src.database import SessionLocal, engine

# Create all tables
models.Base.metadata.create_all(bind=engine)

# Tags for documentation
tags_metadata=[
    {'name': 'authentication'},{"name": "users"},{"name": "episodes"},{"name": "body_parts"}
]

# Init FastAPI
app=FastAPI(openapi_tags=tags_metadata)

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ==============================
# ======= API METHODS ==========
# ==============================

# ==== AUTHENTICATION ====

from typing import Union
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

# Authentication config
SECRET_KEY="abc123."
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

oauth2_scheme=OAuth2PasswordBearer(tokenUrl='/token')



def create_access_token(data: dict, expires_delta: Union[timedelta, None]=None):
    to_encode=data.copy()
    if expires_delta:
        expire=datetime.utcnow() + expires_delta
    else:
        expire=datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt=jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



@app.post("/token", response_model=schemas.TokenOut, tags=["authentication"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(get_db)):
    user=authenticate_user(db, form_data.username, form_data.password)
    if user == 1:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Incorrect email",
            headers={"WWW-Authenticate": "Bearer"}
        )
    elif user == 2:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    access_token=create_access_token(
        data={"sub": user.email}, 
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer", "session_expires": ACCESS_TOKEN_EXPIRE_MINUTES}


@app.post("/login", response_model=schemas.TokenOut, tags=["authentication"])
async def login(form: schemas.UserCreate, db: Session=Depends(get_db)):
    user=authenticate_user(db, form.email, form.password)
    if user == 1:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Email doesn't exist",
            headers={"WWW-Authenticate": "Bearer"}
        )
    elif user == 2:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    access_token_expires=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token=create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer", "session_expires": ACCESS_TOKEN_EXPIRE_MINUTES}


async def get_current_user(token: str=Depends(oauth2_scheme), db: Session=Depends(get_db)):
    credentials_exception=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload=jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str=payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data=schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user=crud.get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user

@app.get("/users/me", response_model=schemas.User, tags=["authentication"])
async def read_users_me(current_user: schemas.User=Depends(get_current_user)):
    return current_user

# ==== USER ====

# Create user
@app.post("/users", response_model=schemas.User, tags=["users"])
def create_user(user: schemas.UserCreate, db: Session=Depends(get_db)):
    # Check if user already exists
    db_user=crud.get_user_by_email(db, email=user.email)
    if db_user is not None:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    return crud.create_user(db=db, user=user)

# ==== BODY PART ====

# Get all body parts
@app.get("/body_parts", response_model=list[schemas.BodyPart], tags=["body_parts"])
def read_body_parts(db: Session=Depends(get_db)):
    body_parts=crud.get_body_parts(db)
    return body_parts

# ==== EPISODE  ====

# Get all episodes of an user.
# This method will only be available to the user himself.
@app.get("/users/me/episodes", response_model=list[schemas.Episode], tags=["episodes"])
async def read_user_episodes(current_user: schemas.User=Depends(get_current_user), skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    episodes=crud.get_episodes_by_user(db, user_id=current_user.id, skip=skip, limit=limit)
    return episodes

# Create episode for a given user
@app.post("/users/me/episodes", response_model=schemas.Episode, tags=["episodes"])
async def create_user_episode(episode: schemas.EpisodeCreate, current_user: schemas.User=Depends(get_current_user), db: Session=Depends(get_db)):
    # Check if body_parts is empty
    if not episode.body_parts:
        raise HTTPException(
            status_code=400,
            detail="Body parts are required"
        )

    return crud.create_episode(db=db, episode=episode, user_id=current_user.id)
    

# Delete one episode for a given user
@app.delete("/users/me/episodes/{episode_id}", tags=["episodes"])
async def delete_user_episode(episode_id: int, current_user: schemas.User=Depends(get_current_user), db: Session=Depends(get_db)):
    # Get episode
    episode=crud.get_episode_by_id(db, episode_id=episode_id)
    # Check if episode exists
    if episode is None:
        raise HTTPException(
            status_code=404,
            detail="Episode not found"
        )
    # Check if user is the owner of the episode
    if episode.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You are not the owner of this episode"
        )
    # Delete episode
    return crud.delete_episode(db=db, episode_id=episode_id)
    
# Update episode
@app.put("/users/me/episodes/{episode_id}", response_model=schemas.Episode, tags=["episodes"])
async def update_user_episode(episode_id: int, episode: schemas.EpisodeCreate, current_user: schemas.User=Depends(get_current_user), db: Session=Depends(get_db)):
    # Get episode
    db_episode=crud.get_episode_by_id(db, episode_id=episode_id)
    # Check if episode exists
    if db_episode is None:
        raise HTTPException(
            status_code=404,
            detail="Episode not found"
        )
    # Check if user is the owner of the episode
    if db_episode.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You are not the owner of this episode"
        )
    # Update episode
    return crud.update_episode(db=db, episode_id=episode_id, episode=episode)


# ==== INSERT BODY PARTS ====

import xml.etree.ElementTree as ET

# Read body_parts.xml
def read_body_parts_xml(file_path: str):
    with open(file_path, "r") as f:
        tree = ET.parse(f)
        root = tree.getroot()
        body_parts=[]
        for child in root:
            body_parts.append(
                schemas.BodyPart(
                    name=child.attrib["name"],
                )
            )
        return body_parts

print("Reading body parts")
body_parts=read_body_parts_xml("src/body_parts.xml")
print(body_parts)

print("Inserting body parts")
for body_part in body_parts:
    # Check it doesn't exist
    db_body_part=crud.get_body_part_by_name(next(get_db()), name=body_part.name)
    if db_body_part is None:
        crud.create_body_part(db=next(get_db()), body_part=body_part)