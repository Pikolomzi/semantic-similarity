# Use the official Python image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Command to run the Python script
CMD ["python", "semantic.py"]
