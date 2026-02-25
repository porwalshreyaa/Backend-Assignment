from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base


class Booking(Base):
    __tablename__ = "bookings"

    _id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users._id"))
    class_id = Column(Integer, ForeignKey("fitness_classes._id"))

    user = relationship("User", back_populates="bookings")
    fitness_class = relationship("FitnessClass", back_populates="bookings")