import os

current_path = os.path.dirname(os.path.abspath(__file__))

PROJECT_DIR = os.path.join(current_path, os.pardir)

DATA_DIR = os.path.join(PROJECT_DIR, 'data')
RAW_DATA_DIR = os.path.join(PROJECT_DIR, 'data', 'raw')
INTERIM_DATA_DIR = os.path.join(PROJECT_DIR, 'data', 'interim')
PREPROCESSED_DATA_DIR = os.path.join(PROJECT_DIR, 'data', 'preprocessed')

SRC_DIR = os.path.join(PROJECT_DIR, 'src')

MODELS_DIR = os.path.join(PROJECT_DIR, 'models')
REPORTS_DIR = os.path.join(PROJECT_DIR, 'reports')
