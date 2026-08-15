#!/bin/bash
# Build script for macOS standalone application
# Usage: ./build-macos.sh

set -euo pipefail

echo "========================================"
echo "Building RegisterWiFiMAC for macOS"
echo "========================================"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

echo ""
echo "Step 1: Checking Python version..."
python3 --version

echo ""
echo "Step 2: Installing dependencies..."
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -r requirements.txt
python3 -m pip install pyinstaller

echo ""
echo "Step 3: Building standalone application..."
python3 -m PyInstaller RegisterWiFiMAC-macos.spec

echo ""
echo "Step 4: Cleanup..."
rm -rf build __pycache__ .eggs *.egg-info 2>/dev/null || true

echo ""
echo "========================================"
echo "Build completed successfully!"
echo "Application location: dist/RegisterWiFiMAC.app"
echo "========================================"

# Make the app executable
chmod +x "dist/RegisterWiFiMAC.app/Contents/MacOS/RegisterWiFiMAC"

echo "Application is ready to run!"
