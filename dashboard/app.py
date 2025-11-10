try:
	import streamlit as st
except Exception:
	class _DummyST:
		def title(self, *args, **kwargs):
			print("TITLE:", *args)
		def plotly_chart(self, *args, **kwargs):
			print("PLOTLY CHART:", args[0] if args else None)
		def warning(self, *args, **kwargs):
			print("WARNING:", *args)
		def bar_chart(self, *args, **kwargs):
			print("BAR CHART:", args[0] if args else None)
		def dataframe(self, *args, **kwargs):
			if args and hasattr(args[0], "head"):
				print("DATAFRAME PREVIEW:")
				print(args[0].head())
			else:
				print("DATAFRAME:", args[0] if args else None)
	st = _DummyST()

import pandas as pd

try:
	import plotly.express as px
except Exception:
	px = None

st.title("RetailPulse Dashboard")

sales_df = pd.read_csv("data/processed/sales_data.csv")

# Plot sales by category (use Plotly if available, otherwise fallback to Streamlit)
if px is not None:
	fig = px.bar(sales_df, x="category", y="sales", title="Sales by Category")
	st.plotly_chart(fig)
else:
	st.warning("plotly.express is not installed; falling back to Streamlit charts. Install with: pip install plotly")
	grouped = sales_df.groupby("category", as_index=False)["sales"].sum()
	st.bar_chart(grouped.set_index("category")["sales"])

# Load processed data
df = pd.read_csv("etl/processed/retailpulse.csv")

# Display preview
st.dataframe(df)
