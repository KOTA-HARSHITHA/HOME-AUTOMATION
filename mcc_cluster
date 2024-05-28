#include <ESP8266WiFi.h>

const char* ssid = "harshitha";  // Enter SSID here

const char* password = "1010101010";  //Enter Password here

// Variable to store the HTTP request

String header;

String LED1State = "off";
String LED2State = "off";
String LED3State = "off";
String LED4State = "off";

const int LED1 = D1;
const int LED2 = D2;
const int LED3 = D5;
const int LED4 = D6;


WiFiServer server(80);


void setup() {

  Serial.begin(115200);

  pinMode(LED1, OUTPUT);
   pinMode(LED2, OUTPUT);
    pinMode(LED3, OUTPUT);
     pinMode(LED3, OUTPUT);

  digitalWrite(LED1, LOW);
   digitalWrite(LED2, LOW);
     digitalWrite(LED2, LOW);
       digitalWrite(LED4, LOW); 
  

 Serial.print("Connecting to ");

 Serial.println(ssid);

WiFi.begin(ssid,password);



// Print local IP address and start web server

 Serial.println("");
  server.begin();
    Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(">");
  }
  Serial.println();

  Serial.print("Connected, IP address: ");
  Serial.println(WiFi.localIP());
}

 


void loop(){

  WiFiClient client = server.available();   

  if (client) {                             // If a new client connects,

    Serial.println("new client connected");          

    String currentLine = "";                // make a String to hold incoming data from the client

    while (client.connected())

      if (client.available()) {             // if there's bytes to read from the client,

        char c = client.read();             

        Serial.write(c);                    

        header += c;

        if (c == '\n') {                    // if the byte is a newline character

          if (currentLine.length() == 0) {

            client.println("HTTP/1.1 200 OK");

            client.println("Content-type:text/html");

            client.println("Connection: close");

            client.println();


            if (header.indexOf("GET /LED1/on") >= 0) {

              Serial.println("LED1 on");

              LED1State = "on";

              digitalWrite(LED1, HIGH);

            }
            else if (header.indexOf("GET /LED1/off") >= 0) {

              Serial.println("LED1 off");

              LED1State = "off";

              digitalWrite(LED1, LOW);

            } 
             else if (header.indexOf("GET /LED2/on") >= 0) {

              Serial.println("LED2 on");

              LED2State = "on";

              digitalWrite(LED2, HIGH);

            } 
             else if (header.indexOf("GET /LED2/off") >= 0) {

              Serial.println("LED2 off");

              LED2State = "off";

              digitalWrite(LED2, LOW);

            } 
            else if (header.indexOf("GET /LED3/on") >= 0) {

              Serial.println("LED3 on");

              LED3State = "on";

              digitalWrite(LED3, HIGH);

            } 
            else if (header.indexOf("GET /LED3/off") >= 0) {

              Serial.println("LED3 off");

              LED3State = "off";

              digitalWrite(LED3, LOW);

            } 
            else if (header.indexOf("GET /LED4/on") >= 0) {

              Serial.println("LED4 on");

              LED4State = "on";

              digitalWrite(LED4, HIGH);

            } 
            else if (header.indexOf("GET /LED4/off") >= 0) {

              Serial.println("LED4 off");

              LED4State = "off";

              digitalWrite(LED4, LOW);

            } 

            

            // Display the HTML web page

            client.println("<!DOCTYPE html><html>");

            client.println("<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">");

            client.println("<link rel=\"icon\" href=\"data:,\">");

            client.println("<style>html { font-family: Cairo; display: inline; margin: 0px auto; text-align: center; background-color: #3D3D3D;} button{cursor:pointer;}");

            client.println(".button { background-color:  #000000;border: 3px solid rgba(0, 0, 0, 0.32); color: #5EECFF; padding: 16px 40px;}");

      //  For home page button
             client.println(".buttonh { background-color: #017e02; color: white; padding: 16px 40px;}");

            client.println("text-decoration: none; font-size: 35px; margin: 2px; cursor: pointer;}");

            client.println(".button2 {background-color: #555555;}</style></head>");

        

           

          

            // Web Page Heading

            client.println("<body>");

        //     Home button 
             client.println("<p><a href=\"https://danieldominicsaviokennedy.github.io/Smart-SwitchBoard3/\"><button class=\"buttonh\">HOME</button></a></p><br><br>");
            

            // If the LED1State is off, it displays the ON button       

            if (LED1State=="off") {
            //   client.println("<h1>Switch-1</h1>");
              client.println("<p><a href=\"/LED1/on\"><button class=\"button\">S-1 ON</button></a></p>");
              }
            else {
              //   client.println("<h1>Switch-1</h1>");
              client.println("<p><a href=\"/LED1/off\"><button class=\"button button2\">S-1 OFF</button></a></p>");
              }  
           if (LED2State=="off") {
             //  client.println("<h1>Switch-2</h1>");
         
              client.println("<p><a href=\"/LED2/on\"><button class=\"button\">S-2 ON</button></a></p>");
              }
            else {
              //  client.println("<h1>Switch-2</h1>");
              client.println("<p><a href=\"/LED2/off\"><button class=\"button button2\">S-2 OFF</button></a></p>");
              }     
           if (LED3State=="off") {
                //   client.println("<h1>Switch-3</h1>");
              client.println("<p><a href=\"/LED3/on\"><button class=\"button\">S-3 ON</button></a></p>");
              }
            else {
               //  client.println("<h1>Switch-3</h1>");
              client.println("<p><a href=\"/LED3/off\"><button class=\"button button2\">S-3 OFF</button></a></p>");
              }
            if (LED4State=="off") {
               //  client.println("<h1>Switch-4</h1>");
              client.println("<p><a href=\"/LED4/on\"><button class=\"button\">S-4 ON</button></a></p>");
              }
            else {
              //    client.println("<h1>Switch-4</h1>");
              client.println("<p><a href=\"/LED4/off\"><button class=\"button button2\">S-4 OFF</button></a></p>");
              }            

            client.println("</body></html>");

            client.println();

            break;

          } else { 

            currentLine = "";

          }

        } else if (c != '\r') {  

          currentLine += c;      

        }

      }

    }

    header = "";

    client.stop();

    Serial.println(WiFi.localIP());

    Serial.println("");

  }
