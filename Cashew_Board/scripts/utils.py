import pandas as pd


def android_to_hex(color_code):
    hex_code = "#{:06x}".format(color_code & 0xffffff)
    return hex_code


def validate_csv_df(csv_file: pd.DataFrame) -> bool:
    
    valid_columns = ['account', 'amount','currency', 'title', 'note', 'date', 'income', 'type', 'category name', 'subcategory name', 'color', 'icon', 'emoji', 'budget', 'objective']

    for i in csv_file.columns:
        
        if i in valid_columns:
            validation = True
        else:
            validation = False
            break
        
    return validation