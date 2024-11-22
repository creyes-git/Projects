import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go


def plot_pie_categories(df):
    
    df = df[df["income"] == False] # Keeps only expenses
    df["category name"] = df.apply(lambda row: row["category name"] if row["subcategory name"] == "" else row["subcategory name"], axis = 1) # Keep subcategory if not empty
    df = df[["category name", "amount", "color"]].groupby(["category name"]).agg({"amount": "sum", "color": "first"}).reset_index() # Group by category name and sum amount
    
    fig = go.Figure(layout = go.Layout(height = 500, width = 500))
    fig.add_trace(go.Pie(labels = df["category name"],
                         values = df["amount"],
                         hoverinfo = "value+percent",
                         hovertemplate = "$%{value} = %{percent} <extra></extra>",
                         hoverlabel = dict(font_size = 15),
                         textinfo = "label",
                         textposition = "inside",
                         insidetextorientation = "radial",
                         insidetextfont = dict(color = "black"),
                         showlegend = False,
                         hole = 0.4,
                         marker = dict(colors = df["color"],)))
    
    return fig


def plot_hist_income_expense(df):
    
    df["date"] = df["date"].dt.strftime("%Y-%m") # Format date to keep only year and month
    df_income = df[df["income"] == True] # Keeps only incomes
    df_expense = df[df["income"] == False] # Keeps only expenses
    df_income = df_income[["amount", "date"]].groupby(["date"]).agg({"amount": "sum"}).reset_index() # Group by date and sum amount
    df_expense = df_expense[["amount", "date"]].groupby(["date"]).agg({"amount": "sum"}).reset_index()
    
    fig = go.Figure(layout = go.Layout(height = 500, width = 1500)).update_layout(title = "Monthly Income-Expenses Evolution")
    
    fig.add_trace(go.Bar(x = df_income["date"],
                         y = df_income["amount"],
                         hoverinfo = "y",
                         hovertemplate = "Income: $%{y} <extra></extra>",
                         hoverlabel = dict(font_size = 15),
                         showlegend = False,
                         marker_color = "#4caf50")) # Income Trace
    
    fig.add_trace(go.Bar(x = df_expense["date"],
                         y = df_expense["amount"],
                         hoverinfo = "y",
                         hovertemplate = "Expense: $%{y} <extra></extra>",
                         hoverlabel = dict(font_size = 15),
                         showlegend = False,
                         marker_color = "#ff7043")) # Expense Trace
    
    fig.add_trace(go.Line(x = df_income["date"],
                          y = df_income["amount"] - df_expense["amount"],
                          hoverinfo = "y",
                          hovertemplate = "Saving: $%{y} <extra></extra>",
                          hoverlabel = dict(font_size = 15),
                          showlegend = False,
                          line_color = "#FFBE04")) # Saving Trace
    
    return fig


def plot_saving_rate(df):
    
    df = df[["income", "amount"]].groupby(["income"]).agg({"amount": "sum"}).reset_index() # Group by type and sum amount
    df["income"] = df["income"].replace({True: "Income", False: "Expense"})
    
    fig = go.Figure(layout = go.Layout(height = 500, width = 500))
    
    fig.add_trace(go.Pie(labels = df["income"],
                         values = df["amount"],
                         hovertemplate = "%{label}: $%{value} <extra></extra>",
                         hoverlabel = dict(font_size = 15),
                         showlegend = False,
                         hole = 0.4,
                         marker = dict(colors = ["#ff7043", "#4caf50"])))
    
    fig.add_annotation(x = 0.5, 
                       y = 1.25,
                       text = f"Savings Rate: {round(((df['amount'][1] - df['amount'][0]) / df['amount'][1]) * 100, 2)} %",
                       showarrow = False, 
                       font = dict(size = 16, color = 'black'))

    return fig