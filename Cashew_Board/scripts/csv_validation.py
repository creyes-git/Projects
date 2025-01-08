import pandas as pd


def validate_csv_df(csv_file: pd.DataFrame) -> bool:
    
    csv_file.columns == ["account", "amount", "currency", "title", "note", "date", "income", "type", "category name", "subcategory name", "color", "icon", "emoji", "budget", "objective"]