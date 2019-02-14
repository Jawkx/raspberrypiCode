#include <Wire.h>
#include "motordriver_4wd.h"
#include "motordriver_4wd_dfs.h"

#define SLAVE_ADDRESS 0x04

char number[50];
int state = 0;

//Code Initialization
void setup() {
  MOTOR.init();
  // initialize i2c as slave
  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);
  // define callbacks for i2c communication
  //  Wire.onRequest(sendData);
}

void loop() {
  delay(100);
  Wire.onReceive(receiveData);
  Serial.print(number);

  if ( number[0] == 'G' ){
    goStraight();
  }else if ( number[0] == 'L'){
    slowDown();
  } else if ( number[0] == 'S'){
    stopCar();
  }
} 

// callback for received data
void receiveData(int byteCount) {
  int i = 0;
  while (Wire.available()) {
    number[i] = Wire.read();
    i++;
  }
 // number[i] = '\0';
} 

void goStraight() {
  
  MOTOR.setSpeedDir1(30,DIRF);
  MOTOR.setSpeedDir2(30,DIRR);
  
}

void slowDown() {

  MOTOR.setSpeedDir1(5,DIRF);
  MOTOR.setSpeedDir2(5,DIRR);
  
}
void stopCar(){

  MOTOR.setSpeedDir1(0,DIRF);
  MOTOR.setSpeedDir2(0,DIRF);
  
}
