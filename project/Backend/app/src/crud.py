from sqlalchemy.orm import Session

# Local imports
from . import models, schemas
from .utils.hashing import get_password_hash

# ==== USERS ====

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ==== BODY PARTS ====

def get_body_parts(db: Session):
    return db.query(models.BodyPart).all()

def get_body_part_by_name(db: Session, name: str):
    return db.query(models.BodyPart).filter(models.BodyPart.name == name).first()

def create_body_part(db: Session, body_part: schemas.BodyPartCreate):
    db_body_part = models.BodyPart(name=body_part.name)
    db.add(db_body_part)
    db.commit()
    db.refresh(db_body_part)
    return db_body_part


# ==== EPISODES ====

def get_episodes_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Episode).filter(models.Episode.user_id == user_id).offset(skip).limit(limit).all()

def create_episode(db: Session, episode: schemas.EpisodeCreate, user_id: int):
    # Adds episode and it's body parts to the database within episode.body_parts
    db_episode = models.Episode(
        date_time=episode.date_time,
        duration=episode.duration,
        deliberated=episode.deliberated,
        stress_level=episode.stress_level,
        daily_cigarette_smoked=episode.daily_cigarette_smoked,
        temperature=episode.temperature,
        user_id=user_id,
        body_parts=[]
    )
    for body_part in episode.body_parts:
        db_body_part = get_body_part_by_name(db, body_part.name)
        db_episode.body_parts.append(db_body_part)

    db.add(db_episode)
    db.commit()
    db.refresh(db_episode)
    return db_episode
    

def get_episode_by_id (db: Session, episode_id: int):
    return db.query(models.Episode).filter(models.Episode.id == episode_id).first()
    
def delete_episode(db: Session, episode_id: int):
    episode = get_episode_by_id(db, episode_id)
    if episode:
        db.delete(episode)
        db.commit()
        return True
    return False

def update_episode(db: Session, episode_id: int, episode: schemas.EpisodeCreate):
    db_episode = get_episode_by_id(db, episode_id)
    if db_episode:
        db_episode.date_time = episode.date_time
        db_episode.duration = episode.duration
        db_episode.deliberated = episode.deliberated
        db_episode.stress_level = episode.stress_level
        db_episode.daily_cigarette_smoked = episode.daily_cigarette_smoked
        db_episode.temperature = episode.temperature
        db_episode.body_parts = []
        for body_part in episode.body_parts:
            db_body_part = get_body_part_by_name(db, body_part.name)
            db_episode.body_parts.append(db_body_part)
        db.commit()
        db.refresh(db_episode)
        return db_episode