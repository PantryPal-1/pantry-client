import streamlit as st
import requests

def get_recipes(ingredient_list):
    # Replace with the actual URL of your Flask API
    # url = "http://127.0.0.1:5000/rec"
    url = "http://localhost:5000/rec"

    # Convert the list of ingredients into a format that can be sent in a GET request
    params = {"ingredients": ','.join(ingredient_list)}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error when trying to get recipes: {response.status_code}")

def main():
    st.title("PantryPal")  # Set the title of the webpage

    # Create a text input box for the user to enter ingredients
    ingredients = st.text_area("Enter the list of ingredients (one per line):")

    # Create a button to submit the ingredients
    if st.button("Submit"):
        # Split the user input into a list of ingredients
        ingredient_list = ingredients.split('\n')
        
        # Get recipe recommendations
        recipes = get_recipes(ingredient_list)

        # Print the list of ingredients back to the user
        st.write("You submitted the following ingredients:")
        for ingredient in ingredient_list:
            st.write(ingredient)

        # Display the recipe recommendations
        if recipes:
            st.write("Here are your recipe recommendations:")
            for recipe in recipes:
                st.write(recipe)

if __name__ == "__main__":
    main()
