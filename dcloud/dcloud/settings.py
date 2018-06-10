import os
from dcloud import aws_conf

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '534f6m=i@*)=q3kuwlge1m3c+@^cabr3ttcx*omv^+dorydjfr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'restful.apps.RestfulConfig',
    'website',
    's3direct',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dcloud.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dcloud.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ko_kr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Login redirect

LOGIN_REDIRECT_URL = '/'

# AWS

# If these are not defined, the EC2 instance profile and IAM role are used.
# This requires you to add boto3 (or botocore, which is a dependency of boto3)
# to your project dependencies.
AWS_ACCESS_KEY_ID = aws_conf.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = aws_conf.AWS_SECRET_ACCESS_KEY

AWS_STORAGE_BUCKET_NAME = aws_conf.AWS_STORAGE_BUCKET_NAME

# The region of your bucket, more info:
# http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region
S3DIRECT_REGION = 'ap-northeast-2'

# Destinations, with the following keys:
#
# key [required] Where to upload the file to, can be either:
#     1. '/' = Upload to root with the original filename.
#     2. 'some/path' = Upload to some/path with the original filename.
#     3. functionName = Pass a function and create your own path/filename.
# key_args [optional] Arguments to be passed to 'key' if it's a function.
# auth [optional] An ACL function to whether the current Django user can perform this action.
# allowed [optional] List of allowed MIME types.
# acl [optional] Give the object another ACL rather than 'public-read'.
# cache_control [optional] Cache control headers, eg 'max-age=2592000'.
# content_disposition [optional] Useful for sending files as attachments.
# bucket [optional] Specify a different bucket for this particular object.
# server_side_encryption [optional] Encryption headers for buckets that require it.

S3DIRECT_DESTINATIONS = {
    'example_destination': {
        # REQUIRED
        'key': '/',

        # OPTIONAL
        #'auth': lambda u: u.is_staff, # Default allow anybody to upload
        #'allowed': ['image/jpeg', 'image/png', 'video/mp4'],  # Default allow all mime types
        #'bucket': 'pdf-bucket', # Default is 'AWS_STORAGE_BUCKET_NAME'
        'acl': 'private', # Defaults to 'public-read'
        'cache_control': 'max-age=2592000', # Default no cache-control
        #'content_disposition': 'attachment',  # Default no content disposition
        #'content_length_range': (5000, 20000000), # Default allow any size
        #'server_side_encryption': 'AES256', # Default no encryption
    },
    'example_other': {
        'key': lambda filename, args: args + '/' + filename,
    	'key_args': 'uploads/images',  # Only if 'key' is a function
    }
}
