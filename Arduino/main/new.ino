void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);
}

void loop() {
  if(Serial.available()>0){
    sel=Serial.parseInt();
    Serial.print(sel);
}
