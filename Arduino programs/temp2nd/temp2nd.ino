#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

#define DHTPIN D1       // DHT11 data pin (GPIO5 on NodeMCU)
#define DHTTYPE DHT11   // DHT11 sensor type

const char* ssid = "Redmi Note 9";
const char* password = "vibharavi";
const char* mqttServer = "192.168.186.30";
const int mqttPort = 1883;
const char* deviceAccessToken = "dht11rvcedevice";

WiFiClient espClient;
PubSubClient client(espClient);
DHT dht(DHTPIN, DHTTYPE);

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

  // Start DHT sensor
  dht.begin();
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Read DHT11 sensor data
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  // Check if any reads failed and exit early (to try again).
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Publish data to ThingsBoard
  String payload = String("{\"temperature\":") + temperature + ",\"humidity\":" + humidity + "}";
  String topic = "v1/devices/me/telemetry"; // ThingsBoard telemetry topic
  client.publish(topic.c_str(), payload.c_str());
  Serial.println("PUBLISHED");

  delay(5000);  // Publish data every 5 seconds
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
