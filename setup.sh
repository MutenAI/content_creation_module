#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Setting up the Python environment
echo "Setting up the Python environment..."

# Create and activate the virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

echo "Python environment setup complete."

# Setting up the Node.js environment
echo "Setting up the Node.js environment..."

# Navigate to the content-ui directory
cd content-ui

# Install Node.js dependencies
npm install

# Create the app directory if it doesn't exist
mkdir -p app

# Install missing modules if needed
npm install autoprefixer

echo "Node.js environment setup complete."

echo "Setup complete. You can now run the development server with 'npm run dev' in the content-ui directory." 