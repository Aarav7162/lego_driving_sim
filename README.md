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
  Reads the controller for steering and throttle. Converts brake inputs from the cloud into keypresses.

- dashboard.html  
  Displays live braking values from Ninja IoT cloud. Updates every 200ms.

- esp_brake.ino  
  Reads brake pedal and writes `braking_value` to Ninja IoT.

- images/  
  The photos of the steering controller and pedals. I'll be linking this repository with a rebrickable page soon for the tutorial if anyone wants to build it. I'll post the building tips there. Just look up Aarav7162 on rebrickable and keep an eye out (i'll update the repo too).

---

## How It Works

1. ESP8266 reads the LEGO brake pedal and writes `braking_value` to Ninja IoT.
2. Python controller server:
   - Reads steering inputs from the game controller.
   - Converts brake inputs from the cloud into `S` (RT) or `D` (LT) keypresses.
   - Automatically handles controller calibration if multiple controllers are present.
3. Dashboard fetches `braking_value` from Ninja IoT every 200ms and displays it live.

---

## Getting Started

1. Flash the ESP8266  
   - Open esp_brake.ino.  
   - Set your Wi-Fi SSID/password/UID and configure the ultrasonic sensor pins.  

2. Install Python Dependencies  
   ```bash
   pip install pygame pyautogui flask requests
   pip install pynput
   pip install keyboard // You'll need the admin login for this

3. Run the Controller Server

    Start the Python server:
    ```bash
    python controller_server.py

4. Open the Dashboard

   Open `dashboard.html` in a browser. You’ll see live updates for: 
   - **Brake**  

5. Controls
   - Right stick forward (throttle): Directly controls acceleration in the game. Is connected to the pneumatic pedals.
   - Brake pedal (cloud): Presses and holds `S` when value exceeds threshold. Is connected to the pneumatic pedals.
   - Steering wheel: Mechanically connected to a controller. Converted to keyboard input via Python script with:
      - LT: Presses and holds `D`.
      - RT: Presses and hold `A`


## Credits
>  **Hardware, ESP and Python logic**: Aarav Kapasi  
>  **HTML dashboard**: Generated with AI and customized by Aarav Kapasi  
