let video;
let label = "waiting...";
let naziv = "";
let classifier;
let modelURL = 'https://teachablemachine.withgoogle.com/models/WA3z8CfxL/';

function setup() {
  createCanvas(640, 520);
  video = createCapture(VIDEO);
  video.hide();

  // učitavanje modela i pokretanje klasifikacije tek kad je spreman
  classifier = ml5.imageClassifier(modelURL + 'model.json', modelReady);
}

function modelReady() {
  console.log("Model je učitan");
  classifyVideo();
}

function classifyVideo() {
  classifier.classify(video, gotResults);
}

function draw() {
  background(0);
  image(video, 0, 0);

  textSize(32);
  textAlign(CENTER, CENTER);
  fill(255);
  text(label, width / 2, height - 16);

  if (label === "ja") {
    naziv = "🦄";
  } else if (label === "sveska") {
    naziv = "🍎";
  } else {
    naziv = "🍏";
  }

  textSize(256);
  text(naziv, width / 2, height / 2);
}

function gotResults(error, results) {
  if (error) {
    console.error(error);
    return;
  }
  label = results[0].label;
  classifyVideo();
}
