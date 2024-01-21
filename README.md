# Git Profile Django Project

## Overview

This Django project allows users to fetch and display GitHub user profiles along with their public repositories. The application utilizes the GitHub REST API to retrieve user information, repository details, and topics.

## Features

- Fetch GitHub user profile by username.
- Display user information, including avatar and a list of public repositories.
- Each repository includes its name, description, topics, and a link to view on GitHub.
- Pagination support for repositories.

## Getting Started

## Prerequisites

- Python (version 3.6 or higher)
- Django (install using `pip install Django`)

### Installation

1. Clone the repository:

   **git clone https://github.com/your-username/git-profile-django.git**
   **cd git-profile-django**
Create a virtual environment:

**python -m venv venv**
Activate the virtual environment:

On Windows:


**.\venv\Scripts\activate**
On macOS/Linux:


**source venv/bin/activate**
Install project dependencies:

**pip install -r requirements.txt**
Apply database migrations:

**python manage.py migrate**
Usage
Run the development server:


python manage.py runserver
Open your web browser and go to http://127.0.0.1:8000/

Enter a GitHub username in the provided form and click "Fetch Profile."

View the user's GitHub profile information along with paginated repositories.

### Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or create a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
