const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition

var recognition = new SpeechRecognition();

var textbox = $("#textbox")
var startbtn = $("#start-btn")


var content = ''
recognition.continuous = false

recognition.onstart = function () {
    startbtn.text("Stop")
    $('#start-btn').attr('start-btn', 'stop-btn');
}

recognition.onspeechend = function () {
    startbtn.text("Start")
    $("#stop-btn").toggleClass('btn btn-dark btn-block');
}

recognition.onerror = function () {
    startbtn.text("Try again")
}

recognition.onresult = function (event) {
    var current = event.resultIndex;
    var transcript = event.results[current][0].transcript

    content += transcript
    textbox.val(content)
}

$("#generate-btn").click(function (event) {

})

$("#start-btn").click(function (event) {
    if (content.length) {
        content += ''
    }
    $('#start-btn').attr('start-btn', 'stop-btn');
    recognition.start()
})

$("#cancel-btn").click(function (event) {
    textbox.val('')
    content = ''
})