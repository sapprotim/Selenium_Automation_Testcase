# ConnectedLife – Automated Test Suite

End-to-end UI test suite for the **ConnectedLife** healthcare management platform, built with Python, Pytest, and Selenium WebDriver.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running Tests](#running-tests)
- [Test Reports](#test-reports)
- [CI/CD](#cicd)
- [Credentials](#credentials)

---

## Overview

This repository contains automated regression tests covering every major role and feature of the ConnectedLife web application:

| Role | Covered |
|------|---------|
| Organization Admin | Programme Management, Analytics, Alerts & Nudges |
| Facility Admin | Facility & Department management |
| Department Admin | Department workflows |
| Clinician | Clinician-specific screens |
| User / Patient | Onboarding, Profile, Schedule, Challenges |

---

## Project Structure

```
AH_Automation_Testcase/
├── .github/
│   └── workflows/
│       └── python-package-conda.yml   # GitHub Actions CI pipeline
│
├── Login_logout/
│   └── test_login_logout.py
│
├── Facility admin/
│   └── Test_Facility_admin.py
│
├── Department Admin/
│   └── test_department_admin.py
│
├── Clinician/
│   └── test_clinician.py
│
├── User/
│   ├── test_user_onboarding.py
│   └── test_User_page.py
│
├── Facility and department/
│   └── Test_Facility_and_department.py
│
├── Analytics/
│   └── Test_Analytics.py
│
├── Appnication Tacker/
│   └── test_Application_Tracker.py
│
├── Programme Management/
│   ├── Test_challenge.py
│   ├── test_alerts_Nudges.py
│   ├── test_Specialised Nutrition.py
│   ├── test_Physiotherapy_Equipments.py
│   ├── test_Physiotherapy_Exercises.py
│   ├── test_medichine.py
│   ├── test_Links.py
│   ├── test_Predefined_stm_Message.py
│   ├── test_Predefined_user_Messages.py
│   └── test_Themes.py
│
├── user profile/
│   ├── test_Overview.py
│   ├── test_Analysis.py
│   ├── test_Analytics.py
│   ├── test_Specialist.py
│   ├── test_Document.py
│   ├── Test_alerts_Nudge.py
│   ├── test_Challenge.py
│   └── Schecudule/
│       ├── test_Activity.py
│       ├── test_Stay_Hydrated.py
│       ├── test_Take_Rest.py
│       ├── test_Medication_&_Specialised_Nutrition.py
│       └── test_Report Condition.py
│
├── excelfile.py                        # Excel credential reader utility
├── driver.py                           # Driver utility
└── program management.py              # Standalone org-admin programme management tests
```

---

## Prerequisites

- Python 3.10
- Conda (recommended) or pip
- Google Chrome + matching [ChromeDriver](https://chromedriver.chromium.org/downloads)
- The following Python packages:

| Package | Purpose |
|---------|---------|
| pytest | Test runner |
| selenium | Browser automation |
| pandas | Read credentials from Excel |
| faker | Generate random test data |
| openpyxl | Excel file support |

---

## Setup

### Using Conda (recommended)

```bash
# Clone the repository
git clone https://github.com/sapprotim/Testcase.git
cd Testcase

# Create and activate environment
conda env create -f environment.yml
conda activate <env-name>
```

### Using pip

```bash
pip install pytest selenium pandas faker openpyxl pytest-html
```

### Credentials file

Tests read login credentials from an Excel file. Place `login info.xlsx` at:

```
D:\userinfo\login info.xlsx
```

The file must follow this row structure:

| Row (0-indexed) | Role | Columns: Username (B), Password (C), OTP (D) |
|-----------------|------|----------------------------------------------|
| 0 | URL | App URL in column B |
| 1 | Org Admin | org username, password, OTP |
| 2 | Facility Admin | facility username, password, OTP |
| 3 | Department Admin | dept username, password, OTP |
| 4 | STM1 / Clinician | stm1 username, password, OTP |
| 5 | STM2 | stm2 username, password, OTP |
| 6 | User/Link | user username, password, OTP |

> **Security note:** No credentials are committed to the repository. All test files read credentials at runtime from the local Excel file. Never hardcode usernames, passwords, or OTPs directly in test files.

---

## Running Tests

```bash
# Run all tests
pytest

# Run a specific module
pytest "Login_logout/test_login_logout.py"

# Run with verbose output
pytest -v

# Run and generate HTML report
pytest --html=reports/selenium_report.html
```

---

## Test Reports

After a test run, open the generated report in your browser:

```
reports/selenium_report.html
```

The report includes:
- Pass / fail / skip counts per test
- Screenshot captures on failure
- Detailed step-by-step logs

---

## CI/CD

The repository uses **GitHub Actions** (`.github/workflows/python-package-conda.yml`):

1. Sets up Python 3.10 with Conda
2. Installs dependencies from `environment.yml`
3. Runs `flake8` linting (max line length: 127)
4. Executes the full pytest suite

---

## Credentials

Test credentials are **not** committed to the repository. The `excelfile.py` utility and each test fixture read them at runtime from the local Excel file at `D:\userinfo\login info.xlsx`. Make sure this file exists and is correctly populated before running the tests locally.
