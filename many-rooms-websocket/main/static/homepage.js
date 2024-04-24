// When the button is clicked,
// this function asks the server for the number of a room that isn't full
// This function then calls redirectRoom to join the given room number
function joinRoom(){
    player_name = document.getElementById("playerName").value;
    
    URL = "/requestRoomNum/" + player_name;
    fetch(URL).then( response => response.json()).then( the_json => redirectRoom(the_json) );
}

function redirectRoom(the_json){
    room_number = the_json['num'];

    player_name = document.getElementById("playerName").value;

    URL = "/gameRoom/" + room_number + "/" + player_name;

    URL = "http://" + location.host + URL;

    location.href = URL;
}



