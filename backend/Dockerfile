# Use an official Python runtime as a base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy only the required files (avoid unnecessary files)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on (e.g., 5000 for Flask, 8000 for FastAPI/Django)
EXPOSE 8000

# Define the command to run your application
# Start FastAPI with Uvicorn
CMD ["ENV=development","uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]            