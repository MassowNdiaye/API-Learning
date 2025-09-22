# Mistakes/Errors and Solutions 

**⚠️ Warning: Don’t Rename Folders While VS Code Is Open - Sep 20 2025 - 10:35PM**

Renaming folders while VS Code is open can cause:

- Broken file links (open files may “disappear”).
- Git confusion (files may appear deleted or moved).
- Extensions to stop working.

✅ **Safe way:**  
Rename folders **inside VS Code** or **close VS Code** before renaming externally.

--- 

**⚠️ Never put .gitignore inside venv file or Push venv files on GitHub** - Sep 22 2:15PM - 2025

 1. Add venv to .gitignore
 2. git rm -r --cached venv   ->  Used to untrack venv if pushed to GitHub
 3. git commit -m "Removed venv from repository and updated .gitignore" 
 4. git push

**⚠️ Installling requirements.txt from GitHub after I created issues** - Sep 22 2:24PM - 2025

 1. source venv/bin/activate (Make sure to be inside venv)
 2. pip install -r requirements.txt or pip3 if pip not found message come out.

---
 
