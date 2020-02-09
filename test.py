import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
st.title('My first app - Tien Ta')
st.markdown('today I try to use streamlit for some usecase in my task')
st.write("Here's our first attempt at using data to create a table:")
'''# 1.Write a data frame'''
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
# Draw a title and some text to the app:
'''
# 2.This is the document title

This is some _markdown_.
'''

df = pd.DataFrame({'col1': [1,2,3]})
df  # <-- Draw the dataframe

x = 10
'x', x  # <-- Draw the string 'x' and then the value of 
'''
# 3.Code blocks
st.code renders single-line as well as multi-line code blocks. 
There is also an option to specify the programming language.
'''
st.code("""
@st.cache
def get_data():
    url = "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-09-12/visualisations/listings.csv"
    return pd.read_csv(url)
""", language="python")
st.markdown("_To display a code block, pass in the string to display as code to [`st.code`](https://streamlit.io/docs/api.html#streamlit.code)_.")
'''
Alternatively, using a with st.echo block executes the code within it and also renders it as a code section in the app.
'''
with st.echo():
    st.markdown("Alternatively, use [`st.echo`](https://streamlit.io/docs/api.html#streamlit.echo).")
'''# 4.Add interactivity with widgets
With widgets, Streamlit allows you to bake interactivity directly into your apps with checkboxes, buttons, sliders, and more. 
Check out our API reference(https://docs.streamlit.io/getting_started.html) for a full list of interactive widgets.
'''
st.header('Use checkboxes to show/hide data')
'''
One use case for checkboxes is to hide or show a specific chart or section in an app. st.checkbox() takes a single argument, which is the widget label. In this sample, the checkbox is used to toggle a conditional statement
'''
st.code("""
        @st.cache
        if st.checkbox('Show dataframe'):
        chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
        st.line_chart(chart_data)
        """,language="python")
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)
st.header('Use a selectbox for options')
'''Use st.selectbox to choose from a series. You can write in the options you want, or pass through an array or data frame column.

Let’s use the df data frame we created earlier.'''

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    'Which number do you like best?',
     df['second column'])
'You selected: ', option
st.header('Put widgets in a sidebar')
'''For a cleaner look, you can move your widgets into a sidebar. This keeps your app central, while widgets are pinned to the left. Let’s take a look at how you can use st.sidebar in your app'''
option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option
''' # 5.Show progress 
When adding long running computations to an app, you can use st.progress() to display status in real time.

First, let’s import time. We’re going to use the time.sleep() method to simulate a long running computation:
Now, let’s create a progress bar:
'''
import time
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
'''# 6. Draw some charts

'''
st.header('Draw a line chart')
'''You can easily add a line chart to your app with st.line_chart(). We’ll generate a random sample using Numpy and then chart it.'''
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.header('Plot a map')
'''With st.map() you can display data points on a map. Let’s use Numpy to generate some sample data and plot it on a map of San Francisco.'''
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)