from taipy.gui import Gui, notify
import taipy.gui.builder as tgb
import pandas as pd
from datetime import datetime, date


with tgb.Page() as page:
    tgb.toggle(theme=True)

    tgb.dialog(
        "{show_dialog}",
        partial="{partial}",
        title="Forecast Data",
        on_action=lambda state: state.assign("show_dialog", False),
    )

    tgb.toggle(theme=True)

    with tgb.part("header sticky"):
        with tgb.layout(
            "100px 1",
            columns__mobile="100px 1",
            class_name="header-content",
        ):
            tgb.image("favicon.png", width="50px")
            tgb.text("#### Stock **Visualization**", mode="md")

    tgb.html("br")
    with tgb.part("container"):
        with tgb.layout("1 1 1", gap="40px", class_name="card"):
            with tgb.part():
                tgb.text("#### Selected **Period**", mode="md")
                tgb.text("From:", mode="md")
                tgb.date(
                    "{start_date}",
                    class_name="fullwidth",
                )
                tgb.text("To:", mode="md")
                tgb.date(
                    "{end_date}",
                    class_name="fullwidth",
                )
            with tgb.part():
                tgb.text("#### Selected **Ticker**", mode="md")
                tgb.text(
                    "You can choose any ticker referenced by YFinance.", mode="md"
                )
                tgb.input(
                    value="{selected_stock}",
                    label="Write a ticker here and press Enter",
                    change_delay=-1,
                    class_name="fullwidth",
                )

                tgb.text("Or choose a popular one", mode="md")
                lov = [
                    "MSFT",
                    "GOOG",
                    "AAPL",
                    "AMZN",
                ]
                
            with tgb.part():
                tgb.text("#### Prediction **years**", mode="md")
                tgb.text(
                    "Select number of prediction **years**: {n_years}", mode="md"
                )
                tgb.slider("{n_years}", min=1, max=5)

                tgb.text(
                    "Clicking the button will train a **model**.",
                    mode="md",
                )

        tgb.html("br")

        with tgb.expandable(title="Historical Data", expanded=False):
            with tgb.layout("1 1"):
                with tgb.part():
                    tgb.text("### Historical **Closing** price", mode="md")
                    tgb.chart(
                        "{data}", mode="line", x="Date", y__1="Open", y__2="Close")

                with tgb.part():
                    tgb.text("### Historical **Daily** Trading Volume", mode="md")
                    tgb.chart("{data}", mode="line", x="Date", y="Volume")

            tgb.text("### **Whole** Historical Data {selected_stock}", mode="md")
            tgb.table("{data}")

        tgb.text("### **Forecast** Data", mode="md")

        tgb.chart("{forecast}", mode="line", x="Date", y__1="Lower", y__2="Upper")

        tgb.html("br")

        with tgb.part("text-center"):
            tgb.button(
                "More info", on_action=lambda s: s.assign("show_dialog", True))


# Run Taipy GUI
app = Gui(page)
partial = app.add_partial("<|{forecast}|table|>")
app.run(dark_mode = True, title = "OpenBB Stocks Screener", margin = "0px")

