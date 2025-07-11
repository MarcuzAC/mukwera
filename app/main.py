from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth,rides, users

app = FastAPI(title="Mukwera API", version="1.0")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(rides.router, prefix="/rides", tags=["Rides"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Mukwera API"}