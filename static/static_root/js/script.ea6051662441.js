$(document).ready(function(){
    
    //
	// About Waypoint
	//
    $("#about").waypoint(function(direction){
    	if (direction == 'down'){
    		$('#home-nav').removeClass('active-page');
    		$('#about-nav').addClass('active-page');
    	}

    	else if (direction == 'up'){
    		$('#about-nav').removeClass('active-page');
    		$('#home-nav').addClass('active-page');
    	}
   	}, {offset: '10%'});

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

});