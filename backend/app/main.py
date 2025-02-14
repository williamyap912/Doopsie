from fastapi import FastAPI
from app.router import router_task
from app.database.database import engine, Base
try:
    from backend.app.router.router_task import router
    print("✅ Successfully imported router")
except Exception as e:
    print(f"❌ Error importing router: {e}")

app = FastAPI()

# Register routes properly
app.include_router(router_task.router, prefix="/api", tags=["Tasks"])
print("✅ Router successfully registered")

# Create the database tables
Base.metadata.create_all(bind=engine)

for route in app.routes:
    print(f"Route Path: {route.path} | Methods: {route.methods}")

@app.get("/")
def read_root():
    return {"message": "Task Management API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)