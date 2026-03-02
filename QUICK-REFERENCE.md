# Quick Reference - Avoid Merge Conflicts
# 🚀 GDG Sprintathon Edition

## ⚠️ The Golden Rule
**ALWAYS sync with main BEFORE and AFTER working on your issue!**

## 🎯 Quick Commands for GDG Sprintathon

### ✅ STEP 1: Before You Start Any Issue
```bash
# Always start fresh from main!
git checkout main
git pull origin main

# Now create your issue branch
git checkout -b issue-123
```

### ✅ STEP 2: While Working (Every Hour)
```bash
# Check if main has new changes
git fetch origin
git merge origin/main
# Note: Use slash (/) not space!
```

### ✅ STEP 3: Before You Push (CRITICAL!)
```bash
# Sync with main one more time
git fetch origin
git merge origin/main
# IMPORTANT: origin/main with slash (/)

# If conflicts appear, fix them NOW
# Then push
git push origin issue-123
```

### 🔥 If Manager Says "MERGE CONFLICT!"
```bash
# 1. Fetch latest main
git fetch origin

# 2. Merge main into your branch
git merge origin/main

# 3. Open conflicted files in VS Code
# 4. Look for these markers:
#    <<<<<<< HEAD (your changes)
#    ======= (separator)
#    >>>>>>> origin/main (their changes from main)

# 5. Keep BOTH changes (yours + theirs)
# 6. Remove the <<<<<<, =======, >>>>>>> markers
# 7. Save file

# 8. Add and commit
git add .
git commit -m "fix: resolve merge conflicts with main"

# 9. Push again
git push origin issue-123

# 10. Tell manager: "Conflicts resolved!"
```

## 📊 Merge vs Rebase

| Command | When to Use | Result |
|---------|-------------|--------|
| `git merge` | ✅ GDG Sprintathon, Hackathons | Safe, preserves history |
| `git rebase` | ❌ NOT for team events | Dangerous, rewrites history |

## 🎓 For GDG Sprintathon: USE MERGE ONLY!

**Why?**
- Rebase requires force push
- Force push can delete others' work
- Merge is safer for team collaboration
- Managers prefer merge commits

## 💡 Pro Tips

1. **Sync 3 times:**
   - Before starting issue
   - Every hour while working
   - Before pushing

2. **Small commits:**
   - Commit every feature
   - Don't wait till end

3. **Ask team:**
   - "Who's working on file X?"
   - Avoid same files

4. **Test after merge:**
   - Run your code
   - Make sure it still works

## 🆘 Emergency Commands

```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# See what changed
git status
git diff

# Abort merge if stuck
git merge --abort

# Get help
git --help
```

## ✨ Remember

**The #1 mistake in GDG Sprintathon:**
Not syncing with main before pushing!

**The #1 solution:**
```bash
git fetch origin && git merge origin/main
```

Run this before EVERY push! 🎯
