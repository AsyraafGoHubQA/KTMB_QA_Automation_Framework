# Playwright + Python Automation Framework

## Environment Setup Guide

Welcome! 👋

This guide explains how to set up your development environment before using the Playwright + Python Automation Framework.

Please complete all the steps below before running any automation tests.

---

# 1. Prerequisites

Before starting, ensure the following software is installed on your machine.

| Tool | Recommended Version | Download |
|------|----------------------|----------|
| Python | 3.12 or later | https://www.python.org/downloads/ |
| Visual Studio Code | Latest | https://code.visualstudio.com/ |
| Git | Latest | https://git-scm.com/downloads |
| Google Chrome | Latest | https://www.google.com/chrome/ |

---

> **Note**
>
> All commands shown in this guide are shell commands.
> Windows users can execute them using **VS Code Terminal**, **PowerShell**, **Command Prompt**, or **Git Bash**.

---

# 2. Verify Installation

Open **Command Prompt**, **PowerShell**, **Git Bash**, or the **VS Code Terminal**.

## Verify Python Installation

```bash
python --version
```

Expected Output

```text
Python 3.12.x
```

This confirms Python has been installed successfully.

---

## Verify Git Installation

```bash
git --version
```

Expected Output

```text
git version x.x.x
```

This confirms Git has been installed successfully.

---

# 3. Install VS Code Extensions

Open Visual Studio Code and install the following extensions.

| Extension | Required | Purpose |
|-----------|----------|---------|
| Python | ✅ | Python language support |
| Pylance | Recommended | IntelliSense and code completion |
| Playwright Test for VS Code | Recommended | Execute and debug Playwright tests |
| GitLens | Optional | Enhanced Git history |

---

<<<<<<< HEAD
# 4. Clone the Project
--Can skip this part first.
Download the project from GitHub:
=======
# 4. Clone the Repository

Clone the automation project from GitHub.
>>>>>>> b3a8bda (Update README with environment setup guide)

```bash
git clone https://github.com/AsyraafGoHubQA/KTMB_QA_Automation_Framework.git
```

Navigate to the Login Module project.

```bash
cd "Login Module"
```

---

# 5. Open the Project in Visual Studio Code

1. Open Visual Studio Code.
2. Click **File → Open Folder**.
3. Select the **Login Module** folder.

---

# 6. Create a Virtual Environment

Create a Python virtual environment.

```bash
python -m venv .venv
```

This creates an isolated Python environment for the project.

---

# 7. Activate the Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

Once activated, your terminal should display:

```text
(.venv)
```

---

# 8. Install Project Dependencies

Install all required Python packages.

```bash
pip install -r requirements.txt
```

This installs all dependencies required by the automation framework.

---

# 9. Install Playwright


Install the Playwright package.

```bash
pip install playwright
```

Install the required browser binaries.

```bash
playwright install
```

This downloads the supported browsers (Chromium, Firefox, and WebKit).

---

# 9. Verify Playwright Installation

Run:

```bash
playwright --version
```

If a version number is displayed, Playwright has been installed successfully.

---

<<<<<<< HEAD
# 10. Configure Python in VS Code
=======
# 11. Configure Python Interpreter in VS Code
>>>>>>> b3a8bda (Update README with environment setup guide)

1. Press **Ctrl + Shift + P**
2. Search for **Python: Select Interpreter**
3. Select the interpreter located in the `.venv` folder.

Example:

```text
.venv\Scripts\python.exe
```

This ensures Visual Studio Code uses the correct Python environment.

---

<<<<<<< HEAD
# 11. Git Workflow (Daily Use)
=======
# 12. Run the Sample Login Test
>>>>>>> b3a8bda (Update README with environment setup guide)

Verify that the framework has been configured correctly.

```bash
pytest tests/test_login.py
```

Expected Result:

- Browser launches successfully.
- Login automation is executed.
- Test execution result is displayed in the terminal.

If the test runs successfully, your environment setup is complete.

---

# 13. Daily Git Workflow

## Before Starting Work

Pull the latest changes from GitHub.

```bash
git pull
```

---

## After Completing Your Changes

Stage your changes.

```bash
git add .
```

Commit your changes.

```bash
git commit -m "Describe your changes"
```

Push your changes to GitHub.

```bash
git push
```

---

# 14. Project Structure

```text
Login Module
│
├── data
│
├── pages
│
├── tests
│
├── utils
│
├── screenshots
│
├── README.md
│
├── requirements.txt
│
└── runner.py
```

---

# 15. Troubleshooting

## Python Not Found

- Reinstall Python.
- Ensure **Add Python to PATH** is selected during installation.

---

## Git Not Found

- Reinstall Git.
- Ensure Git is added to the system PATH.

---

## Playwright Browsers Missing

Run:

```bash
playwright install
```

---

## Missing Python Modules

Run:

```bash
pip install -r requirements.txt
```

---

# Current POC Scope

The current Proof of Concept (POC) includes the following components:

- ✅ Playwright Framework Setup
- ✅ Python Integration
- ✅ Page Object Model (POM)
- ✅ Data-Driven Testing (Excel)
- ✅ Login Module Automation
- ✅ Git Version Control
- ✅ Project Environment Setup Guide

---

# Environment Setup Checklist

<<<<<<< HEAD
---
=======
Before executing any automation, ensure the following tasks have been completed.

- [ ] Python installed
- [ ] Git installed
- [ ] Visual Studio Code installed
- [ ] Required VS Code extensions installed
- [ ] Repository cloned successfully
- [ ] Virtual environment created
- [ ] Virtual environment activated
- [ ] Project dependencies installed
- [ ] Playwright installed
- [ ] Playwright browsers installed
- [ ] Python interpreter configured
- [ ] Sample login test executed successfully

---

Your machine is now fully configured and ready to develop and execute automation tests using the Playwright + Python Automation Framework.
