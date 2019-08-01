int analogvalue = 0;
double tempC = 0;
char *message = "my name is particle";
String aString;
int PIRSensor = D0;

void setup()
{
  Particle.variable("analogvalue", analogvalue);
  Particle.variable("temp", tempC);
  if (Particle.variable("mess", message)==false)
  {
      // variable not registered!
  }
  Particle.variable("mess2", aString);

  pinMode(A0, INPUT);
}

void loop()
{
  // Read the analog value of the sensor (TMP36)
  analogvalue = analogRead(A0);
  //Convert the reading into degree celcius
  tempC = (((analogvalue * 3.3)/4095) - 0.5) * 100;
  delay(10000);
  if(digitalRead(PIRSensor) == HIGH){
      Particle.publish("motion-detected", "Kangroo is moved!", PRIVATE);
  }
}
