import pandas as pd 
import plotly.graph_objects as go
#import webcolors
import os


data_folder = r"/workspaces/Projects/Cashew_Board/data"
file_on_folder = os.listdir(data_folder)[0]


def android_to_hex(color_code):
    hex_code = "#{:06x}".format(color_code & 0xffffff)
    return hex_code


df = pd.read_csv(fr"{data_folder}/{file_on_folder}", engine = "pyarrow", keep_default_na = False)
df["color"] = df["color"].apply(android_to_hex)


def plot_pie_categories(df):
    
    """Plot a pie chart of the categories of expenses in a given dataframe.

    Parameters
    ----------
    df : pandas dataframe
        The dataframe containing the expenses to be plotted.

    Returns
    -------
    fig : plotly.graph_objects.Figure
        The pie chart figure."""
        
    df = df[df["income"] == False] # Keeps only expenses
    df['amount'] = df['amount'].abs() # Transform negative values to positive
    df["category name"] = df.apply(lambda row: row["category name"] if row["subcategory name"] == "" else row["subcategory name"], axis = 1) # Keep subcategory if not empty
    df = df[["category name", "amount", "color"]].groupby(["category name"]).agg({"amount": "sum", "color": "first"}).reset_index() # Group by category name and sum amount
    
    fig = go.Figure(layout = go.Layout(height = 500, width = 500))
    fig.add_trace(go.Pie(labels = df["category name"],
                         values = df["amount"],
                         hoverinfo = "label+value+percent",
                         textinfo = "label+value",
                         textposition = "inside",
                         showlegend = False,
                         marker = dict(colors = df["color"],)))
    
    return fig

plot_pie_categories(df)