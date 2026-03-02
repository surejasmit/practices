#!/bin/bash
# Demo Script: Simulating Hackathon Git Workflow

echo "=== Git Merge vs Rebase Demo ==="
echo ""

# Initialize repo
echo "1. Setting up repository..."
git init
git config user.name "Demo User"
git config user.email "demo@hackathon.com"

# Create initial commit on main
echo "2. Creating main branch with initial code..."
echo "print('Hello Hackathon')" > app.py
git add app.py
git commit -m "initial: setup project"

# Simulate authority adding code to main
echo ""
echo "3. Authority adds feature to main..."
git checkout -b temp-main
echo "print('Hello Hackathon')" > app.py
echo "print('Feature by authority')" >> app.py
git add app.py
git commit -m "feat: authority adds feature"
git checkout main
git merge temp-main
git branch -d temp-main

# Create your branch from old main
echo ""
echo "4. You create your branch (from old main)..."
git checkout -b HEAD~1 your-branch
echo "print('Hello Hackathon')" > app.py
echo "print('Your feature')" >> app.py
git add app.py
git commit -m "feat: your feature"

# Now you have conflict
echo ""
echo "5. Trying to merge main into your branch..."
echo "   This will create a CONFLICT!"
git merge main || echo "CONFLICT DETECTED!"

echo ""
echo "=== This is what happens in your hackathon! ==="
echo "Now you need to resolve conflicts manually."
