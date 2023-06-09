# syntax=docker/dockerfile:1

FROM python:3.10.6

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy code files to the image
COPY . .

# Set entry point script as executable
RUN chmod +x entrypoint.sh

# Define entry point script
ENTRYPOINT ["./entrypoint.sh"]