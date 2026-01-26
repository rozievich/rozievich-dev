import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ["*"]


# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps
    'rest_framework',
    'corsheaders',
    # Local apps
    'core.apps.CoreConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '15/min',
        'user': '120/min'
    }
}

# CORS Settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://dev.rozievich.uz",
    "https://dev.rozievich.uz",
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
CORS_ALLOW_METHODS = [
    'GET',
    'OPTIONS',
    'POST',
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    # ===== Branding =====
    "site_title": "rozievich Portfolio",
    "site_header": "Portfolio Admin Panel",
    "site_brand": "rozievich",
    "site_logo": None,
    "site_icon": None,
    "welcome_sign": "Xush kelibsiz, rozievich Admin Panelga!",
    "copyright": "Oybek Rozievich © 2025-2026",
    
    # ===== Top Menu =====
    "topmenu_links": [
        {"name": "🏠 Dashboard", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "📱 Website", "url": "https://dev.rozievich.uz", "new_window": True},
        {"name": "🐙 GitHub", "url": "https://github.com/rozievich", "new_window": True},
        {"name": "📧 Email", "url": "mailto:oybekrozievich@gmail.com", "new_window": True},
    ],

    # ===== Search Settings =====
    "search_model": [
        "core.Skill",
        "core.Experience",
        "core.Portfolio",
        "core.Message",
    ],

    # ===== Icons for Models =====
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "core.skill": "fas fa-tools",
        "core.experience": "fas fa-briefcase",
        "core.portfolio": "fas fa-images",
        "core.message": "fas fa-envelope",
    },

    # ===== Sidebar Settings =====
    "show_sidebar": True,
    "navigation_expanded": True,
    "show_search": True,
    "show_recent": True,
    "sidebar_nav_compact_style": False,
    
    # ===== UI Builder & Features =====
    "show_ui_builder": True,
    "related_modal_active": True,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "core.experience": "vertical_tabs",
        "core.portfolio": "collapsible",
    },

    # ===== Custom Links (optional) =====
    "custom_links": {
        "core": [
            {
                "name": "📊 Analytics",
                "url": "admin:index",
                "icon": "fas fa-chart-bar",
                "permissions": ["auth.view_user"]
            }
        ]
    },

    # ===== Order Models =====
    "order_with_respect_to": [
        "core.Skill",
        "core.Experience",
        "core.Portfolio",
        "core.Message",
    ],

    # ===== Hide Models =====
    "hide_models": ["auth.group"],

    # ===== Show Admin Object Tools =====
    "show_admin_object_tools": True,
}


JAZZMIN_UI_TWEAKS = {
    # ===== Theme Settings =====
    "theme": "lux",                          # Modern & elegant theme
    "navbar": "navbar-white navbar-light",
    "sidebar": "sidebar-dark-primary",
    "brand_colour": "navbar-primary",
    "accent": "accent-primary",

    # ===== Text Sizes =====
    "navbar_small_text": False,
    "sidebar_nav_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "footer_small_text": False,

    # ===== Layout Settings =====
    "layout_boxed": False,
    "footer_fixed": False,
    "navbar_fixed": True,
    "sidebar_fixed": True,
    "sidebar_nav_child_indent": True,

    # ===== Sidebar Navigation =====
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "sidebar_disable_expand": False,

    # ===== Additional Options =====
    "theme_switch": True,                    # Allow dark/light mode toggle
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    }
}
