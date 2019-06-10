//Variables
int TempC;
int Sound;
int Luz;
String MedidaT;
String MedidaS;
String MedidaL;
String MedidasJuntas;
int pinT = A0;
int pinS = A1;
int pinL = A2;

void setup(){
  Serial.begin(9600);
}

void loop(){
  MedidaT="TEMP-";
  MedidaS="SND-";
  MedidaL="LUZ-";
  
  TempC=analogRead(pinT);
  Sound=analogRead(pinS);
  Luz=analogRead(pinL);
  
  Sound = Sound/10;  // Previo pruebas de sonido con sensor
  if (Sound>99){
    Sound=99;
  }
  Luz = Luz/10;
  TempC = (5.0*TempC*100.0)/1024.0;
  
  String temp = (String) TempC;
  String snd = (String) Sound;
  String luz = (String) Luz;
  
  MedidaT = MedidaT + temp;
  if (Sound<10){
    snd = "0" + snd;
  }
  MedidaS = MedidaS + snd;
  MedidaL = MedidaL + luz;
  MedidasJuntas = MedidaT + ":" + MedidaS + ":" + MedidaL;
  
  Serial.println(MedidasJuntas);
  delay(3000);
}
