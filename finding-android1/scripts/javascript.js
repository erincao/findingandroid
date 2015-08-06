var counter = 0;

$(document).ready(function(){
  hide_n_show_1();
   $(".next_level_button").hide()
   $("#android_level1").click(function(){

    $.post( "/AttemptsHandler", { 'attempts': counter } );
     $("#android_level1").height(200).width(200)
     animateAndroid_1();
     $(".next_level_button").fadeIn()
   });
   $('.bglevel1').click(function() {
     counter++;
   });
});

$(document).ready(function(){
  $(".next_level_button").hide()
  $("#android_level2").click(function(){
    $.post( "/AttemptsHandler", { 'attempts': counter } );
    $("#android_level2").height(200).width(200)
    animateAndroid_2();
    $(".next_level_button").fadeIn()
  });
  $('.bglevel2').click(function() {
    counter++;
  });
});

$(document).ready(function(){
  $(".next_level_button").hide()
  $("#android_level3").click(function(){
    $.post( "/AttemptsHandler", { 'attempts': counter } );
    $("#android_level3").height(200).width(200)
    animateAndroid_3();
    $(".next_level_button").fadeIn()
  });
  $('.bglevel3').click(function() {
    counter++;
  });
});

$(document).ready(function(){
  $(".next_level_button").hide()
  $("#android_level4").click(function(){
    $.post( "/AttemptsHandler", { 'attempts': counter } );
    $("#android_level4").height(200).width(200)
    animateAndroid_4();
    $(".next_level_button").fadeIn()
  });
  $('.bglevel4').click(function() {
    counter++;
  });
});

$(document).ready(function(){
  $(".next_level_button").hide()
  $("#android_level5").click(function(){
    $.post( "/AttemptsHandler", { 'attempts': counter } );
    $("#android_level5").height(200).width(200)
    animateAndroid_5();
    $(".next_level_button").fadeIn()
  });
  $('.bglevel5').click(function() {
    counter++;
  });
});

$(document).ready(function(){
    animateLollipop();
    animateFlying_Android();
    animateAndroid_Superhero();
    animateAndroid_Tornado();
    animateAndroid_Videogame();
    animateBalloon_1();
    animateBalloon_2();
    animateBalloon_3();
    animateDancing_Android;
});

// function randomize(){
//
// }

function animateLollipop(){
    var newq = makeNewPosition();
    $("#lollipop").animate({ top: newq[0], left: newq[1] }, function(){
      animateLollipop();
      $("#lollipop").click(function(){
       $("#lollipop").fadeOut()
     });
    });
};

function animateFlying_Android(){
    var newq = makeNewPosition();
    $("#flying_android").animate({ top: newq[0], left: newq[1] }, function(){
      animateFlying_Android();
      $("#flying_android").click(function(){
       $("#flying_android").fadeOut()
     });
    });
};

function animateAndroid_Superhero(){
    var newq = makeNewPosition();
    $("#android_superhero").animate({ top: newq[0], left: newq[1] }, function(){
      animateAndroid_Superhero();
      $("#android_superhero").click(function(){
       $("#android_superhero").fadeOut()
     });
    });
};

function animateAndroid_Tornado(){
    var newq = makeNewPosition();
    $("#android_tornado").animate({ top: newq[0], left: newq[1] }, function(){
      animateAndroid_Tornado();
      $("#android_tornado").click(function(){
       $("#android_tornado").fadeOut()
     });
    });
};

function animateAndroid_Videogame(){
    var newq = makeNewPosition();
    $("#android_videogame").animate({ top: newq[0], left: newq[1] }, function(){
      animateAndroid_Videogame();
      $("#android_videogame").click(function(){
       $("#android_videogame").fadeOut()
     });
    });
};

function animateBalloon_1(){
    var newq = makeNewPosition();
    $("#balloon_1").animate({ top: newq[0], left: newq[1] }, function(){
      animateBalloon_1();
      $("#balloon_1").click(function(){
       $("#balloon_1").fadeOut()
     });
    });
};

function animateBalloon_2(){
    var newq = makeNewPosition();
    $("#balloon_2").animate({ top: newq[0], left: newq[1] }, function(){
      animateBalloon_2();
      $("#balloon_2").click(function(){
       $("#balloon_2").fadeOut()
     });
    });
};

function animateBalloon_3(){
    var newq = makeNewPosition();
    $("#balloon_3").animate({ top: newq[0], left: newq[1] }, function(){
      animateBalloon_3();
      $("#balloon_3").click(function(){
       $("#balloon_3").fadeOut()
     });
    });
};

function animateDancing_Android(){
    var newq = makeNewPosition();
    $("#android_dancing").animate({ top: newq[0], left: newq[1] }, function(){
      animateDancing_Android();
      $("#android_dancing").click(function(){
       $("#android_dancing").fadeOut()
     });
    });
};

function hide_n_show_1(){
  $("#android_level1").hide()
  $(".bglevel1").hide()
  $("#android_level1").show()
  $(".bglevel1").show()
}

function makeNewPosition(){
    // Get viewport dimensions (remove the dimension of the div)
    var h = $(window).height() - 50;
    var w = $(window).width() - 50;

    var nh = Math.floor(Math.random() * h);
    var nw = Math.floor(Math.random() * w);

    return [nh,nw];
}

function animateAndroid_1(){
    var newq = makeNewPosition();
    $("#android_level1").animate({ top: newq[0], left: newq[1] }, function(){
      animateAndroid_1();
    });
};

function animateAndroid_2(){
    var newq = makeNewPosition();
    $("#android_level2").animate({ top: newq[0], left: newq[1] }, function(){
      animateAndroid_2();
    });
};

function animateAndroid_3(){
    var newq = makeNewPosition();
    $("#android_level3").animate({ top: newq[0], left: newq[1] }, function(){
      animateAndroid_3();
    });
};

function animateAndroid_4(){
    var newq = makeNewPosition();
    $("#android_level4").animate({ top: newq[0], left: newq[1] }, function(){
      animateAndroid_4();
    });
};

function animateAndroid_5(){
    var newq = makeNewPosition();
    $("#android_level5").animate({ top: newq[0], left: newq[1] }, function(){
      animateAndroid_5();
    });
};
