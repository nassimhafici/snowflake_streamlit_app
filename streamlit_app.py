import streamlit as st
import snowflake.connector
import pandas as pd
import requests


def get_fruit_list():
    fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
    fruit_list = fruit_list.set_index("Fruit")
    return fruit_list


def get_multiselect_fruit_list(fruit_list):
    preselected_fruits = ["Avocado", "Strawberries"]
    return st.multiselect("Pick some fruits:", list(fruit_list.index), preselected_fruits)


def main() -> None:
    st.header('Breakfast Favorites')
    st.text('🥣 Omega 3 & Blueberry Oatmeal')
    st.text('🥗 Kale, Spinach & Rocket Smoothie')
    st.text('🐔 Hard-Boiled Free-Range Egg')
    st.text('🥑🍞 Avocado Toast')

    st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

    my_fruit_list = get_fruit_list()
    fruits_selected = get_multiselect_fruit_list(my_fruit_list)
    fruits_to_show = my_fruit_list.loc[fruits_selected]
    st.dataframe(fruits_to_show)
    
    # New Section to display fruityvice api response
    st.header("Fruityvice Fruit Advice!")
    fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
    st.write('The user entered ', fruit_choice)
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    
    # take the json version of the response and normalize it
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    # output the screen as a table
    st.dataframe(fruityvice_normalized)



if __name__ == "__main__":
    main()
