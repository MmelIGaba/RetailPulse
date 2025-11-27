import os
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime
from pathlib import Path

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="RetailPulse Pro - Ultimate Retail Analytics",
    page_icon="Shopping Cart",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== PATHS & AUTO DISCOVERY ======================
from pathlib import Path

# app.py is inside /dashboard
APP_DIR = Path(__file__).resolve().parent
BASE_DIR = APP_DIR.parent      # Repo root
PROCESSED_DIR = BASE_DIR / "data" / "processed"

def find_file(patterns):
    if not PROCESSED_DIR.exists():
        return None

    for p in [p.strip() for p in patterns.split("|")]:
        matches = [f for f in PROCESSED_DIR.iterdir()
                   if p.lower() in f.name.lower()]

        if matches:
            return str(matches[0])

    return None
# Auto-discover files


files = {
    "amazon": find_file("Amazon Sale Report"),
    "international": find_file("International sale Report"),
    "may2022": find_file("May-2022"),
    "pl_march": find_file("P L March 2021|PL March"),
    "expense": find_file("Expense IIGF"),
    "warehouse": find_file("Cloud Warehouse Compersion|warehouse"),
    "sale_report": find_file("Sale Report"),
}

@st.cache_data(ttl=3600)
def load(path):
    if not path or not os.path.exists(path):
        return pd.DataFrame()
    for enc in ["utf-8", "latin1", "cp1252", "iso-8859-1"]:
        try:
            return pd.read_csv(path, encoding=enc, low_memory=False)
        except:
            continue
    st.warning(f"Could not read {os.path.basename(path)}")
    return pd.DataFrame()

# Load everything
amazon = load(files["amazon"])
intl   = load(files["international"])
may    = load(files["may2022"])
pl     = load(files["pl_march"])
expense = load(files["expense"])
warehouse = load(files["warehouse"])

# ====================== MERGE SALES DATA ======================
df = pd.DataFrame()
for data, source in [(amazon, "Amazon India"), (intl, "International"), (may, "May-2022")]:
    if not data.empty:
        temp = data.copy()
        temp["Source"] = source
        df = pd.concat([df, temp], ignore_index=True)

if df.empty:
    st.error("No sales data found in data/processed folder!")
    st.stop()

# ====================== SMART COLUMN DETECTION ======================
# Date column — try many possible names
date_candidates = ["Date", "Order Date", "order_date", "date", "OrderDate", "ship-date", "Date "]
date_col = next((col for col in date_candidates if col in df.columns), None)

if date_col:
    df["Date"] = pd.to_datetime(df[date_col], errors="coerce")
else:
    st.warning("No date column found → using dummy dates")
    df["Date"] = pd.date_range("2022-01-01", periods=len(df), freq="D")

# Amount / Sales column
amount_candidates = ["Amount", "Sales", "sales", "Total", "Price", "Amt", "amount"]
amount_col = next((col for col in amount_candidates if col in df.columns), None)
if amount_col:
    df["Sales"] = pd.to_numeric(df[amount_col], errors="coerce").fillna(0)
else:
    df["Sales"] = 0

# Quantity
qty_candidates = ["Qty", "Quantity", "qty", "QTY", "quantity", "Units"]
qty_col = next((col for col in qty_candidates if col in df.columns), None)
if qty_col:
    df["Qty"] = pd.to_numeric(df[qty_col], errors="coerce").fillna(0)
else:
    df["Qty"] = 1

# Category
cat_candidates = ["Category", "category", "Product Category", "item", "Item"]
cat_col = next((col for col in cat_candidates if col in df.columns), None)
if cat_col:
    df["Category"] = df[cat_col]

# State
state_candidates = ["ship-state", "Ship-State", "State", "ship_state", "state"]
state_col = next((col for col in state_candidates if col in df.columns), None)
if state_col:
    df["State"] = df[state_col].str.title()

# Status
status_candidates = ["Status", "status", "order_status", "Order Status"]
status_col = next((col for col in status_candidates if col in df.columns), None)
if status_col:
    df["Status"] = df[status_col]

# Size
if "Size" not in df.columns:
    size_candidates = ["Size", "size", "SIZE"]
    size_col = next((col for col in size_candidates if col in df.columns), None)
    if size_col:
        df["Size"] = df[size_col]

