# mypygui

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge"/></a>
  <a href="https://docs.python.org/3/library/tkinter.html"><img src="https://img.shields.io/badge/Tkinter-GUI-green?style=for-the-badge"/></a>
  <a href="https://mariadb.org/"><img src="https://img.shields.io/badge/MariaDB-Database-orange?style=for-the-badge"/></a>
  <a href="https://github.com/Marvellbrazil/mypygui/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Marvellbrazil/mypygui?style=for-the-badge"/></a>
</p>

A simple Python GUI application using Tkinter connected to MariaDB — built as a learning project to demonstrate GUI forms, data input, and basic CRUD operations.

---

## Table of Contents

- [Overview](#overview)
- [Technologies](#technologies)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**mypygui** is a beginner-friendly desktop application built with Python and Tkinter, integrated with a MariaDB database.  
The goal of this project is to help learners understand:

- how to build desktop GUI applications,
- how to handle form inputs,
- how to display stored records in a table view.

This project is intentionally kept simple, clean, and easy to modify.

---

## Technologies

- **Python 3.11**
- **Tkinter (built-in GUI library)**
- **MariaDB**
- **mariadb Python connector**

---

## Prerequisites

Make sure you have:

- Python 3.x installed  
- MariaDB or MySQL server installed  
- Database created (e.g. `db_mypygui`)
- Required Python package:

```bash
    git clone https://github.com/Marvellbrazil/mypygui.git
    cd mypygui

    python -m venv venv
    venv\Scripts\activate

    pip install mariadb
```

## Setup

Make sure you setup your database connection in <code>connection.py</code> before running the program :

```sql
CREATE DATABASE db_mypygui;
```

```python
__DB_HOST__ = "localhost"
__DB_USN__ = "<your_username>"
__DB_PASS__ = "<your_password>"
__DB_PORT__ = 3306 # Default mariadb port
__DB_NAME__ = "db_mypygui"
```

## Run

To run type this in the terminal :

```bash
python main.py
```