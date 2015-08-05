$(document).ready(function(){
   $("#next_level_button_1").hide()
    $("#android_level1").click(function(){
      $("#android_level1").height(200).width(200)
     animateAndroid_1();
     $("#next_level_button_1").fadeIn()
   });
  });

$(document).ready(function(){
  $("#next_level_button_2").hide()
  $("#android_level2").click(function(){
    $("#android_level2").height(200).width(200)
    animateAndroid_2();
    $("#next_level_button_2").fadeIn()
});
});

$(document).ready(function(){
  $("#next_level_button_3").hide()
  $("#android_level3").click(function(){
    $("#android_level3").height(200).width(200)
    animateAndroid_3();
    $("#next_level_button_3").fadeIn()
});
});

$(document).ready(function(){
  $("#next_level_button_4").hide()
  $("#android_level4").click(function(){
    $("#android_level4").height(200).width(200)
    animateAndroid_2();
    $("#next_level_button_4").fadeIn()
});
});



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
    $("#android_level1").animate({ top: newq[0], left: newq[1] }, function(){
      animateAndroid_3();
    });
};

function animateAndroid_4(){
    var newq = makeNewPosition();
    $("#android_level1").animate({ top: newq[0], left: newq[1] }, function(){
      animateAndroid_4();
    });
};

function animateAndroid_5(){
    var newq = makeNewPosition();
    $("#android_level1").animate({ top: newq[0], left: newq[1] }, function(){
      animateAndroid_5();
    });
};
