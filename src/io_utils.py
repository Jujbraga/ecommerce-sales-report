from pathlib import Path
import pandas as pd

# källhänvisning: https://stackoverflow.com/questions/78466287/
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "ecommerce_sales.csv"

df = pd.read_csv(DATA_PATH)