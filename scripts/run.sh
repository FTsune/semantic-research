#!/bin/bash

# Run script for the similarity evaluation project

echo "Starting Text Similarity Evaluation..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "Docker is not running. Please start Docker first."
    exit 1
fi

# Build and run with Docker Compose
echo "Building Docker images..."
docker-compose build

echo "Starting services..."
docker-compose up -d

echo ""
echo "Services started successfully!"
echo ""
echo "Access points:"
echo "- Jupyter Lab: http://localhost:8888"
echo "- Streamlit App: http://localhost:8501"
echo ""
echo "To stop services: docker-compose down"
echo "To view logs: docker-compose logs -f"