import os


PROD_FORMATTER_SETTINGS = {
    'standard': {
        'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
        'datefmt': "%d/%b/%Y %H:%M:%S"
    },
}

PROD_LOGGER_SETTINGS = {
    # 'flask': {
    #     'handlers': ['console', 'info_file', 'debug_file'],
    #     'propagate': True,
    #     'level': 'INFO',
    # },
    # 'debug': {
    #     'handlers': ['console', 'error_file', 'debug_file'],
    #     'level': 'ERROR',
    #     'propagate': True,
    # },
    '': {
        'handlers': ['console', 'error_file', 'critical_file', 'info_file', 'warning_file'],
        # 'level': 'DEBUG',
        'propagate': True,
    },
    # 'gunicorn.error': {
    #     'level': 'ERROR',
    #     'handlers': ['error_file', 'debug_file'],
    #     'propagate': True,
    # },
    # 'gunicorn.access': {
    #     'level': 'ERROR',
    #     'handlers': ['info_file', 'debug_file'],
    #     'propagate': False,
    # },
}


def handler_settings(LOG_ROOT, size, backup_count):
    settings = {
        'info_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_ROOT, "info.log"),
            'maxBytes': int(1024 * 1024 * float(size)),  # File size in MB
            'backupCount': int(backup_count),
            'formatter': 'standard',
        },
        'warning_file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_ROOT, "warning.log"),
            'maxBytes': int(1024 * 1024 * float(size)),  # File size in MB
            'backupCount': int(backup_count),
            'formatter': 'standard',
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_ROOT, "error.log"),
            'maxBytes': int(1024 * 1024 * float(size)),  # File size in MB
            'backupCount': int(backup_count),
            'formatter': 'standard',
        },
        'critical_file': {
            'level': 'CRITICAL',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_ROOT, "critical.log"),
            'maxBytes': int(1024 * 1024 * float(size)),  # File size in MB
            'backupCount': int(backup_count),
            'formatter': 'standard',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    }
    return settings


def get_log_settings(LOG_ROOT, setting='production', size=5, backup_count=2):
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,

        # How to format the output
        'formatters': PROD_FORMATTER_SETTINGS,

        # Log handlers (where to go)
        'handlers': handler_settings(LOG_ROOT, size, backup_count),

        # Loggers (where does the log come from)
        'loggers': PROD_LOGGER_SETTINGS
    }
    return LOGGING
