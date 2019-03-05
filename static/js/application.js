$(document).ready(function(){
    
    // Make a connection to the socket server
    let socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('connect', function() {
        console.log('Client connected.');
    });

    socket.on('iR_data', function(iR_data) {
        let parsed_iR_data = JSON.parse(iR_data)

        // Make data visible on the front end
        $('#AirTemp').text(parsed_iR_data.AirTemp);
        $('#TrackTemp').text(parsed_iR_data.TrackTemp);
        $('#OilTemp').text(parsed_iR_data.OilTemp);
        $('#WaterTemp').text(parsed_iR_data.WaterTemp);
        $('#SessionTime').text(parsed_iR_data.SessionTime);
        $('#FuelLevel').text(parsed_iR_data.FuelLevel);
        $('#Lap').text(parsed_iR_data.Lap);
    });
    
});