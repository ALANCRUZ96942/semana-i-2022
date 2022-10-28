

/*Configuracion esp32*/
#include <esp_wpa2.h>
#include <Arduino.h>
#if defined(ESP32)
  #include <WiFi.h>
#elif defined(ESP8266)
  #include <ESP8266WiFi.h>
#endif
#include <Firebase_ESP_Client.h>

//Credenciales
#include "password.h"

//Provide the token generation process info.
#include "addons/TokenHelper.h"
//Provide the RTDB payload printing info and other helper functions.
#include "addons/RTDBHelper.h"




// Insert your network credentials
const char* ssid = "Tec"; 
#define EAP_IDENTITY AUTH
#define EAP_PASSWORD PASSWORD

// Insert Firebase project API Key
#define API_KEY "AIzaSyDAevrT5wmuxqptMnlTghUnvpZPV0pfTa4"

// Insert RTDB URLefine the RTDB URL */
#define DATABASE_URL "https://esp-32-semana-i-523bd-default-rtdb.firebaseio.com/" 

//Define Firebase Data object
FirebaseData fbdo;

FirebaseAuth auth;
FirebaseConfig config;

unsigned long sendDataPrevMillis = 0;
//variables a mandar
int count = 0;
bool signupOK = false;
//String 
String sValue;
int intValue;
//bool boolValue;
//String
String pValue;
int pwmValue;








//para sensor PIR

const int PIN_TO_SENSOR = 16; // GIOP16 pin connected to OUTPUT pin of sensor
int pinStateCurrent   = LOW;  // current state of pin
int pinStatePrevious  = LOW;  // previous state of pin
int pirValue = 0;
//para sensor de temperatura
#include "DHT.h"
#define DHTPIN 4
#define DHTTYPE DHT11   // DHT 11
DHT dht(DHTPIN, DHTTYPE);
float h,t,f,hif,hic;
int temp;

//sensor ultrasonico
const int trigPin = 5;
const int echoPin = 18;
//define sound speed in cm/uS
#define SOUND_SPEED 0.034
#define CM_TO_INCH 0.393701
long duration;
float distanceCm;
float distanceInch;

/*Display de 7 segmentos*/
//se demuestra el manejo del display de siete segmentos
//se declaran los pines a usar
//int LEDs[] = {8,9,7,6,4,3,2};        // for Arduino microcontroller
//int LEDs[] = {D2,D1,D3,D4,D6,D7,D8}; // for ESP8266 microcontroller
int LEDs[] = {22,23,21,19,17,2,15};    // for ESP32 microcontroller
//se declaran los arreglos que forman los dígitos
int zero[] = {0, 1, 1, 1, 1, 1, 1};   // cero
int one[] = {0, 0, 0, 0, 1, 1, 0};   // uno
int two[] = {1, 0, 1, 1, 0, 1, 1};   // dos
int three[] = {1, 0, 0, 1, 1, 1, 1};   // tres
int four[] = {1, 1, 0, 0, 1, 1, 0};   // cuatro 
int five[] = {1, 1, 0, 1, 1, 0, 1};   // cinco
int six[] = {1, 1, 1, 1, 1, 0, 1};   // seis
int seven[] = {1, 0, 0, 0, 1, 1, 1};   // siete
int eight[] = {1, 1, 1, 1, 1, 1, 1}; // ocho
int nine[] = {1, 1, 0, 1, 1, 1, 1};   // nueve
int ten[] = {1, 1, 1, 0, 1, 1, 1};   // diez, A
int eleven[] = {1, 1, 1, 1, 1, 0, 0};   // once, b
int twelve[] = {0, 1, 1, 1, 0, 0, 1};   // doce, C
int thirteen[] = {1, 0, 1, 1, 1, 1, 0};   // trece, d
int fourteen[] = {1, 1, 1, 1, 0, 0, 1};   // catorce, E
int fifteen[] = {1, 1, 1, 0, 0, 0, 1};   // quince, F
//se declara contador
unsigned char contador = 0;
//función que despliega del 0 al F
void segment_display(unsigned char valor)
{
    switch(valor)
    {
        case 0:
                    for (int i = 0; i<7; i++) digitalWrite(LEDs[i], zero[i]);
                    break;
        case 1:
                    for (int i = 0; i<7; i++) digitalWrite(LEDs[i], one[i]);
                    break;
        case 2:
                    for (int i = 0; i<7; i++) digitalWrite(LEDs[i], two[i]);
                    break;
        case 3:
                    for (int i = 0; i<7; i++) digitalWrite(LEDs[i], three[i]);
                    break;
        case 4:
                    for (int i = 0; i<7; i++) digitalWrite(LEDs[i], four[i]);
                    break;
        case 5:
                    for (int i = 0; i<7; i++) digitalWrite(LEDs[i], five[i]);
                    break;
        case 6:
                    for (int i = 0; i<7; i++) digitalWrite(LEDs[i], six[i]);
                    break;
        case 7:
                    for (int i = 0; i<7; i++) digitalWrite(LEDs[i], seven[i]);
                    break;
        case 8:
                    for (int i = 0; i<7; i++) digitalWrite(LEDs[i], eight[i]);
                    break;
        case 9:
                    for (int i = 0; i<7; i++) digitalWrite(LEDs[i], nine[i]);
                    break;
        case 10:
                    for (int i = 0; i<7; i++) digitalWrite(LEDs[i], ten[i]);
                    break;
        case 11:
                    for (int i = 0; i<7; i++) digitalWrite(LEDs[i], eleven[i]);
                    break;
        case 12:
                    for (int i = 0; i<7; i++) digitalWrite(LEDs[i], twelve[i]);
                    break;
        case 13:
                    for (int i = 0; i<7; i++) digitalWrite(LEDs[i], thirteen[i]);
                    break;
        case 14:
                    for (int i = 0; i<7; i++) digitalWrite(LEDs[i], fourteen[i]);
                    break;
        case 15:
                    for (int i = 0; i<7; i++) digitalWrite(LEDs[i], fifteen[i]);
                    break; 
        default:
                    for (int i = 0; i<7; i++) digitalWrite(LEDs[i], zero[i]);
                    break;          
    }
}


