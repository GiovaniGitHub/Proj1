from pathlib import Path
import sys


BASE_DIR = Path(__file__).resolve().parent.parent

DB_DIR = BASE_DIR / 'db'
sys.path.append(str(BASE_DIR))

