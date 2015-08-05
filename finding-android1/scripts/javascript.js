$(document).ready(function(){
   $(".next_level_button").hide()
    $("#android_level1").click(function(){
      $("#android_level1").height(200).width(200)
     animateAndroid();
     $(".next_level_button").fadeIn()
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
function animateAndroid(){
    var newq = makeNewPosition();
    $("#android_level1").animate({ top: newq[0], left: newq[1] }, function(){
      animateAndroid();
    });
};
