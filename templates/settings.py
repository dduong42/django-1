# encoding: utf-8

"""
This file is auto-generated by Ansible, do not modify it.
"""

from project.settings import *

{% if django_database.engine == 'postgres' %}
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ django_database.name }}',
        'USER': '{{ django_database.user }}',
        'PASSWORD': '{{ django_database.password }}',
        'HOST': '',               # Set to empty string for localhost.
        'PORT': '',               # Set to empty string for default.
    }
}
{% endif %}

# Email
{% if django_debug %}
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
{% endif %}

# Debug
DEBUG = {{ django_debug }}

# Security
ALLOWED_HOSTS = ["{{ django_domain }}"]
SECRET_KEY = "{{ secret_key }}"

# Static
STATIC_ROOT = "{{ dir_static }}"
STATIC_URL = "{{ static_url }}"

# Media
MEDIA_ROOT = "{{ dir_media }}"
MEDIA_URL = '{{ media_url }}'