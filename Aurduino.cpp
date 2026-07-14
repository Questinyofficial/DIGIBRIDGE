/*
----------------------------------------------------
Bridge Digital Twin
Sensor Unit v2.0

Sensors
-------
DHT11
HX711 Load Cell

Output Format
-------------
temperature,humidity,load

Example
-------
31.4,65.0,12.37
----------------------------------------------------
Wiring layout
HX711 Pin	Arduino UNO
VCC	        5V
GND	        GND
DT (DOUT)	D3
SCK	        D2
*/

#include <DHT.h>
#include "HX711.h"

// -----------------------------
// DHT11
// -----------------------------
#define DHTPIN 7
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

// -----------------------------
// HX711
// -----------------------------
#define HX711_DT 3
#define HX711_SCK 2

HX711 scale;

// IMPORTANT:
// Replace this after calibration
float calibration_factor = 420.0;

// --------------------------------------------------

void setup()
{
    Serial.begin(9600);

    dht.begin();

    scale.begin(HX711_DT, HX711_SCK);

    delay(1000);

    scale.set_scale(calibration_factor);

    scale.tare();          // Zero the scale

    delay(1000);
}

// --------------------------------------------------

void loop()
{
    float temperature = dht.readTemperature();

    float humidity = dht.readHumidity();

    float load = scale.get_units(10);

    if (load < 0)
        load = 0;

    if (isnan(temperature) || isnan(humidity))
    {
        Serial.println("ERROR");
    }
    else
    {
        Serial.print(temperature, 1);
        Serial.print(",");

        Serial.print(humidity, 1);
        Serial.print(",");

        Serial.println(load, 2);
    }

    delay(2000);
}