console.log("custom.js loaded")

// Script start
var totalItems = $('.beritaitem').length;
var currentIndex = $('div.beritaitem.active').index() + 1;
var time = 5000;
var play = true;
var reset = false;

var berita1 = "This section is under construction!!!";
var berita2 = "This section is under construction!!!";
var berita3 = "This section is under construction!!!";

$('#beritateks').html(berita1);

//menganti berita untuk + 1
function changenews() {
    currentIndex = $('div.beritaitem.active').index() + 1;
    if (currentIndex == 1) {
        $('#beritateks').html(berita2);
    }
    else if (currentIndex == 2) {
        $('#beritateks').html(berita3);
    }
    else {
        $('#beritateks').html(berita1);
    }
}

//mengganti berita untuk -1
function minusnews() {
    currentIndex = $('div.beritaitem.active').index() - 1;
    if (currentIndex == 1) {
        $('#beritateks').html(berita2);
    }
    else if (currentIndex == -1) {
        $('#beritateks').html(berita3);
    }
    else {
        $('#beritateks').html(berita1);
    }
}

//fungsi timer
function Timer(fn, t) {
    var timerObj = setInterval(fn, t);

    //stop
    this.stop = function () {
        if (timerObj) {
            clearInterval(timerObj);
            timerObj = null;
        }
        return this;
    }

    // saat mulai
    this.start = function () {
        if (!timerObj) {
            this.stop();
            timerObj = setInterval(fn, t);
        }
        return this;
    }

    //  reset
    this.reset = function (newT = t) {
        t = newT;
        return this.stop().start();
    }
}

//saat pointer tidak pada caraousel
function jalankan() {
    timer.reset(5000);
}

//saat pointer pada cararousel
function berhenti() {
    timer.stop();
}

var timer = new Timer(function () {
    changenews();
    timer.reset(5000);
}, 5000);

$(".next").click(function () {
    changenews();
    timer.reset(5000);
});

$(".prev").click(function () {
    minusnews();
    timer.reset(5000);
});

$(document).ready(function () { 
    $(document).click(function () {
         $('.navbar-collapse').collapse('hide');
    });
  });