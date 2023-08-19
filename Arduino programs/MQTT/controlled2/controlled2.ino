#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#define ledPin D7

const char* ssid = "Redmi Note 9";
const char* password = "vibharavi";
const char* mqttServer = "192.168.186.30";
const int mqttPort = 1883;
const char* deviceAccessToken = "Ledrvcedevice";

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(9600);
  delay(10);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected to WiFi");

  // Set MQTT server and callback function
  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);

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

void callback(char* topic, byte* payload, unsigned int length) {
  // Handle MQTT messages if required
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect with the given client ID and access token
    if (client.connect("ESP8266Client", deviceAccessToken, nullptr)) {
      Serial.println("\nConnected to MQTT broker");
    } else {
      Serial.print("Failed, rc=");
      Serial.print(client.state());
      Serial.println(" Retrying in 5 seconds...");
      delay(5000);
    }
  }
}
