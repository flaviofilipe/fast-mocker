# Use the official Python image with version 3.11
FROM python:3.11-slim

# Install Poetry via pip
RUN pip install poetry==1.2.2

# Set working directory
WORKDIR /app

# Copy Dependencies
COPY poetry.lock pyproject.toml ./

# [OPTIONAL] Validate the project is properly configured
RUN poetry check

# Install Dependencies
RUN poetry install --no-root --no-interaction --no-cache --without dev

# Copy Application
COPY . /app

# Run Application
EXPOSE 8000

# Run the FastAPI project using the "task run" command
CMD [ "poetry", "run", "task", "run", "--host=0.0.0.0" ]
