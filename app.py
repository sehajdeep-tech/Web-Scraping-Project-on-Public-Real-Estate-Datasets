import streamlit as st
import pandas as pd

st.title("Real Estate Dataset Explorer (data.gov)")

@st.cache_data
def load_data():
    return pd.read_csv('datasets.csv')

df = load_data()

search_query = st.text_input("Search datasets by keyword (e.g. tax, zoning):")

if search_query:
    filtered_df = df[df['Title'].str.contains(search_query, case=False) | df['Description'].str.contains(search_query, case=False)]
else:
    filtered_df = df

st.subheader(f" Found {len(filtered_df)} datasets")

for idx, row in filtered_df.iterrows():
    st.markdown(f"### {row['Title']}")
    st.markdown(f"{row['Description']}")
    st.markdown(f"[View Dataset]({row['Link']})")
    st.markdown("---")

st.caption("Only public metadata is used. Always verify dataset license before use.")
