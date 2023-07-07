import streamlit as st

def main():
    st.title("PantryPal")  # Set the title of the webpage

    # Create a text input box for the user to enter ingredients
    ingredients = st.text_area("Enter the list of ingredients (one per line):")

    # Create a button to submit the ingredients
    if st.button("Submit"):
        # Split the user input into a list of ingredients
        ingredient_list = ingredients.split('\n')
        
        # Print the list of ingredients back to the user
        st.write("You submitted the following ingredients:")
        for ingredient in ingredient_list:
            st.write(ingredient)

if __name__ == "__main__":
    main()
