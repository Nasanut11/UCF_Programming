// Creative Project 3: Celestial Blossom

// Credits & Inspirations: 
/*
  This project was designed to fulfill the requirements laid out in the assingment - to create an audio visual instrument using       p5.js. The idea changed a lot due to difficulties with getting things to work, so here we are. Originally the idea was to create     an instrument that would play parts of the lyrics for Rick Astley's "Never Gonna Give You Up" in place of the monotones (i.e. one   lyric in place of one note or sound). Ultimately this did not pan out as I couldn't get it to function/did not have time to tinker   with it. The final version seen here allows users to input any piece of text; whether it be word, sentence, or paragraph, to         create "music" using each individual letter in a given word.
  
*/
//----------------------------------------------------------------------------------------------------------------------------------

let monoSynth;
let alphabet = ["a","b","c","d","e","f","g","h","i","j","k","k","m","n","o","p","q","r","t","u","v","w","x","y","z"];
let notes = ["A4","B4","C4","D4","E4","F4","G4"];
// Letters defined to be assinged a random note
let sounds = [];
/*let lyrics = ["Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you"];*/

//----------------------------------------------------------------------------------------------------------------------------------

function setup() {
  let canvas = createCanvas(300,300);
  background(0);
  textAlign(CENTER);
  text('tap to play', width/2, height/2);
    
  generateKeys();
  //let lyric = random(lyrics);
  //canvas.mousePressed(()=>{
  //  lyricToLetters(lyric)
  //})
  
  input = createInput();
  input.position(20, 65);
  button = createButton('submit');
  button.position(input.x + input.width, 65);
  button.mousePressed(lyricToLetters);

  monoSynth = new p5.MonoSynth();
}

function generateKeys() {
  for(let i = 0; i < alphabet.length; i++) {
    sounds.push(random(notes));
  }
}

// Generate sound for phrase -------------------------------------------------------------------------------------------------------
function lyricToLetters(value) {
  userStartAudio();
  //let lyric = value;
  let lyric = input.value();
  for(let i = 0; i < lyric.length; i++) {
    let char = lyric[i];
    let index = alphabet.indexOf(char);
    let note = sounds[index];
    let volume = 1;
    let time = 0;
    let dur = 1/16;
    monoSynth.play(note, volume, i, dur);
  }
}