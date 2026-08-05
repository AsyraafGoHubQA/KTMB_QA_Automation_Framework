Here is your **cleaned, more natural, and user-friendly README.md version** formatted for VS Code / GitHub usage. I’ve simplified the language, improved flow, and made it feel more like a real engineering team document.

---

# ReadMe : Playwright + Python Automation Framework

## Environment Setup Guide

Welcome! 👋
This guide will help you set up your machine so you can run and develop automation tests using the Playwright + Python framework.

Please follow the steps in order before running any tests.

---

# 1. Prerequisites

Before starting, make sure the following tools are installed on your system:

| Tool               | Recommended Version | Download Link                     |
| ------------------ | ------------------- | --------------------------------- |
| Python             | 3.12 or later       | https://www.python.org/downloads/ |
| Visual Studio Code | Latest              | https://code.visualstudio.com/    |
| Git                | Latest              | https://git-scm.com/downloads     |
| Google Chrome      | Latest              | https://www.google.com/chrome/    |

---

#PS : "Bash" means typing commands into a shell

# 2. Verify Installation

Open **Command Prompt (Windows)** or **Terminal (Mac/Linux)** and run the following commands.

## Check Python

```bash
python --version
```

You should see something like:

```text
Python 3.12.x
```

👉 This confirms Python is installed correctly.

---

## Check Git

```bash
git --version
```

You should see:

```text
git version x.x.x
```

👉 This confirms Git is installed correctly.

---

# 3. Install VS Code Extensions

Open VS Code and install these extensions:

| Extension                   | Purpose                           |
| --------------------------- | --------------------------------- |
| Python                      | Python support                    |
| Pylance                     | IntelliSense and code suggestions |
| Playwright Test for VS Code | Run and debug tests               |
| GitLens (Optional)          | Better Git history view           |

---

# 4. Clone the Project
--Can skip this part first.
Download the project from GitHub:

```bash
git clone <GitHub Repository URL>
```

👉 This copies the project to your local machine.

Move into the project folder:

```bash
cd automation-framework
```

---

# 5. Open Project in VS Code

1. Open **Visual Studio Code**
2. Click **File → Open Folder**
3. Select the cloned project folder

---

# 6. Create Virtual Environment

We use a virtual environment to keep dependencies clean and isolated.

```bash
python -m venv .venv
```

👉 This creates a local Python environment inside your project.

---

# 7. Activate Virtual Environment

## Windows

```bash
.venv\Scripts\activate
```

## Mac / Linux

```bash
source .venv/bin/activate
```

Once activated, you will see:

```text
(.venv)
```

---

# 8. Install Playwright

Install Playwright:

```bash
pip install playwright
```

Now install browser binaries:

```bash
playwright install
```

👉 This downloads Chromium, Firefox, and WebKit browsers.

---

# 9. Verify Playwright Installation

```bash
playwright --version
```

If you see a version number, Playwright is installed successfully ✅

---

# 10. Configure Python in VS Code

1. Press **Ctrl + Shift + P**
2. Search: **Python: Select Interpreter**
3. Select the interpreter inside `.venv`

Example:

```text
.venv/Scripts/python.exe
```

👉 This ensures VS Code uses the correct environment.

---

# 11. Git Workflow (Daily Use)

## Get latest code

```bash
git pull
```

👉 Always run this before starting work.

---

## Save your changes

```bash
git add .
```

👉 Stages your changes.

```bash
git commit -m "your message here"
```

👉 Saves your work locally.

```bash
git push
```

👉 Sends your changes to GitHub.

---

# 13. Troubleshooting

## Python not found

* Reinstall Python
* Make sure **“Add to PATH”** is checked

---

## Git not found

* Reinstall Git
* Enable **Add Git to PATH**

---

## Playwright browsers missing

```bash
playwright install
```

---

## Missing Python modules

```bash
pip install -r requirements.txt
```

---

# ✅ Setup Checklist

Make sure everything below is completed:

* Python installed
* Git installed
* VS Code installed
* Required extensions installed
* Project cloned
* Virtual environment created
* Virtual environment activated
* Dependencies installed
* Playwright installed
* Browsers installed
* Python interpreter configured
* Sample test executed successfully

---

🎉 Once all steps are done, your environment is ready for automation development!

---
