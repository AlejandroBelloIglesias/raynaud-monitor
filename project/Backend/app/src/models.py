from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from .database import Base, engine

    

# ==== USER ====

class User(Base):

    __tablename__ = "users"

    # Columns
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # Relationships
    episodes = relationship("Episode", back_populates="user")



# ==== EPISODE ====

 
class Episode(Base):

    __tablename__ = "episodes"
    
    # Columns
    id = Column(Integer, primary_key=True, index=True)
    date_time = Column(Integer, index=True) # Unix timestamp
    duration = Column(Integer)
    deliberated = Column(Boolean)
    stress_level = Column(Integer) # Stress level (1-5)
    temperature = Column(Integer)
    daily_cigarette_smoked = Column(Integer)

    # Relationships
    # Multiple body parts can be associated with multiple episodes
    body_parts = relationship("BodyPart", secondary="link")
    
    # One user can have multiple episodes
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship(User, back_populates="episodes")


# ==== BODYPART ====

class BodyPart(Base):

    __tablename__ = "body_parts"

    # Columns
    name = Column(String, primary_key=True, index=True) 

    # Relationships
    # Multiple body parts can be associated with multiple episodes
    episodes = relationship("Episode", secondary="link")


# ==== LINK ====

class Link(Base):
    __tablename__ = "link"

    # Columns
    episode_id = Column(Integer, ForeignKey("episodes.id"), primary_key=True)
    body_part_name = Column(String, ForeignKey("body_parts.name"), primary_key=True)

# ==== DATABASE INITIALIZATION ====

Base.metadata.create_all(bind=engine)