
$(document).ready(function(){
    $("#about1").hide()
    $("#about2").hide()    
    $("#donate1").hide()
    $("#donate2").hide()
    $(".event-card").hide()
    //
	// About Waypoint
	//
    $("#about").waypoint(function(direction){
    	if (direction == 'down'){
    		$('#home-nav').removeClass('active-page');
    		$('#about-nav').addClass('active-page');

            $("#about2").fadeIn(1000);
    	}

    	else if (direction == 'up'){
    		$('#about-nav').removeClass('active-page');
    		$('#home-nav').addClass('active-page');

            $("#about2").fadeOut(1000);
    	}
   	}, {offset: '10%'});


    $("#about").waypoint(function(direction){
        if (direction == 'down'){
            $("#about1").fadeIn(1000);
            
        }

        else if (direction == 'up'){
            $("#about1").fadeOut(1000);
            
        }
    }, {offset: '60%'});
    //
	// Events Waypoint
	//
	$("#events").waypoint(function(direction){
    	if (direction == 'down'){
    		$('#about-nav').removeClass('active-page');
    		$('#events-nav').addClass('active-page');
    	}

    	else if (direction == 'up'){
    		$('#events-nav').removeClass('active-page');
    		$('#about-nav').addClass('active-page');
    	}
   	}, {offset: '10%'});


    $("#events").waypoint(function(direction){
        if (direction == 'down'){
            
            $(".event-card").fadeIn()
        }

        else if (direction == 'up'){
            $(".event-card").fadeOut()
        }
    }, {offset: '47%'});

    //
    // Donate Waypoint
    //

    if (screen.width >= 992) {
        $("#donate").waypoint(function(direction){
            if (direction == 'down'){
                $('#events-nav').removeClass('active-page');
            }

            else if (direction == 'up'){
                $('#events-nav').addClass('active-page');
            }
        }, {offset: '10%'});

        $("#donate").waypoint(function(direction){
            if (direction == 'down'){

                $('#donate1').fadeIn(1000);
                $("#donate2").fadeIn(1000);
            }

            else if (direction == 'up'){
                $('#donate1').fadeOut(1000);
                $("#donate2").fadeOut(1000);
            }
        }, {offset: '50%'});
    }

    if (screen.width < 992) {
        $('#donate1').style.display = "block";
        $("#donate2").style.display = "block";
    }
});