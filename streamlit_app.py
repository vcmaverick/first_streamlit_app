import streamlit
streamlit.title('New diner')

streamlit.header('🍞Breakfast menu')
streamlit.text('🥣Bluberry oatmeal')
streamlit.text('🥑Avacado toast')
streamlit.text('🥗Scrambled eggs')
streamlit.text('🍇smoothies')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe('my_fruit_list')

