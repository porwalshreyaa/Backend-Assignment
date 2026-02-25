from fastapi import FastAPI
from app.db.session import engine, Base
from app.apis.auth.router import router as auth
from app.apis.bookings.router import router as bookings
from app.apis.fitness_class.router import router as fitness_class
from app.core.logging_config import setup_logging
import logging

setup_logging()


app = FastAPI(title="Fitness Booking API")

logger = logging.getLogger(__name__)

app.include_router(auth)
app.include_router(bookings)
app.include_router(fitness_class)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        logger.info("Application Startup!")

