#!/bin/bash

# Setup script for the similarity evaluation project

echo "Setting up Text Similarity Evaluation Project..."

# Create directory structure
mkdir -p models evaluation dataset reports notebooks templates scripts

# Copy model files to models directory
echo "Setting up model files..."
cp tfidf_cosine.py models/
cp okapi_bm25.py models/
cp bertscore.py models/
cp sbert.py models/
cp jaccard.py models/

# Copy evaluation files
echo "Setting up evaluation files..."
cp analyzer.py evaluation/
cp metrics.py evaluation/

# Copy dataset
echo "Setting up dataset..."
cp philippine-legal-dataset.json dataset/

# Create __init__.py files
touch models/__init__.py
touch evaluation/__init__.py

echo "Setup complete!"
echo ""
echo "To run the project:"
echo "1. Build Docker image: docker-compose build"
echo "2. Run services: docker-compose up"
echo "3. Access Jupyter Lab: http://localhost:8888"
echo "4. Access Web Interface: http://localhost:5000"