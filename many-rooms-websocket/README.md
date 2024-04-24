This example is the same red/blue number example as we saw with repeated server queries.
The only difference here is the use of a long-lived two-directional websocket.
The server uses this connection to alert the browser that it needs to update the numbers (because something has changed).

To test this out:
--------------
docker compose build
docker compose up

Then open up two different browser windows:
-------------
http://localhost:5555

When you make a change in one window,
you should be able (eventuallY) to see the update in the other window. 

