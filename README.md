
# VOT Web App 

This is a simple web application made with python Flask framework using SQLite database and deploying it with Docker.
The app takes user input from an input box and when a button for adding an item is clicked the user input is stored to the database and then is displayed in a list below the input box paired with a delete button which deletes the selected item from the database and the site. 




## How to deploy the app

1. Download the project files on a linux machine
2. Change the directory to where you downloaded the files
3. Install docker and docker compose if you don't have them
4. Run __docker-compose build__ command
5. Run __docker-compose up__ command
6. Open your browser and open the site with http://127.0.0.1:5000 url
7. (Optional) If you want to visualize the database you can download sqlitebrowser or DBeaver and open the database file which is located in the working directory /instance/VOT_Proekt.db
