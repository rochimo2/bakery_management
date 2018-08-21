jQuery(document).ready(function($) {
   
   'use strict';
   
		
//	 * Replace all SVG images with inline SVG	 
	jQuery('img.svg').each(function(){
		var $img = jQuery(this);
		var imgID = $img.attr('id');
		var imgClass = $img.attr('class');
		var imgURL = $img.attr('src'); 
	
		jQuery.get(imgURL, function(data) {
			// Get the SVG tag, ignore the rest
			var $svg = jQuery(data).find('svg');
	
			// Add replaced image's ID to the new SVG
			if(typeof imgID !== 'undefined') {
				$svg = $svg.attr('id', imgID);
			}
			// Add replaced image's classes to the new SVG
			if(typeof imgClass !== 'undefined') {
				$svg = $svg.attr('class', imgClass+' replaced-svg');
			}
	
			// Remove any invalid XML tags as per http://validator.w3.org
			$svg = $svg.removeAttr('xmlns:a');
	
			// Check if the viewport is set, if the viewport is not set the SVG wont't scale.
			if(!$svg.attr('viewBox') && $svg.attr('height') && $svg.attr('width')) {
				$svg.attr('viewBox', '0 0 ' + $svg.attr('height') + ' ' + $svg.attr('width'))
			}
	
			// Replace image with new SVG
			$img.replaceWith($svg);
	
		}, 'xml');
	
	});

	
   //ISOTOPE FILTER
   var $grid = $('.grid').isotope({
	  itemSelector: '.cake',
	  layoutMode: 'fitRows'
	});

   // bind filter button click
	$('.filters-button-group').on( 'click', 'button', function() {
	  var filterValue = $( this ).attr('data-filter');
	  // use filterFn if matches value
	 // filterValue = filterFns[ filterValue ] || filterValue;
	  $grid.isotope({ filter: filterValue });
	});
	// change is-checked class on buttons
	$('.button-group').each( function( i, buttonGroup ) {
	  var $buttonGroup = $( buttonGroup );
	  $buttonGroup.on( 'click', 'button', function() {
	    $buttonGroup.find('.is-checked').removeClass('is-checked');
	    $( this ).addClass('is-checked');
	  });
	});

  
    //SMOOTH SCROLL EFFECT
   $("#nav ul li a[href*='#']").click(function() {
		if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') 
			|| location.hostname == this.hostname) {
				
			var target = $(this.hash);
			target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
			   if (target.length) {
				 $('html,body').animate({
					 scrollTop: target.offset().top 
				}, 1000);
				return false;
			}
		}
	});

   
   //NAVBAR ANIMATION
	
	// get header height (without border)
	var getHeaderHeight = $('.navbar-custom').outerHeight();

	// border height value (make sure to be the same as in your css)
	var borderAmount = 2;

	// shadow radius number (make sure to be the same as in your css)
	var shadowAmount = 30;

	// init variable for last scroll position
	var lastScrollPosition = 0;

	// set negative top position to create the animated header effect
	$('.navbar-custom').css('top', '-' + (getHeaderHeight + shadowAmount + borderAmount) + 'px');

	$(window).scroll(function() {
		var currentScrollPosition = $(window).scrollTop();

		if ($(window).scrollTop() > 2 * (getHeaderHeight + shadowAmount + borderAmount) ) {

			$('body').addClass('scrollActive').css('padding-top', getHeaderHeight);
			$('.navbar-custom').css('top', 0);

			if (currentScrollPosition < lastScrollPosition) {
				$('.navbar-custom').css('top', '-' + (getHeaderHeight + shadowAmount + borderAmount) + 'px');
			}
			lastScrollPosition = currentScrollPosition;

		} else {
			$('body').removeClass('scrollActive').css('padding-top', 0);
		}
	});

	//AUTOCOLLAPSE MOBILE MENU
	$(".navbar-nav li a").click(function(event) {
    $(".navbar-collapse").collapse('hide');
  	}) 
	  
	
	//MAGNIFIC POPUP LOAD CONTENT VIA AJAX
	$('.cake-detail').magnificPopup({type: 'ajax'});
 	
	//MAGNIFIC POPUP IMAGE
	$('.image-popup').magnificPopup({
		type:'image',
		gallery: {
			enabled: false,
			navigateByImgClick: false,
			preload: [0,1] // Will preload 0 - before current, and 1 after the current image
		},
		
	});
	
       
	  
	//OWLCAROUSEL STORE CAROUSEL
	var owl = $("#store-carousel");
 
	  owl.owlCarousel({
		  autoPlay: false,
		  itemsCustom : [ [0, 1], [450, 1], [600, 3], [700, 3], [1000, 3], [1200, 3], [1600, 3] ],
		  pagination : false,
		  navigation : true,
		  navigationText : ['<i class="pe-4x pe-7s-angle-left pe-border"></i>','<i class="pe-4x  pe-7s-angle-right pe-border"></i>'],
	  });


	//OWLCAROUSEL PRICE TABLE CAROUSEL
	var owl = $("#package-carousel");
 
	  owl.owlCarousel({
		  autoPlay: false,
		  itemsCustom : [ [0, 1], [450, 1], [600, 3], [700, 3], [1000, 3], [1200, 3], [1600, 3] ],
		  pagination : false,
		  navigation : true,
		  navigationText : ['<i class="pe-4x pe-7s-angle-left pe-border"></i>','<i class="pe-4x  pe-7s-angle-right pe-border"></i>'],
	  });
	  
	//OWLCAROUSEL FUNFACT CAROUSEL
	var owl = $("#funfacts-carousel");
 
	  owl.owlCarousel({
		  itemsCustom : [
			[0, 1],
			[450, 1],
			[600, 2],
			[700, 4],
			[1000, 4],
			[1200, 4],
			[1600, 4]
		  ],
		  navigation : false,
		  navigationText : ['<i class="pe-4x pe-7s-angle-left pe-border"></i>','<i class="pe-4x  pe-7s-angle-right pe-border"></i>'],
	  });
	  
	  //OWLCAROUSEL PRICE TABLE CAROUSEL
	var owl = $("#price-carousel");
 
	  owl.owlCarousel({
		  itemsCustom : [
			[0, 1],
			[450, 1],
			[600, 2],
			[700, 3],
			[1000, 3],
			[1200, 3],
		  ],
		  pagination : false,
		  navigation : true,
		  navigationText : ['<i class="pe-4x pe-7s-angle-left pe-border"></i>','<i class="pe-4x  pe-7s-angle-right pe-border"></i>'],
	  });
	
	//OWLCAROUSEL TESTIMONIAL CAROUSEL
	var owl = $("#testimonial-carousel");
 
	  owl.owlCarousel({
	  	  singleItem:true,
		  navigation : false, // Show next and prev buttons
		  pagination : false,
		  slideSpeed : 300,
		  paginationSpeed : 400,
		  transitionStyle : "fade"
	  });
	
	//OWLCAROUSEL SPONSORS CAROUSEL
	var owl = $("#sponsors-carousel");
 
	  owl.owlCarousel({
		  
		  autoPlay: false,
		  itemsCustom : [
			[0, 1],
			[450, 1],
			[600, 3],
			[700, 3],
			[1000, 3],
			[1200, 5],
			[1600, 5]
		  ],
		  pagination : false,
		  navigation : true,
		  navigationText : ['<i class="pe-4x pe-7s-angle-left pe-border"></i>','<i class="pe-4x  pe-7s-angle-right pe-border"></i>'],
	  });

	//OWLCAROUSEL TEAM CAROUSEL
	var owl = $("#list-");
 
	  owl.owlCarousel({
		  
		  autoPlay: false,
		  itemsCustom : [
			[0, 1],
			[450, 1],
			[600, 3],
			[700, 3],
			[1000, 3],
			[1200, 5],
			[1600, 5]
		  ],
		  pagination : false,
		  navigation : true,
		  navigationText : ['<i class="pe-4x pe-7s-angle-left pe-border"></i>','<i class="pe-4x  pe-7s-angle-right pe-border"></i>'],
	  });


	$('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
          disableOn: 700,
          type: 'iframe',
          mainClass: 'mfp-fade',
          removalDelay: 160,
          preloader: false,

          fixedContentPos: false,
          iframe: {
          	gmaps: {
		      index: '//maps.google.',
		      src: '%id%&output=embed'
    		}
          },
        });
	
	// FUNFACTS
	 $('.number').counterUp({
		delay: 10,
		time: 3000
	});
	
});	

	//FIX HOVER EFFECT ON IOS DEVICES
	document.addEventListener("touchstart", function(){}, true);
	

$(window).load(function(){
			
    //PRELOADER
    $('#preload').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website.
	
});


