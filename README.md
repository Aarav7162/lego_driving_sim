# LEGO Pneumatic Pedals & Steering Controller Dashboard

This is a custom LEGO build with pneumatic pedals and steering wheel. It uses the ESP8266 and a Xbox contoller to convert it into a working PC controller.

With this setup:  
- The gas pedal (controlled by pneumatic pressure) is mapped to the controller's right stick forward.  
- The brake pedal uses an ultrasonic sensor on an ESP8266.  
- The steering wheel can be mapped to joystick or keyboard inputs. It uses an Xbox controller and a mechanically contolled steering wheel (photos attached under images/)  
- Everything is displayed live on the HTML dashboard.  

---

## Repository Contents

- controller_server.py  
  Reads the Xbox controller and the ESP for brake data, simulates keyboard keypresses (W for accelerate), and sends live data to the dashboard (the dashboard was made completely with ChatGPT, along with some server logic for the ESP too).

- dashboard.html  
  A dashboard that fetches throttle, steering and brake values. Works in any browser.  

- esp_brake.ino  
  ESP8266 code for the brake pedal. Reads distance from the ultrasonic sensor, applies smoothing, and serves the processed value over Wi-Fi at /brake.

- images/  
  The photos of the steering controller and pedals. I'll be linking this repository with a rebrickable page soon for the tutorial if anyone wants to build it. I'll post the building tips there. Just look up Aarav7162 on rebrickable and keep an eye out (i'll update the repo too).

---

## How It Works

1. ESP8266 and Ultrasonic Sensor  
   The ESP measures the brake pedal’s distance. A small filter smooths out tiny movements so the brake feels natural. The ESP hosts a HTTP endpoint (/brake) that returns this value.

2. Python Controller Server  
   - Reads your controller’s right stick forward to detect acceleration.  
   - Automatically presses and releases the W key using pyautogui when throttle exceeds the threshold (around 0.05 on the right stick of the controller).  
   - Reads the ESP for real-time brake values.  
   - Serves both throttle and brake data to the dashboard at http://localhost:5000/data.  

3. Dashboard  
   - Open dashboard.html in any browser.  
   - Fetches live JSON data every 200 ms.  
   - Displays acceleration, brake, and smoothed motion.   

---

## Getting Started

1. Flash the ESP8266  
   - Open esp_brake.ino.  
   - Set your Wi-Fi SSID/password and configure the ultrasonic sensor pins.  
   - Upload to your ESP and check the Serial Monitor for its IP address.  
   - Update ESP_IP in controller_server.py with this address.  

2. Install Python Dependencies  
   ```bash
   pip install pygame pyautogui flask requests

3. Run the Controller Server

    Start the Python server:
    ```bash
    python controller_server.py

4. Open the Dashboard

   Open `dashboard.html` in a browser. You’ll see live updates for:

   - **Throttle**  
   - **Brake**  

5. Controls
   - **Right stick forward**: Presses `W` automatically  
   - **Brake pedal movement**: Updates live using the ESP’s **quadratic motion detection**

# Credits
>  **Hardware and Python logic**: Aarav Kapasi  
>  **HTML dashboard and ESP snippets**: Generated with AI and customized by Aarav Kapasi  
