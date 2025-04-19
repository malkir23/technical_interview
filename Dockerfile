FROM python:3.11

# Set the working directory inside the container
WORKDIR /code

# Copy all project files into the container
COPY . /code

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
