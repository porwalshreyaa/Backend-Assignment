# Fitness Booking API

A **FastAPI backend** for managing fitness classes, user registration, and bookings.


## Features

- User registration and login with JWT authentication
- Admin can create fitness classes
- Users can view and book available classes
- Async database operations with SQLAlchemy
- Automated tests using `pytest` and `pytest-asyncio`


## Tech Stack

- **Backend:** FastAPI  
- **Database:** MySQL (async) / SQLite for tests  
- **ORM:** SQLAlchemy (async)  
- **Auth:** JWT (JSON Web Tokens)  
- **Testing:** pytest + httpx  
- **Environment:** `.env` + Pydantic Settings  


## Prerequisites

- Python 3.12+  
- MySQL server (or Docker for local dev)  
- Poetry for dependency management  
- Node.js & pnpm if you want to run npm scripts  


## Setup

1. **Clone the repo**

```bash
git clone https://github.com/porwalshreyaa/Backend-Assignment
cd BACKEND-ASSIGNMENT
```

2. **Install pnpm and poetry**

```
pnpm install
```

Also might need to `cd` into `package/server` and do
```
poetry install
```

3. **Create a .env in 'server' directory**

```
# .env
SECRET_KEY=supersecret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

DB_USER=fitness_user
DB_PASSWORD=yourpassword
DB_NAME=fitness_db
DB_HOST=localhost
DB_PORT=3306
```
MySQL DB in main and SQLite DB in Test

4. You'd need to create a mysql db and give permission to the user, and add the credentials in .env

I have added .env.example for reference

5. **Run the app**

```
pnpm dev
```

6. **Test the app**

```
pnpm test
```