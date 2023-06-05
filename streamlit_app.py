import streamlit as st
import pandas as pd

def get_fruit_list():
  my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
  my_fruit_list = my_fruit_list.set_index("Fruit")
  st.dataframe(my_fruit_list)
  
def main() -> None:
  st.header('Breakfast Favorites')
  st.text('🥣 Omega 3 & Blueberry Oatmeal')
  st.text('🥗 Kale, Spinach & Rocket Smoothie')
  st.text('🐔 Hard-Boiled Free-Range Egg')
  st.text('🥑🍞 Avocado Toast')

  st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
  preselected_fruits = ["Avocado", "Strawberries"]
  st.multiselect("Pick some fruits:", list(my_fruit_list.index), preselected_fruits)
  get_fruit_list()
  
if __name__ == "__main__":
  main()
