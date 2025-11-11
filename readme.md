# RHCI Portal V1

Django web application for RHCI Portal.

## Prerequisites

- Python 3.8 or higher
- PostgreSQL (optional, SQLite is used by default)
- pip package manager

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd rhci-portal-v1
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the example environment file and update it with your settings:

```bash
cp .env.example .env
```

Edit `.env` file with your configuration:
- Generate a new `SECRET_KEY` for production
- Update database credentials if using PostgreSQL
- Configure email settings if needed

### 5. Database Setup

#### Option A: Using SQLite (Default - No additional setup needed)

The project is configured to use SQLite by default. Just run migrations:

```bash
python manage.py migrate
```

#### Option B: Using PostgreSQL

1. Create a PostgreSQL database:
```bash
createdb rhci_portal_db
```

2. Update `.env` file with PostgreSQL settings:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=rhci_portal_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

3. Run migrations:
```bash
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

Admin panel: `http://127.0.0.1:8000/admin/`

## Important Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key for cryptographic signing | Required |
| `DEBUG` | Enable/disable debug mode | True |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts | localhost,127.0.0.1 |
| `DB_ENGINE` | Database engine | django.db.backends.sqlite3 |
| `DB_NAME` | Database name | db.sqlite3 |
| `DB_USER` | Database user | - |
| `DB_PASSWORD` | Database password | - |
| `DB_HOST` | Database host | localhost |
| `DB_PORT` | Database port | 5432 |
| `EMAIL_HOST` | SMTP server host | smtp.gmail.com |
| `EMAIL_PORT` | SMTP server port | 587 |
| `EMAIL_HOST_USER` | Email account username | - |
| `EMAIL_HOST_PASSWORD` | Email account password | - |
| `TIME_ZONE` | Application timezone | UTC |

## Project Structure

```
rhci-portal-v1/
├── manage.py           # Django management script
├── settings/           # Django settings package
│   ├── __init__.py
│   ├── settings.py     # Main settings file
│   ├── urls.py         # URL configuration
│   ├── wsgi.py         # WSGI configuration
│   └── asgi.py         # ASGI configuration
├── .env                # Environment variables (not in git)
├── .env.example        # Example environment variables
├── requirements.txt    # Python dependencies
└── readme.md          # This file
```

## Useful Commands

```bash
# Create new Django app
python manage.py startapp app_name

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Run tests
pytest

# Create superuser
python manage.py createsuperuser

# Shell with Django context
python manage.py shell
```

## Production Deployment

For production deployment:

1. Set `DEBUG=False` in `.env`
2. Generate a new strong `SECRET_KEY`
3. Update `ALLOWED_HOSTS` with your domain
4. Set security settings to True:
   - `CSRF_COOKIE_SECURE=True`
   - `SESSION_COOKIE_SECURE=True`
   - `SECURE_SSL_REDIRECT=True`
   - `SECURE_HSTS_SECONDS=31536000`
5. Use PostgreSQL or MySQL instead of SQLite
6. Configure proper email backend
7. Use a production server like Gunicorn
8. Set up a reverse proxy (Nginx/Apache)
9. Configure SSL certificates

## License

[Add your license information here]

## Contributors

[Add contributor information here]
