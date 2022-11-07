import pandas as pd
import streamlit as st
import altair as alt
import numpy as np

bbdata = pd.read_csv("bbdatafull.csv")

dukedata = bbdata[bbdata['School'] == 'Duke']

# Give the page a header
st.header(
    'College Basketball Data'
)

# Show the data
st.write(
    bbdata.head()
)

st.sidebar.header("Choose School and Metric")
school_val = st.sidebar.selectbox("Choose Team", bbdata['School'])
y_val = st.sidebar.selectbox("Choose Metric", bbdata.select_dtypes(include=np.number).columns.tolist())


scatter = alt.Chart(bbdata[bbdata['School'] == school_val], title='NCAA Data Over Time').mark_line().encode(
    alt.X('Year'),
    alt.Y(y_val),
    tooltip=[y_val]
).configure_point(
    size=100
)

st.altair_chart(scatter, use_container_width=True)






