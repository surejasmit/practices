# 🚀 Hackathon Cheat Sheet - Keep This Open!

## ⚡ Quick Commands (Copy-Paste Ready)

### Starting New Issue
```bash
git checkout main
git pull origin main
git checkout -b issue-123-description
```

### While Working (Every 2 Hours)
```bash
git fetch origin
git merge origin/main
```

### Before Pushing (ALWAYS!)
```bash
git add .
git commit -m "feat: your description"
git fetch origin
git merge origin/main
git push origin issue-123-description
```

### If Merge Conflict
```bash
# 1. Open conflicted file
# 2. Find <<<<<<< markers
# 3. Keep both changes
# 4. Remove markers
git add .
git commit -m "fix: resolve conflicts"
git push origin issue-123-description
```

---

## 📋 Hourly Checklist

### Every Hour
- [ ] Commit your work
- [ ] Check Discord for updates
- [ ] Drink water 💧

### Every 2 Hours
- [ ] Sync with main: `git fetch origin && git merge origin/main`
- [ ] Take 5-min break 🧘
- [ ] Test your code

### Before Meals
- [ ] Push your work
- [ ] Update issue status
- [ ] Reply to messages

---

## 🎯 Issue Priority

**Pick in this order:**
1. ⭐ Good first issue (Start here!)
2. 🐛 Bug fixes (Quick wins)
3. 📝 Documentation (Easy points)
4. ✨ New features (More points)
5. 🔥 Critical bugs (High impact)

---

## 💬 Communication Templates

### Starting Issue
```
"Working on #123 - [Issue Title]
ETA: 2 hours"
```

### Need Help (After 30 min stuck)
```
"Need help with #123
Error: [paste error]
What I tried: [list attempts]"
```

### Pushing Code
```
"Pushed PR for #123
Ready for review 👀"
```

### Merge Conflict
```
"Got conflict in [file.py]
Resolving now, will push in 10 min"
```

---

## 🚨 Emergency Commands

### Undo Last Commit (Keep Changes)
```bash
git reset --soft HEAD~1
```

### Abort Merge
```bash
git merge --abort
```

### See What Changed
```bash
git status
git diff
```

### Discard All Changes (CAREFUL!)
```bash
git checkout .
```

### Switch Branch (Save Work First)
```bash
git stash
git checkout other-branch
git stash pop
```

---

## ✅ Before Push Checklist

- [ ] Code works locally
- [ ] Tests pass
- [ ] Synced with main
- [ ] No conflicts
- [ ] Good commit message
- [ ] Removed console.logs / print statements
- [ ] Removed commented code

---

## 🏆 Points Strategy

### Day 1 (Focus: Quantity)
- Complete 5-6 easy issues
- Get comfortable with workflow
- Build confidence

### Day 2 (Focus: Quality)
- Complete 3-4 medium issues
- Review others' PRs
- Help beginners

### Day 3 (Focus: Impact)
- Complete 1-2 hard issues
- Fix critical bugs
- Final polish

---

## 💡 Quick Wins

✅ Fix typos in docs (5 min)
✅ Add comments to code (10 min)
✅ Improve error messages (15 min)
✅ Add input validation (20 min)
✅ Write unit tests (30 min)

---

## 🔥 Git Aliases (Add Once, Use Forever)

```bash
git config --global alias.sync '!git fetch origin && git merge origin/main'
git config --global alias.save '!git add . && git commit -m "wip: save"'
git config --global alias.undo 'reset --soft HEAD~1'
```

Now use:
```bash
git sync    # Sync with main
git save    # Quick save
git undo    # Undo last commit
```

---

## 📱 Keep Open in Browser

1. This cheat sheet
2. GitHub repo (for issues)
3. Discord/Slack
4. Project documentation
5. Stack Overflow (for errors)

---

## 🎯 Remember

**The 3 Rules:**
1. Sync with main BEFORE starting
2. Sync with main BEFORE pushing
3. Ask for help after 30 min stuck

**The 3 Don'ts:**
1. Don't work for hours without syncing
2. Don't push without testing
3. Don't panic when conflicts happen

---

## 🆘 When Stuck

1. Read error message carefully
2. Google the error
3. Check project docs
4. Ask in Discord (after 30 min)
5. Ask organizer (after 1 hour)

---

## ⏰ Time Management

```
09:00 - 10:00  Setup & pick issue
10:00 - 12:00  Work on issue 1
12:00 - 13:00  Lunch + sync with main
13:00 - 15:00  Work on issue 2
15:00 - 15:15  Break + sync with main
15:15 - 17:00  Work on issue 3
17:00 - 18:00  Review PRs + help others
18:00          Push everything & go home!
```

---

## 🎉 Most Important

- **Have fun!** 🎊
- **Learn new things** 📚
- **Make friends** 👥
- **Don't stress** 😌
- **Ask questions** ❓
- **Help others** 🤝

---

**Print this page or keep it open during the hackathon!**

**Good luck! You got this! 💪🚀**
