function slider_change(slide) {
  $('#slider img.slider').fadeOut(200, function(){
    $('#slider img.slider').attr('src', '/static/img/Roloduck_Product-screenshot_'+slide+'.png');
  }).fadeIn(200);
  for (var i=1; i<4; i++) {
    if (i == slide) {
      $('#slider-'+slide).html('<img src="/static/img/slider-dot-active.png" />');
    } else {
      $('#slider-'+i).html('<a onclick="slider_change('+i+')"><img src="/static/img/slider-dot.png" /></a>');
    }
  }
}