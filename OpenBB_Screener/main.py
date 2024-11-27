from taipy.gui import Gui, notify
import taipy.gui.builder as tgb
import pandas as pd
from datetime import datetime, date


with tgb.Page() as page:
    tgb.toggle(theme=True)

    tgb.text("OpenBB Stocks Screener")


# Run Taipy GUI
app = Gui(page)
partial = app.add_partial("<|{forecast}|table|>")
app.run(dark_mode = True, title = "OpenBB Stocks Screener", margin = "0px")

