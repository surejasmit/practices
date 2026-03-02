@echo off
echo ========================================
echo   GIT MERGE CONFLICT DEMO
echo ========================================
echo.

echo [1] ORIGINAL CODE (Main Branch)
echo ========================================
python hackathon-app.py
echo.
echo.

echo [2] PERSON1's CODE (Login Feature)
echo ========================================
python hackathon-app-person1.py
echo.
echo.

echo [3] PERSON2's CODE (Logout Feature)
echo ========================================
python hackathon-app-person2.py
echo.
echo.

echo [4] RESOLVED CODE (Both Features)
echo ========================================
python hackathon-app-resolved.py
echo.
echo.

echo ========================================
echo   NOTICE THE DIFFERENCES!
echo ========================================
echo - Original: Basic menu only
echo - Person1: Added LOGIN feature
echo - Person2: Added LOGOUT feature
echo - Resolved: BOTH features working!
echo.
pause
