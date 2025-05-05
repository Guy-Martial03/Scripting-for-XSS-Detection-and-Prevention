# Scripting Defenses to Prevent Cross-Site Scripting (XSS)

## Introduction

Cross-Site Scripting (XSS) remains one of the most common and dangerous vulnerabilities affecting modern web applications. 
This project aims to provide a clear and practical understanding of how XSS attacks work, the different types of 
XSS (Reflected, Stored, and DOM-based), and most importantly, how to protect web applications against them.
By simulating real-world scenarios, this project allows learners to explore how XSS vulnerabilities are exploited 
and how to effectively detect and mitigate them.

## Objective of the XSS Attack:

The goal is to execute malicious code in the victim's browser as if it originated from a trusted website. 
This can allow the attacker to:

- Steal session cookies or other sensitive data

- Impersonate a logged-in user

- Perform actions on behalf of the user (e.g., form submission, clicks)

- Redirect the user to a malicious website

## Pre-requisites

- Intermediate understanding of SQL
- Knowledge of the Python language
- Familiarity with network and system security concepts
- Solid experience with scripting and regular expressions

## Lab Set-up and Tools

- A computer running a windows 10
- Flask – A lightweight web framework for Python.
- SQLite – A simple, file-based relational database included by default with Python via the sqlite3 module. Ensure you are using Python 3.x or later.

## Follow steps

### Step 1: Flask Server

**Objective**: Install Flask server.

 Install Flask:
    ```powershell
    pip install flask
    ```

### Step 2: Running the Application

**Objective**: Running Scripting_Against_XSS_App

 Navigate to the project directory in your terminal :
    ```powershell
    python Scripting_Against_XSS_App.py
    ```

### Step 3: Accessing the Web Interface

**Objective**: Web interface

Once the application is running, open your web browser and navigate to the following address to access the login interface

 ```powershell
   http://localhost:5001
    ```
	
### Performing XSS Tests

**Objective**: Demonstrating XSS Exploits

You can now perform XSS tests by following the examples provided in the " Payload_XSS " file.
This file contains a collection of common XSS payloads designed to demonstrate how different types of attacks behave 
within the application.

## Conclusion

This project provides a practical and educational environment for understanding, testing, and mitigating Cross-Site Scripting (XSS) 
vulnerabilities. By simulating real-world attack scenarios and applying secure coding techniques, developers and security enthusiasts 
can strengthen their awareness and improve the resilience of their web applications.

Thank you for exploring this project — contributions, feedback, and suggestions are always welcome.

