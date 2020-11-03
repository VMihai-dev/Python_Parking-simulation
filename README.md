# Parking simulation - using Python and Django
This project represents a multiclient-server architecture that runs on your local machine. It simulates a car park (server) with 2 entrances (clients) and 2 exits (clients). 
When a car arrives at the entrance, it will let the server know. In return, the server will tell the car if it is allowed to come in (free parking spaces are available) or if it has 
to wait in a queue. When a car leaves, it will free up a space for an upcoming car or for the cars waiting in the queue. 

# Techlonogies used:
- Python. Used socket and threading to implement the multiclient-server architecture.
- Django. Used Django to create a web application that starts up the server + clients and perfroms the Enter/Exit operations on button clicks. 
- Followed PEP8 guidelines for code redability.
- Git. For version control :) 

# How to use it: 
Clone the project and navigate to `/djangoProject/mysite`. Here you can run the web server application:

    python manage.py runserver

Next, navigate to `localhost:8000` and you should see the server setup page:
<img src="https://i.imgur.com/fQdl82L.png"/>
Click all the buttons in order and if you are not directed to the next page, navigate to `localhost:8000/park`:
<img src="https://i.imgur.com/UQdYaFX.png"/>
And that's all, you can click the Entrance buttons to make a request to enter the car park, or the Exit buttons to free up some spaces.

# Running on local machine without Django: 
You can also run this application from the terminal without using Django. You will just have to start this .py files in order:

    python server.py
    python entrance_client1.py
    python entrance_client2.py
    python exit_client1.py
    python exit_client2.py

After that you will need to send "Enter" command from the entrance clients and "Exit" commands from the exit clients. 
