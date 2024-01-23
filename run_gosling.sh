#!/bin/bash

# Load environment variables from .env file
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

# Build the Docker image
docker build -t gosling_app .

# Run the Docker container
docker run -d -e ID -e HASH gosling_app
