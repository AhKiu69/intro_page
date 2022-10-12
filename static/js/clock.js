// function updateTime(){
//     a = new Date()
//     document.getElementById('clock').innerHTML =
//     a.getHours()+':'+a.getMinutes()+':'+a.getSeconds();
// }

function realtimeClock(){
    var rtClock = new Date();
    var hour = rtClock.getHours();
    var minute = rtClock.getMinutes();
    var second = rtClock.getSeconds();

    var amPm = (hour >12) ? "PM":"AM";
    var icon = (hour >12) ? "moon":"sun"
    document.getElementById('imageBox').src = "../static/imgs/" + icon + ".svg";
    hour = ("0"+hour).slice(-2);
    minute = ("0"+minute).slice(-2);
    second = ("0"+second).slice(-2);

    document.getElementById("clock").innerHTML = 
        hour+" : "+minute+" : "+ second+ "  "+amPm;
    var t = setTimeout(realtimeClock,500);
}
setInterval(function(){
    realtimeClock()
},1000)