# Revenue = Sales × Qty
df["Revenue"] = df["Sales"] * df["Qty"]

# Final date features
df["Month"] = df["Date"].dt.strftime("%Y-%m")
df["MonthName"] = df["Date"].dt.strftime("%b %Y")

# ====================== SIDEBAR FILTERS ======================
st.sidebar.header("Filters")

# Date range
if df["Date"].notna().any():
    date_range = st.sidebar.slider(
        "Date Range",
        min_value=df["Date"].min().date(),
        max_value=df["Date"].max().date(),
        value=(df["Date"].min().date(), df["Date"].max().date())
    )
    df = df[
        (df["Date"] >= pd.Timestamp(date_range[0])) &
        (df["Date"] <= pd.Timestamp(date_range[1]))
    ]


# Other filters
if "Category" in df.columns:
    cat_filter = st.sidebar.multiselect("Category", options=sorted(df["Category"].dropna().unique()))
    if cat_filter:
        df = df[df["Category"].isin(cat_filter)]

if "State" in df.columns:
    state_filter = st.sidebar.multiselect("State", options=sorted(df["State"].dropna().unique()))
    if state_filter:
        df = df[df["State"].isin(state_filter)]

source_filter = st.sidebar.multiselect("Source", options=df["Source"].unique(), default=df["Source"].unique())
df = df[df["Source"].isin(source_filter)]

# ====================== KPIs ======================
c1, c2, c3, c4, c5 = st.columns(5)
with c1: st.metric("Total Revenue", f"₹{df['Revenue'].sum():,.0f}")
with c2: st.metric("Total Orders", f"{len(df):,}")
with c3: st.metric("Units Sold", f"{df['Qty'].sum():,.0f}")
with c4: st.metric("AOV", f"₹{df['Revenue'].sum()/len(df):,.0f}" if len(df) else 0)
with c5:
    cancelled = len(df[df["Status"].str.contains("Cancel|Return", case=False, na=False)]) if "Status" in df.columns else 0
    st.metric("Cancelled", f"{cancelled:,}")

# ====================== CHARTS (safe versions) ======================
st.markdown("---")
r1 = st.columns(2)
r2 = st.columns(2)

# Monthly trend
with r1[0]:
    st.subheader("Monthly Revenue")
    monthly = df.groupby("MonthName")["Revenue"].sum().reset_index()
    monthly = monthly.sort_values("MonthName")
    fig = px.line(monthly, x="MonthName", y="Revenue", markers=True, title="Revenue Trend")
    st.plotly_chart(fig, use_container_width=True)

# Category sales
with r1[1]:
    st.subheader("Sales by Category")
    if "Category" in df.columns:
        cat = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False).head(10)
        fig = px.bar(cat, color=cat.index, text_auto=True)
        st.plotly_chart(fig, use_container_width=True)

# State map
with r2[0]:
    st.subheader("Sales by State")
    if "State" in df.columns:
        state_sales = df.groupby("State")["Revenue"].sum().reset_index()
        fig = px.choropleth(state_sales, locations="State", locationmode="country names",
                            color="Revenue", scope="asia", color_continuous_scale="Reds")
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)

# Top products
with r2[1]:
    st.subheader("Top 10 Products")
    prod_col = "Style" if "Style" in df.columns else "SKU" if "SKU" in df.columns else None
    if prod_col:
        top = df.groupby(prod_col)["Revenue"].sum().nlargest(10)
        fig = px.bar(top, orientation="h")
        st.plotly_chart(fig, use_container_width=True)

# Download
st.download_button("Download Filtered Data", df.to_csv(index=False), "retailpulse_filtered.csv", "text/csv")

# Raw tabs
st.markdown("---")
tabs = st.tabs(["Amazon", "International", "May-2022", "P&L", "Expense", "Warehouse"])
with tabs[0]: st.dataframe(amazon.head(100), use_container_width=True)
with tabs[1]: st.dataframe(intl.head(100), use_container_width=True)
with tabs[2]: st.dataframe(may.head(100), use_container_width=True)
with tabs[3]: st.dataframe(pl, use_container_width=True)
with tabs[4]: st.dataframe(expense, use_container_width=True)
with tabs[5]: st.dataframe(warehouse, use_container_width=True)

st.success("RetailPulse Pro Dashboard is LIVE!")