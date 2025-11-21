# GCTF2017-Scoreboard updated for FIRSTCON25

![Final Results Screenshot](screenshots/results.png)

## Setup

* Requires CTFd platform, Python3 and virtualenv
* Modify "app.py"'s BASEURL to your CTFd platform's URL
* Modify "templates/scoreboard.html"'s `var deadline` to the date of the end of your CTF
* `virtualenv -p /usr/bin/python3 env`
* `source env/bin/activate`
* `pip install -r requirements.txt`
* `python app.py`
* Visit "http://localhost:8080"

## Docker setup

* Build the container
````
sudo docker build -t scoreboard .
````

* Run the container in background
````
sudo docker run -p 8888:80 -d scoreboard
````
