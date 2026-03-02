# Wrong vs Right Workflow

## ❌ WRONG (What You Did)

```
Day 1:
  main branch ──────────────────────────────────→
                 ↓
           your branch (issue-123)
                 ↓
           work work work
                 ↓
           (3 days later)
                 ↓
           git push ❌ CONFLICT!
           
Problem: Main moved forward, you didn't sync!
```

## ✅ RIGHT (What You Should Do)

```
Day 1:
  main branch ──────────────────────────────────→
       ↓ (pull latest)
  your branch (issue-123)
       ↓
  work work work
       ↓
  (Before push)
       ↓
  git fetch origin
  git merge origin/main ← SYNC HERE!
       ↓
  git push ✅ SUCCESS!
```

## Real Example

### Wrong Approach:
```bash
# Monday 9 AM
git clone repo
git checkout -b issue-123
# code for 2 days

# Wednesday 5 PM
git push origin issue-123
# Manager: "Conflict in app.py" ❌
```

### Right Approach:
```bash
# Monday 9 AM
git clone repo
git checkout main
git pull origin main          # ← Sync first!
git checkout -b issue-123
# code for 2 days

# Wednesday 5 PM
git fetch origin
git merge origin/main         # ← Sync before push!
# Fix any conflicts now
git push origin issue-123
# Manager: "Looks good!" ✅
```

## The One Command That Saves You

Before EVERY push, run this:

```bash
git fetch origin && git merge origin/main
```

If conflicts appear:
1. Open the file
2. Find <<<<<<< markers
3. Keep both changes
4. Remove markers
5. Save file
6. `git add .`
7. `git commit -m "fix: resolve conflicts"`
8. `git push`

## Remember

**Sync early, sync often!**
- Before starting work: `git pull origin main`
- Before pushing: `git merge origin/main`
- During long work: Check main every hour
