$(function () {
    $('head').append('<style type="text/css"> \
#header {visibility: hidden; opacity: 100;} \
#teaser {visibility: hidden; opacity: 100;} \
#content {visibility: hidden; opacity: 100;} \
#footer {visibility: hidden; opacity: 100;} \
</style>');

    $(window).load(function() {
	$('#header').css({visibility: 'visible', opacity: 0}).fadeTo(1500, 1, function() {
	    $('#teaser').css({visibility: 'visible', opacity: 0}).delay(100).fadeTo(1000, 1, null);
	    $('#content').css({visibility: 'visible', opacity: 0}).delay(100).fadeTo(1000, 1, null);
	    $('#footer').css({visibility: 'visible', opacity: 0}).delay(1200).fadeTo(1000, 1, null);
	});
	// $('#header').css({visibility: 'visible', opacity: 0}).fadeTo(1500, 1, null);
	// $('#teaser').css({visibility: 'visible', opacity: 0}).fadeTo(1500, 1, null);
	// $('#content').css({visibility: 'visible', opacity: 0}).fadeTo(1500, 1, null);
	// $('#footer').css({visibility: 'visible', opacity: 0}).fadeTo(1500, 1, null);
    });

    $(document).ready(function() {
	$('a').click(function(e) {
	    if (e.which == 1) {
		e.preventDefault();
		window.location = this.href;
		$('body').fadeOut(500, null);
		// linkLocation = this.href;
		// $('body').fadeOut(1000, redirectPage);
	    }
	});

	// function redirectPage() {
	//     window.location = linkLocation;
	// }

        $('body').keypress(function(e) {
            if (e.which == 114) {
		// r
		window.location = '/random';
		$('body').fadeOut(500, null);
            }
	    else if (e.which == 97) {
		// a
		// window.location = '<author slug link>';
		// $('body').fadeOut(500, null);
	    }
	    else if (e.which == 104) {
		// h
		window.location = '/';
		$('body').fadeOut(500, null);
	    }
        });
    });
});