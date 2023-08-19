#include <ArduinoJson.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#define ledPin D7

const char* ssid = "Redmi Note 9";
const char* password = "vibharavi";
const char* mqttServer = "demo.thingsboard.io";
const char* deviceToken = "Ledrvcedevice";

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
  setupWifi();
  client.setServer(mqttServer, 1883);
}

void setupWifi() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void reconnect() {
  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");
    if (client.connect(deviceToken)) {
      Serial.println("Connected to MQTT");
    } else {
      Serial.print("Failed with state ");
      Serial.print(client.state());
      delay(2000);
    }
  }
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Send LED state to ThingsBoard
  bool ledState = digitalRead(ledPin);
  String payload = "{\"led_state\": " + String(ledState) + "}";
  client.publish("v1/devices/me/telemetry", payload.c_str());

  delay(1000); // Update every second
}
