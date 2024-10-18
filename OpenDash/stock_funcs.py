from openbb import obb
import pandas as pd


def get_index_symbols():
    """
    Get the list of available index symbols from Yahoo Finance.
    
    Returns
    -------
    index_symbols : pandas.Series
        A pandas Series of index symbols available from Yahoo Finance.
    """
    index_symbols = obb.index.available(provider = "yfinance").to_dataframe()["name"]

    return index_symbols


def get_index_hprice(symbol):
    """
    Get the historical price of a given index symbol.

    Parameters
    ----------
    symbol : str
        The symbol of the index.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the historical price of the index.
     """
    index_price = obb.index.price.historical(symbol, provider = "yfinance", start_date = "2014-01-01").to_dataframe()["close"]
    
    return index_price