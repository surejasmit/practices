# Visual Changes Guide

## Run the Demo

```bash
cd git-demo
python hackathon-app.py           # Original
python hackathon-app-person1.py   # Person1's changes
python hackathon-app-person2.py   # Person2's changes
python hackathon-app-resolved.py  # Resolved version
```

Or run all at once:
```bash
run-demo.bat
```

## What Changed?

### 📄 Original (hackathon-app.py)
```
Welcome to Hackathon Project!
Version: 1.0
========================================
   HACKATHON PROJECT MENU
========================================
Sample Score: 50 points
```

### 🔐 Person1 Added (hackathon-app-person1.py)
```
🔐 LOGIN FEATURE (by Person1)
Username: person1
Password: *******
✅ Login successful!
```

### 🚪 Person2 Added (hackathon-app-person2.py)
```
🚪 LOGOUT FEATURE (by Person2)
User: person2
✅ Logged out successfully!
Session ended.
```

### ✅ Resolved Version (hackathon-app-resolved.py)
```
Version: 2.0 - CONFLICT RESOLVED
Features: Login (Person1) + Logout (Person2)

🔐 LOGIN FEATURE (by Person1)
... menu ...
🚪 LOGOUT FEATURE (by Person2)
```

## The Conflict

Both Person1 and Person2 modified:
- ✏️ The `main()` function
- ✏️ Added their own functions
- ✏️ Changed version number
- ✏️ Modified same lines of code

Result: **MERGE CONFLICT!** ⚠️

## How to See Changes

1. Open `hackathon-app-person1.py` - See 🔐 login
2. Open `hackathon-app-person2.py` - See 🚪 logout
3. Open `hackathon-app-resolved.py` - See BOTH!

The resolved version keeps BOTH features working together!
