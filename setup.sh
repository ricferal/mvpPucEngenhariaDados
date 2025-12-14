#!/bin/bash

echo "=========================================="
echo "MVP Engenharia de Dados - Setup"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.11 or higher."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✓ Dependencies installed successfully"
echo ""

# Create necessary directories
echo "Creating directory structure..."
mkdir -p data/raw data/processed logs config

echo "✓ Directory structure created"
echo ""

# Generate sample data
echo "Generating sample data..."
python src/generate_sample_data.py

echo ""
echo "=========================================="
echo "Setup completed successfully!"
echo "=========================================="
echo ""
echo "To activate the virtual environment:"
echo "  source venv/bin/activate"
echo ""
echo "To run the pipeline:"
echo "  python src/pipeline.py"
echo ""
echo "To run examples:"
echo "  python example.py"
echo ""
echo "To deactivate the virtual environment:"
echo "  deactivate"
echo ""
