# Quick Reference - Avoid Merge Conflicts

## The Golden Rule
**ALWAYS sync with main BEFORE pushing your code!**

## Quick Commands

### Before You Start Working
```bash
git checkout your-branch
git pull origin main
```

### Before You Push
```bash
git fetch origin
git merge origin/main
# Fix conflicts if any
git push origin your-branch
```

### If You Get Conflict Error
```bash
# 1. Open conflicted files in your editor
# 2. Look for these markers:
#    <<<<<<< HEAD (your changes)
#    ======= (separator)
#    >>>>>>> origin/main (their changes)
# 3. Keep what you need, delete markers
# 4. Save file
# 5. Run:
git add .
git commit -m "fix: resolve conflicts"
git push origin your-branch
```

## Merge vs Rebase

| Command | When to Use | Result |
|---------|-------------|--------|
| `git merge` | Hackathons, team work | Preserves all history, creates merge commit |
| `git rebase` | Personal projects, clean history | Rewrites history, linear commits |

## For Your Hackathon: USE MERGE!

Rebase requires force push which can cause problems in team settings.
