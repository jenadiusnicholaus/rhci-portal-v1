#!/usr/bin/env python
"""
Database Configuration Validator
Validates database connection and settings before running the application.
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')
django.setup()

from django.conf import settings
from django.db import connection
from django.core.exceptions import ImproperlyConfigured


def check_database_connection():
    """Test database connection."""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return True, "Database connection successful!"
    except Exception as e:
        return False, f"Database connection failed: {str(e)}"


def check_secret_key():
    """Check if SECRET_KEY is properly configured."""
    secret_key = settings.SECRET_KEY
    if secret_key.startswith('django-insecure'):
        return False, "Warning: Using default insecure SECRET_KEY. Generate a new one for production!"
    return True, "SECRET_KEY is configured."


def check_debug_mode():
    """Check DEBUG setting."""
    debug = settings.DEBUG
    if debug:
        return True, "DEBUG mode is ON (suitable for development)."
    return True, "DEBUG mode is OFF (suitable for production)."


def check_allowed_hosts():
    """Check ALLOWED_HOSTS configuration."""
    allowed_hosts = settings.ALLOWED_HOSTS
    if not allowed_hosts and not settings.DEBUG:
        return False, "ALLOWED_HOSTS is empty. This is required when DEBUG=False."
    return True, f"ALLOWED_HOSTS: {', '.join(allowed_hosts) if allowed_hosts else 'Any (DEBUG mode)'}"


def check_database_config():
    """Display database configuration."""
    db_config = settings.DATABASES['default']
    engine = db_config.get('ENGINE', 'Not set')
    name = db_config.get('NAME', 'Not set')
    
    info = f"Database Engine: {engine}\n"
    info += f"Database Name: {name}"
    
    if 'sqlite' not in engine.lower():
        info += f"\nDatabase User: {db_config.get('USER', 'Not set')}"
        info += f"\nDatabase Host: {db_config.get('HOST', 'Not set')}"
        info += f"\nDatabase Port: {db_config.get('PORT', 'Not set')}"
    
    return True, info


def main():
    """Run all checks."""
    print("=" * 60)
    print("RHCI Portal - Database Configuration Validator")
    print("=" * 60)
    print()
    
    checks = [
        ("SECRET_KEY", check_secret_key),
        ("DEBUG Mode", check_debug_mode),
        ("ALLOWED_HOSTS", check_allowed_hosts),
        ("Database Config", check_database_config),
        ("Database Connection", check_database_connection),
    ]
    
    all_passed = True
    
    for name, check_func in checks:
        print(f"Checking {name}...")
        try:
            passed, message = check_func()
            status = "✅ PASS" if passed else "⚠️  WARNING"
            print(f"{status}: {message}")
            if not passed:
                all_passed = False
        except Exception as e:
            print(f"❌ ERROR: {str(e)}")
            all_passed = False
        print()
    
    print("=" * 60)
    if all_passed:
        print("✅ All checks passed! Your configuration looks good.")
    else:
        print("⚠️  Some checks failed. Please review the warnings above.")
    print("=" * 60)
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
