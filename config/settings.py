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
    # Umumiy ko‘rinish
    "site_title": "Rozievich Admin",
    "site_header": "Rozievich Portfolio",
    "site_brand": "Rozievich",
    "site_logo": None,
    "site_icon": None,
    "welcome_sign": "Xush kelibsiz, admin panelga!",

    "default_ui_tweaks": {
        "sidebar_nav_small_text": False,
        "accent": "accent-primary",
        "navbar": "navbar-white navbar-light",
        "navbar_fixed": True,
        "layout_boxed": False,
        "footer_fixed": False,
        "sidebar_fixed": True,
        "sidebar": "sidebar-dark-primary",
        "sidebar_nav_small_text": False,
        "sidebar_disable_expand": False,
        "sidebar_nav_child_indent": False,
        "sidebar_nav_compact_style": False,
        "sidebar_nav_legacy_style": False,
        "sidebar_nav_flat_style": True,      # flat ko‘rinish chiroyli
        "theme": "default",                  # yoki darkly, cerulean, cosmo, flatly, journal, litera, lumen, lux, materia, minty, pulse, sandstone, simplex, sketchy, slate, solar, spacelab, superhero, united, yeti
        "dark_mode_theme": "darkly",         # qorong‘i rejim uchun yaxshi tanlov
        "button_classes": {
            "primary": "btn-outline-primary",
            "secondary": "btn-outline-secondary",
            "info": "btn-outline-info",
            "warning": "btn-outline-warning",
            "danger": "btn-outline-danger",
            "success": "btn-outline-success"
        }
    },

    # Top menu (foydali bo‘limlar uchun)
    "topmenu_links": [
        {"name": "📱 Asosiy sayt", "url": "https://dev.rozievich.uz", "new_window": True},
        {"name": "🐙 GitHub", "url": "https://github.com/rozievich", "new_window": True},
        {"name": "📧 Email", "url": "mailto:oybek@rozievich.uz", "new_window": False},
    ],

    # Sidebar menyuni to‘liq sozlash (eng foydali qism)
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],   # keraksiz app'larni yashirish mumkin
    "hide_models": [],


    # Icons – modellarga mos belgi qo‘yish juda muhim!
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "core.skill": "fas fa-tools",
        "core.experience": "fas fa-briefcase",
        "core.portfolio": "fas fa-images",
        "core.message": "fas fa-envelope",
    },

    # Qo'shimcha funksiyalar
    "related_modal_active": True,           # modal oynalar ochilishi
    "show_ui_builder": True,                # live UI sozlash (admin ichida)
    "changeform_format": "horizontal_tabs", # yoki single, vertical_tabs
    "changeform_format_overrides": {
        "core.portfolio": "collapsible", # portfolio uchun alohida ko'rinish
    },

    # Copyright va footer | Rozievich Portfolio
    "copyright": "Oybek © 2025-2026",
    "show_ui_builder": True,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "default",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}
