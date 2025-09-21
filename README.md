# LEGO Pneumatic Pedals + Steering Controller Dashboard

This project turns a custom LEGO pneumatic pedal + steering wheel build into a fully working PC controller with a live dashboard.

- **Pedals:** LEGO pneumatic assemblies.  
  - Gas pedal mapped from a gamepad’s right stick forward.
  - Brake pedal uses an ultrasonic sensor on an ESP8266 with simple quadratic motion detection to smooth out distance and realys speed changes.
- **Steering:** Custom LEGO steering wheel with LT/RT inputs or joystick mapping.

The program (python) reads all of these, simulates keyboard keypresses (`W` for throttle) and displays live throttle/brake values on a stylish HTML dashboard.

---

## Repository Contents:

- controller_server.py
  Python script. Reads joystick, polls ESP for brake value, holds/releases `W`, and runs a Flask server to provide JSON to the dashboard.

- dashboard.html
  HTML+CSS dashboard with a liquid glass look. Fetches live throttle and brake values from the Python server.

- esp_brake.ino
  ESP8266 sketch. Reads ultrasonic sensor distance, applies a small quadratic smoothing step to better reflect pedal motion, and serves the value at `/brake` over Wi-Fi.

- images/
  Photos of the LEGO steering wheel and pneumatic pedal build. Add your pictures here for documentation.


---

## How It Works

1. **ESP8266 + Ultrasonic Sensor**  
   The ESP8266 measures brake pedal distance using an ultrasonic sensor. A lightweight quadratic filter is applied so that small pedal movements translate to smooth “acceleration” values. It hosts a minimal HTTP endpoint at `/brake` that returns this processed number.

2. **Python script**  
   - Uses `pygame` to read the right stick forward of your controller.
   - Uses `pyautogui` to press and release the `W` key automatically when throttle > deadzone.
   - Polls the ESP endpoint for brake values in real time.
   - Serves both throttle and the processed brake/acceleration data via Flask at `http://localhost:5000/data`.

3. **Dashboard (`dashboard.html`)**  
   - Opens in any browser.
   - Fetches JSON from `http://localhost:5000/data` every 200 ms.
   - Displays throttle, brake and the smoothed motion values with a sleek liquid-glass panel.

---

## Installation & Usage

1. Flash `esp_brake.ino` to your ESP8266. Edit SSID/password and ultrasonic pins to match your hardware. After it connects to Wi-Fi, note the IP address printed in Serial Monitor. Hard-set this IP in `controller_server.py` under `ESP_IP`.

2. On your PC:
   ```bash
   pip install pygame pyautogui flask requests
   python controller_server.py

3. Run the Controller Server  

    ```bash
    python controller_server.py

4. Open the Dashboard  

Open `dashboard.html` in your browser to launch the live dashboard.  
You’ll see **Throttle**, **Brake**, and **smoothed Motion** values update in real time.

- **Push the right stick forward**: `W` will be held down automatically.  
- **Move your brake pedal**: the ultrasonic sensor’s **quadratic motion detection** updates live.  

---

## Credits  

- **Hardware design and integration**, and most of the Python logic: Aarav Kapasi 
- **HTML dashboard styling** and certain ESP8266 code blocks were generated with the help of AI and then configured by Aarav Kapasi    
