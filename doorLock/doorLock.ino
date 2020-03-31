char incomingByte;

#define Candado 19//define los pines
#define Buzzer  10

void setup() {
    Serial.begin(9600);
    pinMode(Buzzer, OUTPUT);
    pinMode(Candado, OUTPUT);
    Serial.write("Power On\n");
}

char Comp(char This) {
    while (Serial.available() > 0) // no leer amenos de que haya datos alli
    {
    incomingByte = Serial.read();
    }
    if(This== incomingByte){
    incomingByte=0;
    return 1;
    }
    else {return 0;}
}

void loop()
{
    if (Comp('1')) {
        Serial.write("puerta abierta\n");
        analogWrite(Buzzer,124);
        digitalWrite(Candado,1);
        delay(3000);
        digitalWrite(Candado,0);
        analogWrite(Buzzer,0);
        Serial.write("puerta cerrada\n");
    }
}
