# Git Merge vs Rebase - Hackathon Scenario

## Understanding the Hackathon Workflow

In your hackathon:
- **main branch** = where authorities merge everyone's work
- **your branch** = where you work on your issue
- **other branches** = other students working on different problems

## The Problem: Merge Conflicts

Merge conflicts happen when:
1. You and others modify the same file
2. Your branch is behind the main branch
3. Git can't automatically combine the changes

## Solution: Keep Your Branch Updated

### Method 1: MERGE (Safer for beginners)
```bash
git checkout your-branch
git fetch origin
git merge origin/main
# Resolve conflicts if any
git add .
git commit -m "Merge main into my branch"
git push origin your-branch
```

### Method 2: REBASE (Cleaner history)
```bash
git checkout your-branch
git fetch origin
git rebase origin/main
# Resolve conflicts if any
git add .
git rebase --continue
git push origin your-branch --force
```

## When to Use What?

- **MERGE**: Use in hackathons (safer, preserves history)
- **REBASE**: Use for clean history (but requires force push)

## Best Practices to Avoid Conflicts

1. **Pull frequently**: Update your branch daily
2. **Small commits**: Commit often with clear messages
3. **Communicate**: Tell team which files you're editing
4. **Before pushing**: Always sync with main first
