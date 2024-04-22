This is an example of using Javascript to repeatedly query a server for updates.

To test this out:
--------------
docker compose build
docker compose up

Then open up two different browser windows:
-------------
http://localhost:5555

When you make a change in one window,
you should be able (eventuallY) to see the update in the other window. 

By looking at the Javascript,
You can see that the update is being called every 10 seconds
This is intentionally slow, but you can change the frequency with which
the browser asks the server for updates.