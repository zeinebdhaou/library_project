# Use a specific Python version to ensure compatibility
FROM python:3.10-slim

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy requirements file
COPY requirements.txt /usr/src/app/

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . /usr/src/app

# Expose the port that the app runs on
EXPOSE 8080

# Set the entry point and command
ENTRYPOINT ["python"]
CMD ["-m", "swagger_server"]
