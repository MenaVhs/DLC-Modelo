// https://github.com/DeepLabCut/DeepLabCut-live/blob/master/example_processors/MouseLickLED/teensy_leds/teensy_leds.ino

const int LED = 13;
const int IR = 1;
const int REC = 2;
int frec = 7000;

void blink() {

  Serial.write(!digitalRead(REC));
  Serial.flush();
  noTone(IR);
  while (digitalRead(REC) == 0) {}
  
}

void setup() {

  pinMode(LED, OUTPUT);
  pinMode(IR, OUTPUT);
  pinMode(REC, INPUT);
  attachInterrupt(digitalPinToInterrupt(REC), blink, FALLING);

  Serial.begin(9600);
}

void loop() {

  unsigned int ser_avail = Serial.available();
  
  while (ser_avail > 0) {
    
    unsigned int cmd = Serial.read();

    if (cmd == 'L') {
      
      digitalWrite(LED, !digitalRead(LED));
    
    } else if (cmd == 'R') {

      Serial.write(digitalRead(LED));
      Serial.flush();
      
    } else if (cmd == 'I') {

      tone(IR, frec);
      
    }
    
  }
  
}

// Las primeras líneas declaran tres variables constantes que se utilizan más adelante en el código. Estas variables representan los pines a los que se conectan 
// los dispositivos LED, IR y REC.
// La función blink() se define para enviar un mensaje a través del puerto serie cuando se activa el interruptor REC. En primer lugar, se escribe en el puerto serie 
// si el interruptor REC está activado o no (1 o 0, respectivamente). 
// A continuación, se detiene la emisión del tono IR. Luego, se espera en un bucle while hasta que el 
// interruptor REC se libera (cuando su valor digital es 1).
// La función setup() se llama una vez al inicio del programa y se utiliza para configurar los pines y los interruptores. Primero, se establece el modo de los pines LED,
// IR y REC como salida o entrada según corresponda. A continuación, se llama a la función attachInterrupt() para configurar una interrupción en el pin REC. Cuando se 
// produce una caída de voltaje en el pin REC (es decir, cuando se presiona el interruptor), se ejecuta la función blink().
// La función loop() se llama continuamente después de que se complete la función setup(). Primero, se comprueba si hay datos disponibles en el puerto serie. 
// Si hay algún dato, se lee el primer byte y se compara con los caracteres 'L', 'R' e 'I'. Si el byte leído es 'L', el estado del LED se invierte. Si es 'R', 
// el estado del LED se envía a través del puerto serie. Si es 'I', se emite un tono en el dispositivo IR.