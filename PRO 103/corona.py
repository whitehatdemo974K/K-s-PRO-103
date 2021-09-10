import pandas as pd
import plotly.express as px
df=pd.read_csv("Copy+of+data+-+data (1).csv")
fig=px.scatter(df,x="date",y="cases",color="country",title="INCOME",size_max=5)
fig.show()