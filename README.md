
Git Profile Django Project
Overview
This Django project allows users to fetch and display GitHub user profiles along with their public repositories. The application utilizes the GitHub REST API to retrieve user information, repository details, and topics.

Features:
Fetch GitHub user profile by username.
Display user information, including avatar and a list of public repositories.
Each repository includes its name, description, topics, and a link to view on GitHub.
Pagination support for repositories.
Getting Started
Prerequisites
Python (version 3.6 or higher)
Django (install using pip install Django)
Installation
Clone the repository:

bash
git clone https://github.com/your-username/git-profile-django.git
cd git-profile-django

Create a virtual environment:
bash
python -m venv venv
Activate the virtual environment:

On Windows:
bash
.\venv\Scripts\activate

On macOS/Linux:
bash
source venv/bin/activate

Install project dependencies:
bash
pip install -r requirements.txt
Apply database migrations:

bash
python manage.py migrate
Usage
Run the development server:

bash
python manage.py runserver

Open your web browser and go to http://127.0.0.1:8000/

Enter a GitHub username in the provided form and click "Fetch Profile."

View the user's GitHub profile information along with paginated repositories.


