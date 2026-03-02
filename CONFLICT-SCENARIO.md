# Conflict Scenario: Person1 vs Person2

## The Setup

**Main Branch** has:
```python
def main():
    print("Welcome to Hackathon Project!")
    print("Version: 1.0")
```

**Person1** changes hackathon-app.py to:
```python
def login(username):
    print(f"User {username} logged in!")

def main():
    print("Welcome to Hackathon Project!")
    print("Version: 1.0")
    login("person1")
    print("Person1's feature added!")
```

**Person2** changes the SAME hackathon-app.py to:
```python
def logout(username):
    print(f"User {username} logged out!")

def main():
    print("Welcome to Hackathon Project!")
    print("Version: 1.0")
    logout("person2")
    print("Person2's feature added!")
```

## What Happens?

### Timeline:
1. ✅ Person1 pushes to person1 branch - SUCCESS
2. ✅ Authority merges person1 → main - SUCCESS
3. ❌ Person2 tries to push to person2 branch - CONFLICT!

### Why Conflict?

Both modified the SAME lines in hackathon-app.py:
- Person1 added `login()` function
- Person2 added `logout()` function
- Both modified the `main()` function

## Commands to Reproduce

```bash
# === PERSON1 ===
git checkout -b person1
# Copy content from hackathon-app-person1.py to hackathon-app.py
git add hackathon-app.py
git commit -m "feat: person1 adds login"
git push origin person1

# === AUTHORITY MERGES ===
git checkout main
git merge person1
git push origin main

# === PERSON2 (starts from old main) ===
git checkout -b person2 <old-main-commit>
# Copy content from hackathon-app-person2.py to hackathon-app.py
git add hackathon-app.py
git commit -m "feat: person2 adds logout"

# Now person2 needs to sync with main
git fetch origin
git merge origin/main
# ⚠️ CONFLICT! Both changed hackathon-app.py
```

## How Person2 Resolves Conflict

```bash
# Open hackathon-app.py, you'll see:
def logout(username):
    print(f"User {username} logged out!")
    
def main():
    print("Welcome to Hackathon Project!")
    print("Version: 1.0")
    logout("person2")
    print("Person2's feature added!")

# Fix it by keeping BOTH features:
def login(username):
    print(f"User {username} logged in!")

def logout(username):
    print(f"User {username} logged out!")
    
def main():
    print("Welcome to Hackathon Project!")
    print("Version: 1.0")
    login("person1")
    print("Person1's feature added!")
    logout("person2")
    print("Person2's feature added!")

# Then:
git add hackathon-app.py
git commit -m "fix: resolve conflict, keep both features"
git push origin person2
```

## The Lesson

✅ **To avoid this:** Person2 should have synced with main BEFORE making changes!

```bash
git checkout -b person2
git pull origin main  # Get person1's changes first
# Now make your changes
# Less likely to conflict!
```
