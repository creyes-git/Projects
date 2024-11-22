import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go


def plot_pie_categories(df):
    """This function takes a pandas DataFrame as argument and generates a pie chart based on the categorical distribution of the 'amount' column.
    
    Parameters
    ----------
    df : pandas DataFrame
        The DataFrame should contain the columns 'category name', 'amount', and 'color'.
    
    Returns
    -------
    fig : plotly.graph_objs.Figure
        The pie chart figure."""
    
    df = df[df["income"] == False] # Keeps only expenses
    df['amount'] = df['amount'].abs() # Transform negative values to positive
    df["category name"] = df.apply(lambda row: row["category name"] if row["subcategory name"] == "" else row["subcategory name"], axis = 1) # Keep subcategory if not empty
    df = df[["category name", "amount", "color"]].groupby(["category name"]).agg({"amount": "sum", "color": "first"}).reset_index() # Group by category name and sum amount
    
    fig = go.Figure(layout = go.Layout(height = 500, width = 500))
    fig.add_trace(go.Pie(labels = df["category name"],
                         values = df["amount"],
                         hoverinfo = "value+percent",
                         #hovertemplate = "<extra>$%{value}</extra> : %{percent}</extra>",
                         hoverlabel = dict(font_size = 15),
                         textinfo = "label",
                         textposition = "inside",
                         insidetextorientation = "radial",
                         insidetextfont = dict(color = "black"),
                         showlegend = False,
                         hole = 0.4,
                         marker = dict(colors = df["color"],)))
    
    return fig