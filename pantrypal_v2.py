import streamlit as st
import requests
import json
import pandas as pd

def get_recipes(ingredient_list):
    # Replace with the actual URL of your Flask API
    url = "http://127.0.0.1:5000/rec"
    # Prepare the data in the required format
    data = {"ingredients": ingredient_list}
    # Convert dict to json
    data_json = json.dumps(data)
    headers = {'Content-type':'application/json'}

    response = requests.post(url, data=data_json, headers=headers)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame.from_dict(data)
        df.head()
        # print(response.json())
        return df.head()
    else:
        st.error(f"Error when trying to get recipes: {response.status_code}")

def main():
    st.title("PantryPal")  # Set the title of the webpage

    # Create a text input box for the user to enter ingredients
    ingredients = st.text_area("Enter the list of ingredients (one per line):")
    ingredient_list = []

    # Create a button to submit the ingredients
    if st.button("Submit"):
        # Split the user input into a list of ingredients
        ingredient_list = ingredients.split('\n')
        
    # Get recipe recommendations
    if (ingredient_list):
        recipes = get_recipes(ingredient_list)
        # Print the list of ingredients back to the user
        st.write("You submitted the following ingredients:")
        for ingredient in ingredient_list:
            st.write(ingredient)

        # Display the recipe recommendations
        st.write("Here are your recipe recommendations:")
        for i in recipes.index:
            # print(recipes['recipe_urls'][ind], recipes['recipe_name'][ind])
            st.write(recipes['recipe_urls'][i], recipes['recipe_name'][i], recipes['ingredients'][i])

if __name__ == "__main__":
    main()