/*PWM */
// the number of the LED pin
const int ledPin = 32; // 32 corresponds to GPIO32

// setting PWM properties
const int freq = 5000;
const int ledChannel = 0;
const int resolution = 8;


void pruebaDisplay(){
  segment_display(contador);
    delay(1000);
    if(contador < 15) contador++;
    else contador = 0;
}

void pruebaPWM(){
  // increase the LED brightness
  for(int dutyCycle = 0; dutyCycle <= 255; dutyCycle++)
  {
  // changing the LED brightness with PWM
  ledcWrite(ledChannel, dutyCycle);
  delay(1);
  }
  
  // decrease the LED brightness
  for(int dutyCycle = 255; dutyCycle >= 0; dutyCycle--)
  {
  // changing the LED brightness with PWM
  ledcWrite(ledChannel, dutyCycle);
  delay(1);
  }
}

void pir_setup(){
  pinStatePrevious = pinStateCurrent; // store old state
  pinStateCurrent = digitalRead(PIN_TO_SENSOR);   // read new state

  if (pinStatePrevious == LOW && pinStateCurrent == HIGH) 
  {   // pin state change: LOW -> HIGH
    Serial.println("Motion detected!");
    pirValue = 1;
    // TODO: turn on alarm, light or activate a device ... here
  }
  else if (pinStatePrevious == HIGH && pinStateCurrent == LOW) 
  {   // pin state change: HIGH -> LOW
    
    Serial.println("Motion stopped!");
    pirValue = 0;
    // TODO: turn off alarm, light or deactivate a device ... here
  }
  
  }

  void dht11_setup(){
        // Wait a few seconds between measurements.
    
      // Reading temperature or humidity takes about 250 milliseconds!
      // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
       h = dht.readHumidity();
      // Read temperature as Celsius (the default)
       temp = (int)dht.readTemperature();
      // Read temperature as Fahrenheit (isFahrenheit = true)
       f = dht.readTemperature(true);
    
      // Check if any reads failed and exit early (to try again).
      if (isnan(h) || isnan(t) || isnan(f)) 
      {
        Serial.println(F("Failed to read from DHT sensor!"));
        return;
      }
    
      // Compute heat index in Fahrenheit (the default)
       hif = dht.computeHeatIndex(f, h);
      // Compute heat index in Celsius (isFahreheit = false)
       hic = dht.computeHeatIndex(t, h, false);
    

  }

void ultras_setup(){
      // Clears the trigPin
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    // Sets the trigPin on HIGH state for 10 micro seconds
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
  
    // Reads the echoPin, returns the sound wave travel time in microseconds
    duration = pulseIn(echoPin, HIGH);
  
    // Calculate the distance
    distanceCm = duration * SOUND_SPEED/2;
  
    // Convert to inches
    distanceInch = distanceCm * CM_TO_INCH;

}

