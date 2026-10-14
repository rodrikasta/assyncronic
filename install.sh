#!/bin/bash

echo "Installing Assyncronic (⁠◕⁠‿⁠◕⁠)..."

chmod +x main.py

mkdir -p ~/.local/bin

ln -sf "$(pwd)/main.py" ~/.local/bin/assyncronic

echo "Installation complete! You can now open a new terminal and simply type 'assyncronic' :D."