from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.recommendation import router
from routes.assignment import router as assignment_router

app = FastAPI(
    title="Driver Recommendation Agent"
)

# -----------------------------
# CORS Configuration
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    # Allow all origins (good for development/demo)
    allow_origins=["*"],

    # Set to False when using "*"
    allow_credentials=False,

    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Register Routes
# -----------------------------
app.include_router(router)
app.include_router(assignment_router)

# -----------------------------
# Home Endpoint
# -----------------------------
@app.get("/")
def home():
    return {
        "message": "Driver Recommendation Agent Running"
    }