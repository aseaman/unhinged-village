#include <Audio.h>
#include <Wire.h>
#include <SPI.h>
#include <SD.h>
#include <SerialFlash.h>

AudioPlaySdWav           playWav;
AudioOutputI2S           audioOutput;

AudioConnection          patchCord1(playWav, 0, audioOutput, 0);
AudioConnection          patchCord2(playWav, 1, audioOutput, 1);
AudioControlSGTL5000     sgtl5000_1;

// Use these with the Teensy Audio Shield
#define SDCARD_CS_PIN     10
#define SDCARD_MOSI_PIN   7   // Teensy 4 ignores this, uses pin 11
#define SDCARD_SCK_PIN    14  // Teensy 4 ignores this, uses pin 13

// Button
// Button wires don't matter as long as one goes to GND
// and one goes to pin 33
#define BUTTON_PIN        33

int buttonState = 0;

void setup() {
  Serial.begin(9600);
  Serial.print("init");

  pinMode(BUTTON_PIN, INPUT_PULLUP);

  // Audio connections require memory to work.  For more
  // detailed information, see the MemoryAndCpuUsage example
  AudioMemory(8);

  sgtl5000_1.enable();
  sgtl5000_1.volume(0.65);

  SPI.setMOSI(SDCARD_MOSI_PIN);
  SPI.setSCK(SDCARD_SCK_PIN);
  if (!(SD.begin(SDCARD_CS_PIN))) {
    // stop here, but print a message repetitively
    while (1) {
      Serial.println("Unable to access the SD card");
      delay(500);
    }
  }
}

void playFile(const char *filename)
{
  Serial.print("Playing file: ");
  Serial.println(filename);

  // Start playing the file.  This sketch continues to
  // run while the file plays.
  playWav.play(filename);

  // A brief delay for the library read WAV info
  delay(25);

  // Simply wait for the file to finish playing.
  while (playWav.isPlaying()) {
    // uncomment these lines if you audio shield
    // has the optional volume pot soldered
    //float vol = analogRead(15);
    //vol = vol / 1024;
    // sgtl5000_1.volume(vol);
  }
}


void loop() {
  // read state of button
  buttonState = digitalRead(BUTTON_PIN);

  if (buttonState == LOW) {
    Serial.print("Play!");
    playFile("SAMPLE.WAV");
  }
}

