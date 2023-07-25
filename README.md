# pantry-client

PantryPal - Your Personal Recipe Assistant

PantryPal is a web application that helps you find delicious recipes based on the ingredients you have available in your pantry. Whether you're looking for vegetarian or nut-free recipes, PantryPal has got you covered. Say goodbye to recipe books and endless searches, and let PantryPal do the work for you!


Features:

Input your list of ingredients, separated by commas, spaces, or newlines.

Choose the number of recipes you want to see.

Filter recipes by dietary preferences: No filter, Vegetarian, or Nut-free.

Get instant recipe recommendations based on your pantry items.


How to Use:

1.) Clone the repository to your local machine.

2.) Ensure you have Python installed (version 3.6 or above).

3.) Install the required packages by running pip install -r requirements.txt inside the pantry-server directory.

4.) Start the API server by running flask run in your terminal or command prompt in the pantry-server directory. The API server will listen on http://127.0.0.1:5000/, or you can specify the port by adding the flag -p <port number>.

5.) In a new terminal or command prompt, run streamlit run pantrypal.py from the pantry-client directory to launch the PantryPal web application.
The PantryPal web application will open in your default web browser. Follow the instructions provided on the page.
