int mode = 2;
double distance; 
double calibration;
 
void setup()
{
  Serial.begin(9600);
  pinMode(12, INPUT);
}
 
void loop()
{
  if(mode == 1)
  {
  //Read duration in microSeconds
  long duration = pulseIn(12, HIGH);
  
  //Operation Range: 20 cm min (50 cm for accurate)
  distance = duration / 58.0; 
  calibration = -20;
  }
  else if (mode == 2)
  {
  //Analog In .49 mV per unit 
  double voltage = analogRead(5)*.0049;
   
  //.49 mV per cm
  distance = voltage/.0049;
  calibration = 0.0;
  }
   
  double cmToInch = 0.393701;
 
  //Analog Seems to be More Accurate due to PWM timing
  Serial.print((distance+calibration)*cmToInch);
  Serial.println();
  delay(100);
}
