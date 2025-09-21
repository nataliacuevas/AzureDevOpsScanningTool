# Enforcing Least Privilege in Azure DevOps

This repository was created as part of:
- An internship at **PrimeFaktor IT Solutions GmbH**  
- A bachelor's thesis at **FH Technikum Wien**

The work is documented in the thesis:  
**"Enforcing Least Privilege in Azure DevOps: A Policy-Based Approach Leveraging Entra ID to Mitigate Architectural and Default Permissions Risks"**

---

## Repository Overview

The repository contains two main components:

- **Frontend** — built with React  
- **Backend** — built with Python (Flask)

⚠️ **Note:** The code is not in a production-ready state. It contains experimental files (e.g., configurations, Dockerfiles, etc.) and represents the version submitted for the thesis. Further iterations are maintained in a private repository.

---

## Getting Started

### 0. Adjust the Source Code
To scan an Azure DevOps organization, the application requires:
- A **Personal Access Token (PAT)**
- The **Organization name**

Currently, the organization is hardcoded. To update it:

1. Find the name of your Azure DevOps organization.  
2. Open `backend/app.py`.  
3. Replace the string `testOrgpf` with your organization name.

---

### 1. Backend Setup

1. Open a terminal in the `backend` folder.  
2. Ensure **Python 3** is installed.  
3. Create a virtual environment:  
   ```bash
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Start the backend:
   ```bash
   python3 app.py
   ```

---

### 2. Frontend Setup
1. Open a terminal in the `frontend` folder
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the frontend:
   ```bash
   npm start
   ```

---

### 3. Provide a Personal Access Token (PAT)
1. Generate a PAT in your Azure DevOps organization with **Read rights** for users and groups
2. Enter the PAT in the application's UI

---

### Extras
The `/assets` folder contains interview files collected during the thesis process.
These files are **Not required** for running the code.

---

### License
This project is intended for academic and research purposes only.
For further development or usage in production, please contact the author.

