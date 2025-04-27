## conflict-hellfire
A chaotic Git conflict simulation designed to sharpen advanced Git skills.
This repo intentionally creates merge conflicts between multiple feature branches to simulate real-world complex merge situations.

###📜 Problem Statement
In real-world collaborative projects, Git conflicts are inevitable.
This project was created to practice and master conflict resolution, cherry-picking, and merge strategies under tough scenarios.

###🔥 Project Structure
app.py:
Handles login functionality.
Payment processing feature.

utils.py:
Functions for encryption, decryption, tax calculation, and logging login activities.

README.md:
Project documentation.

###🐛 Problem Faced
When trying to merge different feature branches (feature/login, feature/payment, feature/security) into main, complex conflicts were encountered:
Changes from different features overlapped on the same lines in utils.py and app.py.
Some commits were only on the feature branches and not on main, causing incomplete merges.
Because of this, direct merging was not sufficient — leading to an issue where:
My commits were on a different branch.
Direct merge would have lost some feature work or overwritten other features.

###🔨 Solution Strategy
Cherry-pick specific commits from the feature branches.
Manually resolve merge conflicts in app.py and utils.py.
Commit and push after every conflict resolution.
Keep Git history clean with meaningful commit messages.

🚀 How to Reproduce
Clone the repo:
```
git clone https://github.com/its-tsukii/conflict-hellfire.git
cd conflict-hellfire
```
Check branches:
```
git branch -a
```
Simulate the conflict by trying to merge feature branches into main:
```
git checkout main
git merge feature/login
git merge feature/payment
git merge feature/security
```
When conflicts happen:
Open the conflicted files.
Manually edit and resolve.
```
git add .
git commit
```
If commits exist on a different branch only:
Find the commit hash with:
```
git log --oneline --all
```
Cherry-pick:
```
git cherry-pick <commit-hash>                # for commit-hash look into echo "$(git log --oneline --graph --all)"
Resolve conflicts again if needed and continue.
```
Push the final clean main branch:
```
git push origin main
```

###🏆 Lessons Learned
Merging is easy until conflicts show up — real mastery is in handling them.
Cherry-picking is a powerful tool for selecting specific commits across branches.
Manual conflict resolution teaches you about code ownership and responsibility.
Patience and attention is key when fighting "conflict hellfire" battles.

###🎯 Final Status
✅ Successfully merged all features into main.
✅ Repo is now clean, and all functionalities are preserved.

🔗 Repo Link
👉 conflict-hellfire
