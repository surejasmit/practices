# 🚀 Hackathon Roadmap - GDG Sprintathon Success Guide

## 📋 Table of Contents
1. Before the Hackathon
2. Day 1: Setup & First Issue
3. During the Hackathon
4. Avoiding Merge Conflicts
5. Communication Tips
6. Winning Strategy

---

## 🎯 Phase 1: Before the Hackathon (1-2 Weeks Before)

### Technical Skills
```
✅ Git Basics
   - git clone, add, commit, push
   - git branch, checkout, merge
   - git fetch, pull
   - Resolving conflicts

✅ GitHub Workflow
   - Creating branches
   - Pull requests
   - Code reviews
   - Issue tracking

✅ Your Tech Stack
   - Python/JavaScript/Java (whatever they use)
   - Framework basics (React, Django, etc.)
   - Testing basics
   - Documentation
```

### Practice Exercise
```bash
# Do this 5 times before hackathon
1. Clone a repo
2. Create a branch
3. Make changes
4. Commit
5. Fetch & merge main
6. Push
7. Create pull request
```

### Tools to Install
```
✅ Git (latest version)
✅ VS Code or your IDE
✅ GitHub Desktop (optional, for beginners)
✅ Postman (for API testing)
✅ Discord/Slack (for team communication)
```

---

## 🏁 Phase 2: Day 1 - Setup & First Issue

### Hour 1: Setup (9:00 AM - 10:00 AM)
```bash
# 1. Join Discord/Slack channel
# 2. Get repo access from organizers
# 3. Clone the repository

git clone <repo-url>
cd <repo-name>

# 4. Explore the codebase
ls -la
cat README.md

# 5. Run the project locally
npm install  # or pip install -r requirements.txt
npm start    # or python app.py

# 6. Verify it works
```

### Hour 2: Pick Your First Issue (10:00 AM - 11:00 AM)
```
✅ Look for issues tagged:
   - "good first issue"
   - "beginner friendly"
   - "easy"
   - "documentation"

✅ Choose based on:
   - Your skill level
   - Time estimate (start with 1-2 hour tasks)
   - Number of files to change (fewer is better)

✅ Claim the issue:
   - Comment: "I'll work on this"
   - Ask questions if unclear
   - Get assigned by organizer
```

### Hour 3-6: Solve First Issue (11:00 AM - 3:00 PM)
```bash
# 1. Create branch
git checkout main
git pull origin main
git checkout -b issue-123-fix-login-bug

# 2. Work on the issue
# ... code ...

# 3. Test your changes
npm test
# or
python -m pytest

# 4. Commit frequently
git add .
git commit -m "fix: resolve login validation bug"

# 5. Before push - SYNC WITH MAIN!
git fetch origin
git merge origin/main

# 6. Fix conflicts if any
# 7. Push
git push origin issue-123-fix-login-bug

# 8. Create Pull Request on GitHub
# 9. Wait for review
```

---

## ⚡ Phase 3: During the Hackathon (Day 1-3)

### Daily Routine

#### Morning (9:00 AM)
```bash
# 1. Check Discord for updates
# 2. Sync with main
git checkout main
git pull origin main

# 3. Check your PR status
# 4. Pick next issue
```

#### Every 2 Hours
```bash
# Sync with main to avoid conflicts
git fetch origin
git merge origin/main
```

#### Before Lunch & Dinner
```bash
# Commit your work (even if incomplete)
git add .
git commit -m "wip: working on feature X"
git push origin your-branch
```

#### Before Sleep
```bash
# Push everything
git add .
git commit -m "feat: completed feature X"
git fetch origin
git merge origin/main
git push origin your-branch
```

### Issue Selection Strategy

**Day 1:** Easy issues (1-2 hours each)
- Documentation fixes
- UI improvements
- Simple bug fixes
- Add tests

**Day 2:** Medium issues (3-4 hours each)
- New features
- API endpoints
- Database changes
- Integration

**Day 3:** High-impact issues
- Performance optimization
- Security fixes
- Critical bugs
- Final polish

---

## 🛡️ Phase 4: Avoiding Merge Conflicts

### The Golden Workflow
```bash
# EVERY TIME before you start working:
git checkout main
git pull origin main
git checkout your-branch
git merge origin/main

# EVERY TIME before you push:
git fetch origin
git merge origin/main
git push origin your-branch
```

### If Conflict Happens
```bash
# 1. Don't panic!
git fetch origin
git merge origin/main

# 2. Open conflicted files
# Look for:
<<<<<<< HEAD
your code
=======
their code
>>>>>>> origin/main

# 3. Keep BOTH changes (usually)
# 4. Remove markers
# 5. Test the code

# 6. Commit and push
git add .
git commit -m "fix: resolve merge conflicts"
git push origin your-branch
```

### Prevention Tips
```
✅ Sync every 1-2 hours
✅ Ask team: "Who's working on file X?"
✅ Work on different files than others
✅ Small, frequent commits
✅ Push often (don't wait till end of day)
```

---

## 💬 Phase 5: Communication Tips

### In Discord/Slack
```
✅ When starting issue:
   "Working on #123 - Login bug fix"

✅ When stuck (after 30 min):
   "Need help with #123 - Getting error X"

✅ When pushing:
   "Pushed PR for #123 - Ready for review"

✅ When conflict:
   "Got merge conflict in app.py - resolving now"

✅ Ask questions:
   "Which files are being modified by others?"
   "What's the priority order for issues?"
```

