# psicoquestions

This project run with Docker and Redis.


# Run app 

-You need docker "https://www.docker.com/"


Ensure you have Docker installed in your system.

-First we build and up the docker-compose whit Redis client 


$ docker-compose up --build  

You should get an output like this:

...
Pulling redis (redis:)...
latest: Pulling from library/redis
c499e6d256d6: Pull complete

...

web_1    |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
web_1    |  * Restarting with stat
web_1    |  * Debugger is active!
web_1    |  * Debugger PIN: 135-673-635


The app run in Flask server. 

