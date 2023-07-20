import streamlit as st
import requests
import json
import pandas as pd
import re

COMMON_INGREDIENTS = ["Tomato", "Cheese", "Bread", "Butter", "Egg", "Milk", "Onion", "Garlic", "Chicken", "Beef", "Pork", "Salt", "Pepper", "Sugar", "Honey"]

def get_recipes(ingredient_list):
    try:
        url = "http://127.0.0.1:5000/rec"
        data = {"ingredients": ingredient_list}
        data_json = json.dumps(data)
        headers = {'Content-type':'application/json'}

        response = requests.post(url, data=data_json, headers=headers)

        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame.from_dict(data)
            return df.head(10)
        elif response.status_code == 403:
            st.warning("403 ERROR: Please start the API file.")
            return None
        else:
            st.error(f"Error when trying to get recipes: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        st.error("Error occurred while making the request. Please try again later.")
        return None
    except Exception as e:
        st.error("An unexpected error occurred. Please try again later.")
        return None

def main():
    st.set_page_config(
        page_title="PantryPal",
        layout="wide"
    )

    st.title("PantryPal")
    st.markdown("Your personal assistant for recipe recommendations based on your pantry items!")

    st.markdown(
    """
    - Please enter the ingredients you have available.
    - You can separate ingredients by comma, space or newline. For example:\n
    \n
        Tomato
    \n
        Cheese
    \n
        Bread
    \nOR\n
        Tomato, Cheese, Bread
    \nOR\n
        Tomato Cheese Bread
    """)

    col1, col2 = st.columns(2)

    with col1:
        # Let user type in ingredients
        ingredients = st.text_area("Type in list of ingredients:", height=150)

    with col2:
        # Let user select from common ingredients
        selected_ingredients = st.multiselect("Or select from common ingredients:", COMMON_INGREDIENTS)

    ingredient_list = []

    if st.button("Submit"):
        lines = ingredients.split('\n')
        ingredient_list = [item.strip() for line in lines for item in re.split(r'[,\s]\s*', line)]

        ingredient_list = ingredient_list + selected_ingredients

        # Check if any input was provided
        if not ingredient_list:
            st.error("Please enter at least one ingredient.")
            return

        # Check if only white spaces were provided
        if all(not ingredient for ingredient in ingredient_list):
            st.error("Please enter valid ingredient names, not just spaces.")
            return

        # Check if input contains non-text entries or too long words
        for ingredient in ingredient_list:
            if not re.match(r'^[a-zA-Z\s]*$', ingredient):
                st.error("Please use text only for ingredient names (no numbers or special characters).")
                return
            if len(ingredient) > 30:  # max length of an ingredient name is set to 30 characters here
                st.error(f"The ingredient '{ingredient}' is too long. Please enter valid ingredient names.")
                return

    if ingredient_list:
        with st.spinner('Fetching recipes...'):
            recipes = get_recipes(ingredient_list)

        if recipes is not None:
            if recipes.empty:
                st.warning("No matching recipes found.")
            else:
                with st.expander("Ingredients you submitted"):
                    st.write(", ".join(ingredient_list))

                st.markdown("### **Your recipe recommendations:**")
                for i in recipes.index:
                    with st.expander(recipes['recipe_name'][i]):
                        st.write(f"URL: [Recipe Link]({recipes['recipe_urls'][i]})")
                        st.write(f"Ingredients: {recipes['ingredients'][i]}")
                st.success("Fetched recipes successfully!")
        else:
            st.error("An error occurred while fetching recipes.")

if __name__ == "__main__":
    main()
