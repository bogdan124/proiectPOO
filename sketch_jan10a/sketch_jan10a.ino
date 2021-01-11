#include <SoftwareSerial.h>

#include "TinyGPS++.h"
TinyGPSPlus gps;


int sensorPin = A0;    
float sensorValue = 0;  
int count=0;
int starttime = 0;
int heartrate = 0;
boolean counted = false;


SoftwareSerial ss(4,3);


void setup() {
  
    Serial.begin(9600); 
        ss.begin(9600);
   pinMode(sensorPin, INPUT);

}

void loop() {
  while(ss.available() > 0){
    gps.encode(ss.read());
    if(gps.location.isUpdated()){   
      Serial.print(gps.location.lat(),6);  Serial.print(' '); 
      Serial.print(gps.location.lng(),6);  Serial.print(' '); 
      Serial.print(gps.altitude.meters()); Serial.print(' '); 
      Serial.print(gps.speed.mps()); Serial.print(' '); 
      Serial.print(gps.satellites.value());Serial.print(' '); 
        sensorValue = analogRead(sensorPin);
           /*if (sensorValue >550 && counted == false)         
             {                                                               
               count++;
               counted = true; 
              }
             else if (sensorValue < 500)
             {
                    counted = false;
             } */
             delay(1000);
             Serial.println(heartrate);                                    
                
              heartrate=0;
              count =0;
    }
  }

}
