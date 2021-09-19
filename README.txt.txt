To install all required packages:

$ pip install -r requirements.txt

Before starting the server for the first time, run:

$ python manage.py read

This command collects the data from the CSV files provided. This needs only be done once during the first running of the server.

To run the server:

$ python manage.py runserver



Website layout:

'/home' contains the cities as clickable links. With that you can navigate to the specific webpage and view the hotels in each city as needed.

'/name' where name is the name of the city desired contains the hotels from each city and is accessible from the home page.

'/admin' contains the admin login. User: maykin_media, Pass: maykin123. Creating a city with hotels here will add the city to the sidebar
on the main page (Typically I would not leave the admin login on the website, however this is only a test so it does not matter)