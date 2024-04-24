This is similar to the code in websocket-example.
However, in this version, there are 10 different rooms.
Each room has its own Blue Number and Red Number
When a number changes, the server uses websockets to notify everyone in the particular room

To test this out:
--------------
docker compose build
docker compose up

Then open up several different browser windows:
-------------
http://localhost:9990



