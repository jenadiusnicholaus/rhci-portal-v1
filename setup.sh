#!/bin/bash

# RHCI Portal Setup Script
# This script automates the setup process for the Django project

set -e  # Exit on error

echo "🚀 Starting RHCI Portal setup..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python 3 is installed"
PYTHON_VERSION=$(python3 --version)
echo "   Version: $PYTHON_VERSION"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip > /dev/null 2>&1
echo "✅ pip upgraded"
echo ""

# Install requirements
echo "📚 Installing dependencies from requirements.txt..."
pip install -r requirements.txt
echo "✅ Dependencies installed"
echo ""

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚙️  Creating .env file from .env.example..."
    cp .env.example .env
    echo "✅ .env file created"
    echo "⚠️  Please update .env file with your configuration!"
else
    echo "✅ .env file already exists"
fi
echo ""

# Run migrations
echo "🗄️  Running database migrations..."
python manage.py migrate
echo "✅ Migrations completed"
echo ""

# Ask if user wants to create superuser
echo "👤 Do you want to create a superuser? (y/n)"
read -r CREATE_SUPERUSER

if [ "$CREATE_SUPERUSER" = "y" ] || [ "$CREATE_SUPERUSER" = "Y" ]; then
    python manage.py createsuperuser
fi
echo ""

# Create media and static directories
echo "📁 Creating media and static directories..."
mkdir -p media staticfiles
echo "✅ Directories created"
echo ""

echo "✨ Setup completed successfully!"
echo ""
echo "🎯 Next steps:"
echo "   1. Update .env file with your configuration"
echo "   2. Run 'source venv/bin/activate' to activate the virtual environment"
echo "   3. Run 'python manage.py runserver' to start the development server"
echo ""
echo "🌐 The application will be available at http://127.0.0.1:8000/"
echo "🔐 Admin panel at http://127.0.0.1:8000/admin/"
echo ""
