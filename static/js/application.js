$(document).ready(function(){
    // Make a connection to the socket server
    let socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('connect', function() {
        console.log('Client connected.');
    });

    socket.on('iR_data', function(iR_data) {
        console.log('Received message');
        console.log(iR_data.sessionTime);

        // Make data visible on the front end
        $('#data').append('<p>' + iR_data.sessionTime + '</p>');
        // $('#data').text(iR_data.sessionTime);
    });
});