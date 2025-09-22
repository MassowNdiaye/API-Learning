# Learning Notes: 

# ⚠️ **Viewing my APIs over HTTP:** 
 Activate the virtual environment (venv/bin/activate) and run the app:
 - python -m uvicorn main:app --reload

---

# **⚠️ .DS_Store stands for Desktop Service Store.** - Sep 22 2025 - 1:14PM
 It's a hidden system file automatically created by macOS in every folder opened with Finder. 

 It stores folder view preferences, like: 
  - icon positions 
  - window size
 - background color/image

 ✅ **Best practice**
 It's not needed for the code or GitHub, Add it to .gitignore so it doesn't get pushed to GitHub. 

---

 # ⚠️ **GitHub status/add/commit/push** - Sep 22 2025 - 1:26PM
 - git status
 - git add (.) -> add all change in the project 
 - git commit -m "text or commment/title" 
 - git push

---

# ⚠️ **venv = Virtual Environment in Python** - Sep 22 2025 - 1:32PM 
 It's like a BOX where you install packages only for one project, without affecting others projects or your global Python installation. 

- **Why use it?**
 1. Keeps dependecies separate per project. 
 2. Prevent conflicts between package versions.
 3. Makes project reproducible (using requirements.txt)


- **Basic Workflow**
 1. Create a venv
 python -m venv venv  ->  The second venv is just the folder name, can be changed. 

 2. Activate it
 source venv/bin/activate -> You'll see (venv) at the start of the terminal -> means it's active ✅
 
 3. Example of package installation **(FastAPI)**

 **pip install fastapi uvicorn**

 - fastapi -> package name.
 - uvicorn -> Runs FastApi app so you can test APIs in the browser using tools like Postman.

- **Basic Command**
If FastAPI app is inside a file main.py and the app is called "app"" 

 **uvicorn main:app --reload**
 
 main -> filename (main.py)
 app -> the FastAPI app
 --reload -> auto-restarts the server when you change code

 After running the command,this open gives a HTTP.

