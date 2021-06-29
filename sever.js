const {spawn} = require('child_process');
const express = require("express");
const path = require('path');
var bodyParser = require('body-parser');
const app = express();
const fs = require("fs"); 
const port = 3000
//ajax speech recog file
app.use(express.static('public'));  
app.use('/img', express.static('images')); 
app.get("/", function (req, res) { 
  res.sendFile(path.join(__dirname+"/s2t.html")); 
});  

app.use(express.urlencoded());
app.use(express.json());
var inputLine;
app.get("/script.js",(req,res)=>{ 
  res.sendFile(path.join(__dirname+"/server.js")); 
})
app.post("/speach", function (req, res) { 
  inputLine=req.body.textbox; 
  console.log(inputLine)
  res.sendFile(path.join(__dirname+"/done.html")); 
}); 
//req Video
app.get("/video", function (req, res) {
    //creating video 
    var dataToSend;
    // spawn new child process to call the python script
    const python = spawn('python', ['speech_recog.py',inputLine]);///parametrs required in python ==sys.argv[1]
    // collect data from script
    python.stdout.on('data', function (data) {
      console.log('Pipe data from python script ...');
      dataToSend = data.toString();
    });
    // in close event we are sure that stream from child process is closed
    python.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`);})
    ////////////////////////////////////////////////////////////////////end of python    
    // Ensure there is a range given for the video 
    const range = req.headers.range;
    if (!range) {
      res.status(400).send("Requires Range header");
    }
  
    // get video stats (about 61MB)
    const videoPath = "clipg.mp4";
    const videoSize = fs.statSync("clipg.mp4").size;
  
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
    const videoStream = fs.createReadStream(videoPath, { start, end });
  
    // Stream the video chunk to the client
    videoStream.pipe(res);
  
})
/*
app.get('/img/bg4.jpg',(req,res))

app.get('/', (req, res) => {
 
 
 // send data to browser
 res.send(dataToSend)
 });
 */
app.listen(port, () => console.log(`Example app listening on port ${port}!`))