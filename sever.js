const {spawn} = require('child_process');
const util = require('util')
const express = require("express");
const path = require('path');
var bodyParser = require('body-parser');
const app = express();
const fs = require("fs"); 
const port = 3000

//ajax spaech recog file
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
    python().then(function(fromRunpy) { 
    // Ensure there is a range given for the video 
    const range = req.headers.range;
    if (!range) {
      res.status(400).send("Requires Range header");
    }
  
    // get video stats (about 61MB)
    const videoPath = path.join(__dirname)+"/data/samples/output/clipg.mp4";
    console.log(videoPath.isFile());
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
  } 
  
  ).catch( ()=> {
    console.log("Promise Rejected");
});;
  
}) 
//Python promisifying  
async function python(){
 return new Promise(async function(success, nosuccess) { 
  const { spawn } = require('child_process');
  const pyprog = spawn('python', ['speech_recog.py',inputLine]);///parametrs required in python ==sys.argv[1] 
  pyprog.stdout.on('data', function(data) {
      console.log("success **********\n"+data);
      success(data);
      
  });

  pyprog.stderr.on('data', (data) => {
    console.log("err"+data);
      nosuccess(data);
  });
}); 
}
app.listen(port, () => console.log(`Example app listening on port ${port}!`))