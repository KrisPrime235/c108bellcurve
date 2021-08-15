import pandas as pd
import plotly.figure_factory as pff

data = pd.read_csv("phoneBranddata.csv")
HL = data["Avg Rating"].to_list()
fig = pff.create_distplot([HL],["Bell Curve"], show_hist=False)
fig.show()