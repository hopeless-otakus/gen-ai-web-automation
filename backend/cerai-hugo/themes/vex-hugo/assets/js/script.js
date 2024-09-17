// Preloader js    
$(window).on('load', function () {
  $('.preloader').fadeOut(100);
});

var config = {
  target: document.querySelector('pushin'),
  scene: {
    breakpoints: [768, 1440, 1920],
    inpoints: [200, 300],
    outpoints: [600, 700],
    layerDepth: 800
  },
  composition: {
    ratio: [1,1]
  },
  layers: [
    // Layer 1
    {
      inpoints: [100, 300],
      outpoints: [300, 600],
      speed: 25
    },
  ],
};

// Method 1: Using global function
pushInStart(config);

(function ($) {
  'use strict';

  
  // product Slider
  $('.product-image-slider').slick({
    autoplay: false,
    infinite: true,
    arrows: false,
    dots: true,
    customPaging: function (slider, i) {
      var image = $(slider.$slides[i]).data('image');
      return '<img class="img-fluid" src="' + image + '" alt="product-image">';
    }
  });

  // Product slider
  $('.product-slider').slick({
    infinite: true,
    slidesToShow: 4,
    slidesToScroll: 1,
    autoplay: true,
    dots: false,
    arrows: false,
    responsive: [{
        breakpoint: 1024,
        settings: {
          slidesToShow: 3
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1
        }
      }
    ]
  });

})(jQuery);