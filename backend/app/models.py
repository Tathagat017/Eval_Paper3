from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String,Integer,Boolean,DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy.orm import relationship



class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"
    id:Mapped[int]= mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(30))
    email:Mapped[str]= mapped_column(String(10))
    age:Mapped[int]= mapped_column(Integer(12))
    height:Mapped[int]= mapped_column(Integer(10))
    fitness_goals:Mapped[List[str]] = mapped_column(List(String))
    medical_condition:Mapped[List[str]] = mapped_column(List(String))
    activity_level:Mapped[int]=mapped_column(Integer(5))
    
class WorkoutPlans(Base):
    id:Mapped[int]= mapped_column(primary_key=True)
    plan_name:Mapped[str]= mapped_column(String(100))
    difficulty_level:Mapped[int] = mapped_column(Integer(5))
    duration:Mapped[int] = mapped_column(Integer(10))
    target_muscle_group:Mapped[str] = mapped_column(String(20))
    excercise_list:Mapped[List(str)] = mapped_column(List(String))
    
class Excercise(Base):
    id:Mapped(int) = mapped_column(primary_key=True)
    excercise_name:Mapped(str) = mapped_column(String(20))
    category:Mapped(str) = mapped_column(String(30))
    equipment_needed: Mapped(bool) = mapped_column(Boolean)
    difficulty:Mapped[int] = mapped_column(Integer(10))
    instructions:Mapped[List(str)] = mapped_column(List(String))

class ProgressTracking(Base):
    user_id:Mapped[int] = mapped_column(Integer(10))
    workout_id:Mapped[int] = mapped_column(Integer(10))
    date:Mapped[DateTime]  = mapped_column(DateTime)
    excercise_comleted:Mapped[bool] = mapped_column(Boolean)
    sets:Mapped[int] = mapped_column(Integer(50))
    reps:Mapped[int] = mapped_column(Integer(50))
    weights:Mapped[int]= mapped_column(Integer(50))
    calories_burned:Mapped[int] = mapped_column(Integer(1000))

#Fields: user_id, date, meals, calories, macronutrients (protein, carbs, fats)
class NutritionLogs(Base):
    user_id:Mapped[int] = mapped_column(Integer(100))
    date:Mapped[DateTime] = mapped_column(DateTime)
    meals:Mapped[List[str]] = mapped_column(List(String))
    calories:Mapped[int] = mapped_column(Integer(1000))
