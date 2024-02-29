# Cryptography and Hashing

Welcome to the Cryptography and Hashing repository! In this comprehensive course, we explore a wide range of cryptographic concepts, private and public key cryptosystems, various encryption algorithms, and hashing techniques. Whether you're a beginner or an experienced coder, this repository provides both theoretical insights and practical implementations.

## Requirements

To run the **Python** code in this repository, you'll need to set up a Python environment on your machine. Follow the steps below to get started:

### 1. Install Python

If you don't have Python installed, download and install it from the official [Python website](https://www.python.org/). Make sure to check the option to add Python to your system PATH during installation.

### 2. Set Up a Virtual Environment (Optional but Recommended)

It's recommended to use a virtual environment to manage your project dependencies and avoid conflicts with other projects. Open a terminal and run the following commands:

1. Install Python:
   
Windows:
Visit the Python Downloads page.
Download the latest version of Python (3.x) for Windows.
Run the installer and make sure to check the box that says "Add Python to PATH" during installation.

macOS:
macOS usually comes with Python pre-installed. Open the Terminal and check the installed version:

```bash
python3 --version
```

If not installed or you want a different version, consider using Homebrew to install or upgrade Python:

```bash
brew install python
```

Linux (Debian/Ubuntu)
Open the terminal and run:

```bash
sudo apt update
sudo apt install python3
```

1. Verify Installation:
Open a command prompt or terminal and check the installed Python version:

```bash
python --version   # or python3 --version
```

3. Optional: Set Up Virtual Environment:
Setting up a virtual environment is recommended to keep project dependencies isolated. This step is optional but recommended for managing Python projects.

Install virtualenv (if not already installed):
```bash
pip install virtualenv
```
Create a Virtual Environment:
Navigate to your project folder and run:

```bash
# On Windows
python -m venv venv

# On macOS/Linux
python3 -m venv venv
```

Activate the Virtual Environment:
On Windows:

```bash
.\venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```
4. Install Dependencies:
If you are using a virtual environment, make sure it's activated. Then install the required packages using pip:

```bash
pip install -r requirements.txt
```
Replace requirements.txt with the actual file containing your project dependencies.

Now, you have a Python environment set up on your system! You can start writing and running Python code in this environment.

## Contents

1. [Cryptography Fundamentals](#cryptography-fundamentals)
   - What is the aim of cryptography?
   - Private key and public key cryptosystems

2. [Chapter 2 - Caesar Cipher](#chapter-2---caesar-cipher)
   - Caesar cipher theory and implementation
   - How to crack Caesar cipher
   - Frequency analysis and language detection

