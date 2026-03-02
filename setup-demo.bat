@echo off
echo === Git Demo Setup ===
echo.

echo Step 1: Initialize Git Repository
git init
git config user.name "Demo User"
git config user.email "demo@example.com"
echo.

echo Step 2: Add files and commit to main
git add .
git commit -m "initial: hackathon project setup"
echo.

echo Step 3: Create person1 branch
git checkout -b person1
echo.

echo === Setup Complete! ===
echo.
echo Current branch: person1
echo.
echo Next steps:
echo 1. Edit hackathon-app.py (add your features)
echo 2. Run: git add .
echo 3. Run: git commit -m "feat: person1 adds feature"
echo 4. Run: git push origin person1
echo.
pause
