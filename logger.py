from logging import getLogger
from logging.config import dictConfig


def configure_logger(log_path, name='default'):
    dictConfig({
        'version': 1,
        'formatters': {
            'default': {'format': '%(asctime)s - %(levelname)s - %(message)s', 'datefmt': '%Y-%m-%d %H:%M:%S'}
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'stream': 'ext://sys.stdout'
            },
            'file': {
                'level': 'INFO',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'formatter': 'default',
                'when': 'midnight',
                'filename': log_path,
                'backupCount': 5
            }
        },
        'loggers': {
            'default': {
                'level': 'INFO',
                'handlers': ['console', 'file']
            }
        },
        'disable_existing_loggers': False
    })
    return getLogger(name)
