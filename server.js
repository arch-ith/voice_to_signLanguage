const express = require("express");

const { spawn } = require('child_process');
const { Console } = require("console");
const app = express();
const path = require('path');
let ejs = require('ejs');
var bodyParser = require('body-parser');
const fs = require("fs");
app.use(express.urlencoded());
app.use(express.json());
app.set('view engine', 'ejs');

const port = 3000
let inputLine = ""
let done = false
let dataString = ""
let requiredData = ""
//static images file
app.use(express.static('public'));
app.use('/img', express.static('images'));

//Home page s2t.html
app.get("/", function (req, res) {
  inputLine = ""
  done = false
  dataString = ""
  requiredData = ""
  res.sendFile(path.join(__dirname + "/s2t.html"));
});
//Final speach file done.html
app.post("/speach", function (req, res) {
  inputLine = req.body.textbox;
  //res.sendFile(path.join(__dirname+"/done.html"));
  res.render('result', { done: done, islSyntax: requiredData, normalSyntax: inputLine })
  isItDoneYet().then((msg) => {
    console.log(msg)
    console.log(inputLine)

    console.log("data->" + dataString)
    let startIndex = dataString.indexOf("ISL:{")
    let endIndex = dataString.indexOf("}")
    requiredData = dataString.substring(startIndex + 5, endIndex);
    //res.sendFile(path.join(__dirname + "/done.html"))
    done = true;
  }).catch((msg) => {
    console.log(msg);
  })
});
app.get("/loading", (req, res) => {
  res.render('result', { done: done, islSyntax: requiredData, normalSyntax: inputLine })
})
//done request video 
app.get("/video", function (req, res) {
  const range = req.headers.range;
  if (!range) {
    res.status(400).send("Requires Range header");
  }

  // get video stats (about 61MB)
  const videoPath = path.resolve(__dirname + "/data/samples/output/clipg.mp4");
  const videoSize = fs.statSync(videoPath).size;

  // Parse Range
  // Example: "bytes=32324-"
  const CHUNK_SIZE = 10 ** 6; // 1MB
  const start = Number(range.replace(/\D/g, ""));
  const end = Math.min(start + CHUNK_SIZE, videoSize - 1);

  // Create headers
  const contentLength = end - start + 1;
  const headers = {
    "Content-Range": `bytes ${start}-${end}/${videoSize}`,
    "Accept-Ranges": "bytes",
    "Content-Length": contentLength,
    "Content-Type": "video/mp4",
  };

  // HTTP Status 206 for Partial Content
  res.writeHead(206, headers);

  // create video read stream for this particular chunk
  var videoStream = fs.createReadStream(videoPath, { start, end });

  // Stream the video chunk to the client
  videoStream.pipe(res); 
})

//this the python promise 
const isItDoneYet = () => new Promise((resolve, reject) => {
  const python = spawn('python', ['speech_recog.py', inputLine])
  let c = false
  python.stdout.on('data', function (data) {
    dataString += data.toString();
  })
  python.on('exit', (code) => {
    console.log(`child process close all stdio with code ${code}`);
    if (code == 0)
      c = true;
    if (c) {
      const workDone = 'Here is the thing I built'
      resolve(workDone)
    } else {
      const why = 'Sorry I failed to built it'
      reject(why)
    }
  });

})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))
