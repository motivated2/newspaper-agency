﻿# Newspaper Agency Management System

Welcome to the Newspaper Agency Management System! This Django project is designed to help newspaper agencies keep track of their redactors and the newspapers they publish. 

## Introduction

In the fast-paced world of journalism, it's essential to keep track of the talented redactors who contribute to your newspaper agency. With this system, you can efficiently manage your team of redactors and easily track which redactors are assigned to each newspaper.

## Check it out

https://newspaper-agency-94mx.onrender.com/

## Test user

- **login**: testUser
- **password**: p7cz>}CNYtDryhi

## Features

- **Redactor Management**: Easily manage your team of redactors. Keep track of their usernames, names, and years of experience.
  
- **Topic Management**: Create and assign topics to each newspaper. This allows for better organization and categorization of your content.

- **Newspaper Publication**: Keep track of newspapers published by your agency. Each newspaper entry includes details such as title, content, published date, and the redactors who contributed to it.

- **Multiple Topics Assignment**: Assign more than one topic to each newspaper. This feature enhances flexibility and allows for better classification of content.

## Database Structure

The database structure of this project consists of three main models:

1. **Redactor**: Represents a redactor in the system. Inherits from the Django `AbstractUser` model and includes additional fields such as years of experience.

2. **Topic**: Represents a topic or category for newspapers. Each topic has a name.

3. **Newspaper**: Represents a newspaper published by the agency. Includes fields such as title, content, published date, and relationships with redactors and topics.

## Installation

To run this project locally, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your_username/newspaper-agency-management.git
```

2. Navigate to the project directory:

```bash
cd newspaper-agency-management
```

3. Create a virtual environment and activate it (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Apply migrations:

```bash
python manage.py migrate
```

6. Create a superuser to access the admin panel:

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

8. Access the application in your web browser at `http://localhost:8000/`.

## Usage

1. **Admin Panel**: Access the Django admin panel at `http://localhost:8000/admin/` to manage redactors, topics, and newspapers.

2. **Redactor Management**: Add, edit, or delete redactors in the admin panel. Keep track of their usernames, names, and years of experience.

3. **Topic Management**: Create, edit, or delete topics in the admin panel. Assign topics to newspapers to categorize your content effectively.

4. **Newspaper Publication**: Add new newspapers in the admin panel. Specify the title, content, published date, and assign redactors and topics to each newspaper.

5. **Multiple Topics Assignment**: When adding or editing a newspaper, you can assign multiple topics to it, ensuring comprehensive categorization of your content.

## Contributors

- Ihor Bondarenko (igorb6766@gmail.com)

---

Feel free to contribute to this project by submitting pull requests or reporting issues. Happy tracking of your redactors and newspapers! 📰👩‍💻👨‍💼
