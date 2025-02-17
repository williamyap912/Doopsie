from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.router import router_task, router_filtering
from app.database.database import engine, Base
from app.utilities.services.logger import logger

app = FastAPI()

# Register CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes properly
app.include_router(router_task.router, prefix="/api", tags=["Tasks"])
logger.info("✅ Router_task successfully registered")
app.include_router(router_filtering.router, prefix="/api", tags=["Filtering"])
logger.info("✅ Router_filtering successfully registered")

# Create the database tables
try:
    Base.metadata.create_all(bind=engine)
    logger.info("✅ Database tables created successfully")
except Exception as e:
    logger.error(f"Error creating database tables: {e}")
    raise

for route in app.routes:
    logger.info(f"Route Path: {route.path} | Methods: {route.methods}")

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Unhandled exception: {exc}")
    return HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)