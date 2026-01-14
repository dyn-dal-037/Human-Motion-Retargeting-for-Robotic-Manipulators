#include <WiFi.h>
#include <WebServer.h>
#include "servo_config.h"

// ===== WiFi Credentials =====
const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";

// ===== Web Server =====
WebServer server(80);

// ===== Servo Control Placeholder =====
void writeServo(int id, int angle) {
  angle = constrain(angle, SERVO_MIN_ANGLE, SERVO_MAX_ANGLE);
  // Example:
  // serialServo.write(id, angle);
}

// ===== HTTP Handler =====
void handleSendData() {
  if (!server.hasArg("plain")) {
    server.send(400, "text/plain", "No data received");
    return;
  }

  String data = server.arg("plain");
  data.trim();

  int c1 = data.indexOf(',');
  int c2 = data.indexOf(',', c1 + 1);

  if (c1 == -1 || c2 == -1) {
    server.send(400, "text/plain", "Invalid format");
    return;
  }

  int angle1 = data.substring(0, c1).toInt();
  int angle2 = data.substring(c1 + 1, c2).toInt();
  int angle3 = data.substring(c2 + 1).toInt();

  angle1 = constrain(angle1, SERVO_MIN_ANGLE, SERVO_MAX_ANGLE);
  angle2 = constrain(angle2, SERVO_MIN_ANGLE, SERVO_MAX_ANGLE);
  angle3 = constrain(angle3, SERVO_MIN_ANGLE, SERVO_MAX_ANGLE);

  writeServo(SERVO_ID_1, angle1);
  writeServo(SERVO_ID_2, angle2);
  writeServo(SERVO_ID_3, angle3);

  server.send(200, "text/plain", "OK");
}

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

  Serial.print("[INFO] ESP32 IP: ");
  Serial.println(WiFi.localIP());

  server.on("/sendData", HTTP_POST, handleSendData);
  server.begin();

  Serial.println("[INFO] Web server started");
}

void loop() {
  server.handleClient();
}
