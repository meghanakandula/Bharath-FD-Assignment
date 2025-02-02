# Bharath-FD-Assignment

This Django project implements a **Multilingual FAQ System** with **WYSIWYG** editor support, **API endpoints** for FAQ management, **Redis caching**, and **Google Translate API** integration for automatic translations. It supports multiple languages and allows seamless language switching for FAQ retrieval via API.

## Features

- **Multilingual Support**: FAQ content is available in multiple languages (English, Hindi, Bengali, Telugu, Tamil, Malayalam, Kannada).
- **WYSIWYG Editor**: Rich text editor for FAQ answers (using `django-ckeditor`).
- **Automatic Translation**: Translates FAQ questions and answers using **Google Translate** API during object creation.
- **Caching**: Caching with **Redis** for faster API responses.
- **REST API**: Endpoints for managing and retrieving FAQs with language support.
- **Django Admin**: Admin panel to manage FAQs and their translations easily.

## Installation

### Prerequisites

- Python 3.x
- Django 5.x
- Redis server (for caching)

### Step-by-Step Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AwkwardlyProfessional/multilingual_FAQ.git
    cd multilingual_faq
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the Redis server. If you're using Docker, you can run Redis using:

    ```bash
    docker-compose up -d
    ```

5. Apply migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser for Django Admin:

    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

Now you can access the project at `http://localhost:8000`.

## API Usage

The system exposes a **REST API** to manage and retrieve FAQs.

### Endpoints

1. **GET /api/faqs/**: Get a list of FAQs.
    - Example: `curl http://localhost:8000/api/faqs/`
    - Supports language selection with the `?lang=<language_code>` query parameter.

    **Example Requests:**
    ```bash
    # Fetch FAQs in English (default)
    curl http://localhost:8000/api/faqs/

    # Fetch FAQs in Hindi
    curl http://localhost:8000/api/faqs/?lang=hi

    # Fetch FAQs in Bengali
    curl http://localhost:8000/api/faqs/?lang=bn
    ```

### Caching

The API uses **Redis** for caching FAQ translations. By default, the cache is stored in `redis://127.0.0.1:6379/1`.

## Admin Panel

You can access the Django admin panel at `http://localhost:8000/admin/`.
- Login with the superuser credentials you created earlier.
- Manage FAQs and their translations.

## Project Structure
```
multilingual_faq/
│── faq_project/                 
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│
│── faqs/                         
│   ├── migrations/               # Database migrations
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── tests.py
│   └── utils.py
│
│── requirements.txt
│── manage.py
│── README.md
│── Dockerfile
│── docker-compose.yml
│── .gitignore
```

## Docker Support

This project comes with a `Dockerfile` and `docker-compose.yml` file for containerized deployment.

### Running with Docker

1. Build and run the containers:

    ```bash
    docker-compose up --build
    ```

2. The application will be available at `http://localhost:8000`.

## Tests

To run tests, make sure to activate your virtual environment and run:

```bash
pytest
```

Unit Tests

Unit tests are included to test:
	•	Model methods (for translation and caching).
	•	API responses (ensure that the FAQ data is correctly returned in different languages).

Git Commit Messages

Follow conventional commit message practices:
	•	feat: Add multilingual FAQ model
	•	fix: Improve translation caching
	•	docs: Update README with API examples

Ensure atomic commits with clear commit messages.

Contributing
	1.	Fork the repository.
	2.	Create a new branch: git checkout -b feature-name.
	3.	Make your changes and commit them: git commit -m 'feat: Add feature'.
	4.	Push to your forked repository: git push origin feature-name.
	5.	Create a pull request from your fork to this repository.

License

This project is licensed under the MIT License - see the LICENSE file for details.