void init_Wifi(){
   // WPA2 enterprise magic starts here
    WiFi.disconnect(true);      
    WiFi.mode(WIFI_STA);   //init wifi mode
    Serial.printf("Connecting to WiFi: %s ", ssid);
    //esp_wifi_sta_wpa2_ent_set_ca_cert((uint8_t *)incommon_ca, strlen(incommon_ca) + 1);
    esp_wifi_sta_wpa2_ent_set_identity((uint8_t *)EAP_IDENTITY, strlen(EAP_IDENTITY));
    esp_wifi_sta_wpa2_ent_set_username((uint8_t *)EAP_IDENTITY, strlen(EAP_IDENTITY));
    esp_wifi_sta_wpa2_ent_set_password((uint8_t *)EAP_PASSWORD, strlen(EAP_PASSWORD));
    //esp_wifi_sta_wpa2_ent_enable();
    esp_wpa2_config_t configW = WPA2_CONFIG_INIT_DEFAULT();
    esp_wifi_sta_wpa2_ent_enable(&configW);

    
    // WPA2 enterprise magic ends here
    WiFi.begin(ssid);
  
    while (WiFi.status() != WL_CONNECTED)
    {
        Serial.print(".");
        delay(300);
    }
    Serial.println();
    Serial.print("Connected with IP: ");
    Serial.println(WiFi.localIP());
    Serial.println();

    /* Assign the api key (required) */
    config.api_key = API_KEY;

    /* Assign the RTDB URL (required) */
    config.database_url = DATABASE_URL;

    /* Sign up */
    if (Firebase.signUp(&config, &auth, "", ""))
    {
        Serial.println("ok");
        signupOK = true;
    }
    else
    {
        Serial.printf("%s\n", config.signer.signupError.message.c_str());
    }

    /* Assign the callback function for the long running token generation task */
    config.token_status_callback = tokenStatusCallback; //see addons/TokenHelper.h
  
    Firebase.begin(&config, &auth);
    Firebase.reconnectWiFi(true);
}

void setup() {
  // put your setup code here, to run once:
   Serial.begin(115200);            // initialize serial

  //Sensor PIR
  pinMode(PIN_TO_SENSOR, INPUT); // set ESP32 pin to input mode to read value from OUTPUT pin of sensor

  //Sensor de humedad
  dht.begin();

  //sensor ultrasonico  
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input

    //display de 7 segmenos
  for (int i = 0; i<7; i++) pinMode(LEDs[i], OUTPUT);

//PWM
// configure LED PWM functionalitites
ledcSetup(ledChannel, freq, resolution);

// attach the channel to the GPIO to be controlled
ledcAttachPin(ledPin, ledChannel);

  init_Wifi();


  
}

void loop() {
    ultras_setup();
    dht11_setup();
    pir_setup();
    // Prints the distance in the Serial Monitor


     if (Firebase.ready() && signupOK && (millis() - sendDataPrevMillis > 2000 || sendDataPrevMillis == 0))
    {
        sendDataPrevMillis = millis();
        
        // temperature
        if (Firebase.RTDB.setInt(&fbdo, "test/temp", temp))
        {
            Serial.println("PASSED");
            Serial.println("PATH: " + fbdo.dataPath());
            Serial.println("TYPE: " + fbdo.dataType());
        }
        else 
        {
            Serial.println("FAILED");
            Serial.println("REASON: " + fbdo.errorReason());
        }


        // humidity
        if (Firebase.RTDB.setInt(&fbdo, "ejemplo/humidity", h))
        {
            Serial.println("PASSED");
            Serial.println("PATH: " + fbdo.dataPath());
            Serial.println("TYPE: " + fbdo.dataType());
        }
        else 
        {
            Serial.println("FAILED");
            Serial.println("REASON: " + fbdo.errorReason());
        }
        
        //count++;
    
        // Write an Float number on the database path test/float
        if (Firebase.RTDB.setFloat(&fbdo, "ejemplo/distance", distanceCm))
        {
            Serial.println("PASSED");
            Serial.println("PATH: " + fbdo.dataPath());
            Serial.println("TYPE: " + fbdo.dataType());
        }
        else 
        {
            Serial.println("FAILED");
            Serial.println("REASON: " + fbdo.errorReason());
        }
                // Write an Float number on the database path test/float
        if (Firebase.RTDB.setFloat(&fbdo, "ejemplo/move", pirValue))
        {
            Serial.println("PASSED");
            Serial.println("PATH: " + fbdo.dataPath());
            Serial.println("TYPE: " + fbdo.dataType());
        }
        else 
        {
            Serial.println("FAILED");
            Serial.println("REASON: " + fbdo.errorReason());
        }



        
        //lee primer dato
       if (Firebase.RTDB.getString(&fbdo, "/ejemplo/digito")) 
        //if (Firebase.RTDB.getInt(&fbdo, "/test/digito")) 
        {
             if (fbdo.dataType() == "string")
            //if (fbdo.dataType() == "int") 
            {
                sValue = fbdo.stringData();
                //intValue = fbdo.intData();
                intValue = sValue.toInt();
                segment_display(intValue);
                Serial.println(intValue);
            }
        }
        else 
        {
            Serial.println(fbdo.errorReason());
        }
        //lee segundo dato
        //if (Firebase.RTDB.getInt(&fbdo, "/ejemplo/pwm")) 
        if (Firebase.RTDB.getString(&fbdo, "/ejemplo/pwm")) 
        {
           if (fbdo.dataType() == "string") 
            //if (fbdo.dataType() == "int") 
            {
                //pwmValue = fbdo.intData();
                pValue = fbdo.stringData();
                pwmValue = pValue.toInt();
                ledcWrite(ledChannel,pwmValue); 
                Serial.println(pwmValue);
            }
        }
        else 
        {
            Serial.println(fbdo.errorReason());
        }
    }


   
}
