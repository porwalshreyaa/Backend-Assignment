from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.db.session import Base


class FitnessClass(Base):
    __tablename__ = "fitness_classes"

    _id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    instructor = Column(String(100), nullable=False)
    start_time = Column(DateTime, nullable=False)
    available_slots = Column(Integer, nullable=False)
    
    bookings = relationship("Booking", back_populates="fitness_class")