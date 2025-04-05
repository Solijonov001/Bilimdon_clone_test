from sqlalchemy import String,Integer,Boolean, Date, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import Optional

from datetime import datetime,timezone

from app.database import Base

from time import time


class User(Base):
    __tablename__ = "users"


    id : Mapped[int] = mapped_column(primary_key=True)
    email : Mapped[str] = mapped_column(unique=True)
    hashed_password : Mapped[str] = mapped_column(String(1238))
    username : Mapped[str] = mapped_column(String(32))
    first_name : Mapped[str] = mapped_column(String(32))
    last_name : Mapped[str] = mapped_column(String(32))
    birthday : Mapped[datetime] = mapped_column(Date)
    joinned_at : Mapped[bool] = mapped_column(DateTime,default=datetime.now(timezone.utc))
    is_activate : Mapped[bool] = mapped_column(default=True)
    is_staff : Mapped[bool] = mapped_column(default=False)
    is_superuser : Mapped[bool] = mapped_column(default=False)


class Participation(Base):
    __tablename__="paricipations"

    id : Mapped[int] = mapped_column(primary_key=True)

    user_id : Mapped[int] = mapped_column(ForeignKey("user_id"),type_=Integer,nullable=True)

    user : Mapped[Optional["User"]] = relationship("User")



    game_id : Mapped[int] = mapped_column()
    start_time : Mapped[time.time]
    end_time : Mapped[time.time] = mapped_column(nullable=True)
    gained_score : Mapped[int] = mapped_column(default=0)
    registered_at : Mapped[datetime]


class Game(Base):
    __tablename__="game"

    id : Mapped[int] = mapped_column(primary_key=True)

    ower_id : Mapped[int] = mapped_column(ForeignKey("user_id"),type_=Integer,nullable=True)

    ower: Mapped[Optional["User"]] = relationship("User")
    topic_id : Mapped[int] = mapped_column()


