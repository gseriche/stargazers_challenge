# Use an official Python runtime as a parent image
FROM python:3.12-alpine3.20

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set Python to run in unbuffered mode
ENV PYTHONUNBUFFERED=1

# Run the unit tests
RUN python -m unittest test_main.py

# Run app.py when the container launches
CMD ["python", "main.py"]