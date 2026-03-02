# Practical Demo: Main Branch → Person1 Branch

## Step 1: Push Project to Main Branch

```bash
cd git-demo
git add .
git commit -m "initial: hackathon project setup"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

## Step 2: Create Person1 Branch and Pull Code

```bash
# Create and switch to person1 branch
git checkout -b person1

# Pull code from main (already have it, but this is the command)
git pull origin main

# Now you have all code from main in person1 branch
```

## Step 3: Make Changes in Person1 Branch

```bash
# Edit files (hackathon-app.py, add features, etc.)
# After editing:

git add .
git commit -m "feat: person1 adds login feature"
```

## Step 4: Push Person1 Branch

```bash
git push -u origin person1
```

## Complete Command Sequence

```bash
# === ON MAIN BRANCH ===
git add .
git commit -m "initial: project setup"
git push origin main

# === CREATE PERSON1 BRANCH ===
git checkout -b person1
# Make your changes to files
git add .
git commit -m "feat: person1 changes"
git push -u origin person1
```

## If Someone Else Pushes to Main Later

```bash
# You're on person1 branch
git fetch origin
git merge origin/main
# Fix conflicts if any
git push origin person1
```

That's it! ✅
