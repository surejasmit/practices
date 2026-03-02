# Step-by-Step Workflow for Hackathon

## Initial Setup (Do Once)
```bash
# Clone the hackathon repo
git clone <repo-url>
cd <repo-name>

# Create your branch
git checkout -b your-name/issue-123
```

## Daily Workflow (Do This Every Time Before Pushing)

### Step 1: Save your work
```bash
git add .
git commit -m "feat: add login feature"
```

### Step 2: Update from main (IMPORTANT!)
```bash
# Fetch latest changes
git fetch origin

# Merge main into your branch
git merge origin/main
```

### Step 3: Handle Conflicts (if they appear)
```bash
# Git will show conflict files
# Open each file and look for:
<<<<<<< HEAD
your changes
=======
their changes
>>>>>>> origin/main

# Edit the file to keep what you need
# Remove the conflict markers (<<<, ===, >>>)

# After fixing all conflicts:
git add .
git commit -m "fix: resolve merge conflicts"
```

### Step 4: Push your work
```bash
git push origin your-name/issue-123
```

## If Authorities Say "Merge Conflict"

This means main branch has new changes. Do this:

```bash
# 1. Fetch latest main
git fetch origin

# 2. Merge main into your branch
git merge origin/main

# 3. Fix conflicts in your editor
# 4. Add and commit
git add .
git commit -m "fix: resolve conflicts with main"

# 5. Push again
git push origin your-name/issue-123
```

## Pro Tips

✅ **DO THIS:**
- Pull/merge from main BEFORE starting work each day
- Commit small changes frequently
- Test your code after resolving conflicts
- Ask authorities which files are being modified by others

❌ **DON'T DO THIS:**
- Don't work for days without syncing with main
- Don't modify files other students are working on
- Don't force push (unless you know what you're doing)
- Don't panic when you see conflicts - they're normal!