### With Organizers
```
✅ Be proactive: Ask for next task
✅ Be honest: "This is taking longer than expected"
✅ Be helpful: Review others' PRs
✅ Be responsive: Reply within 15 minutes
```

### Code Review Comments
```
✅ Be respectful: "Consider using X instead of Y"
✅ Be specific: "Line 45: This could cause null error"
✅ Be helpful: "Great work! Small suggestion: ..."
```

---

## 🏆 Phase 6: Winning Strategy

### Points System (Usually)
```
Easy Issue:     10-20 points
Medium Issue:   30-50 points
Hard Issue:     60-100 points
Code Review:    5-10 points
Helping Others: 5-10 points
```

### Maximize Points
```
Day 1: Complete 5-6 easy issues    = 60-120 points
Day 2: Complete 3-4 medium issues  = 90-200 points
Day 3: Complete 1-2 hard issues    = 60-200 points
       + Review 10 PRs             = 50-100 points
       + Help 5 people             = 25-50 points
       ----------------------------------------
       TOTAL:                      = 285-670 points
```

### Quality Over Quantity
```
✅ Write clean code
✅ Add comments
✅ Write tests
✅ Update documentation
✅ Follow project style guide
```

### Stand Out
```
✅ Fix critical bugs (high priority)
✅ Improve performance
✅ Add security features
✅ Help other participants
✅ Review PRs quickly
✅ Be active in discussions
```

---

## 📊 Daily Checklist

### Morning
- [ ] Check Discord/Slack
- [ ] Sync with main
- [ ] Review PR feedback
- [ ] Pick 2-3 issues for the day
- [ ] Estimate time for each

### During Work
- [ ] Commit every 30 minutes
- [ ] Sync with main every 2 hours
- [ ] Test your changes
- [ ] Ask for help if stuck > 30 min
- [ ] Take breaks (Pomodoro: 25 min work, 5 min break)

### Before Push
- [ ] Test thoroughly
- [ ] Sync with main
- [ ] Fix conflicts
- [ ] Write good commit message
- [ ] Create descriptive PR

### Evening
- [ ] Push all work
- [ ] Update issue status
- [ ] Plan tomorrow's issues
- [ ] Help others if time permits

---

## 🎯 Success Metrics

### Beginner Goal
```
✅ Complete 5-8 issues
✅ Zero merge conflicts
✅ All PRs merged
✅ Help 2-3 people
```

### Intermediate Goal
```
✅ Complete 10-15 issues
✅ Handle conflicts smoothly
✅ Review 5+ PRs
✅ Contribute to discussions
```

### Advanced Goal
```
✅ Complete 15-20 issues
✅ Solve critical bugs
✅ Mentor beginners
✅ Lead a feature
✅ Top 10 leaderboard
```

---

## 🚨 Common Mistakes to Avoid

```
❌ Not syncing with main regularly
❌ Working on same files as others
❌ Pushing at the last minute
❌ Not testing before pushing
❌ Not asking for help when stuck
❌ Taking too complex issues first
❌ Not reading issue description fully
❌ Ignoring PR review feedback
❌ Not communicating progress
❌ Skipping breaks (burnout!)
```

---

## 💡 Pro Tips

```
✅ Use GitHub CLI for faster workflow
✅ Set up code snippets in IDE
✅ Keep a notepad for commands
✅ Bookmark important docs
✅ Use git aliases for common commands
✅ Keep water & snacks nearby
✅ Take 5-min breaks every hour
✅ Sleep well (don't code all night!)
✅ Network with other participants
✅ Have fun! 🎉
```

---

## 🔥 Git Aliases (Time Savers)

Add to `~/.gitconfig`:
```bash
[alias]
    st = status
    co = checkout
    br = branch
    cm = commit -m
    ps = push
    pl = pull
    sync = !git fetch origin && git merge origin/main
    save = !git add . && git commit -m "wip: save progress"
```

Usage:
```bash
git sync    # Instead of: git fetch origin && git merge origin/main
git save    # Quick save your work
git st      # Check status
```

---

## 📚 Resources

### Learn Git
- https://learngitbranching.js.org/
- https://git-scm.com/docs
- GitHub Skills: https://skills.github.com/

### Practice
- https://github.com/firstcontributions/first-contributions
- https://www.freecodecamp.org/news/how-to-contribute-to-open-source/

### During Hackathon
- Keep this roadmap open
- Refer to QUICK-REFERENCE.md
- Check COMMON-ERRORS.md when stuck

---

## ✅ Final Checklist Before Hackathon

- [ ] Git installed and configured
- [ ] GitHub account ready
- [ ] IDE set up with extensions
- [ ] Practiced git workflow 5 times
- [ ] Joined Discord/Slack
- [ ] Read project documentation
- [ ] Tested local development setup
- [ ] Prepared questions to ask
- [ ] Set up comfortable workspace
- [ ] Ready to learn and have fun! 🚀

---

**Remember: Hackathons are about learning, networking, and having fun!**
**Don't stress about winning - focus on improving your skills! 💪**

Good luck! 🎉
