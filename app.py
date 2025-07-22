from flask import Flask, render_template, redirect, url_for
try:
    from gpiozero import LED
    gpio_available = True
except ImportError:
    gpio_available = False

app = Flask(__name__)

# If running on Raspberry Pi, setup GPIO pins
if gpio_available:
    devices = {
        "light": LED(17),
        "fan": LED(27)
    }
else:
    # Fallback: mock objects for non-Raspberry environments
    class MockDevice:
        def __init__(self):
            self._state = False
        def on(self):
            self._state = True
        def off(self):
            self._state = False
        @property
        def value(self):
            return self._state
    devices = {
        "light": MockDevice(),
        "fan": MockDevice()
    }

@app.route('/')
def index():
    return render_template('index.html', devices=devices)

@app.route('/toggle/<name>')
def toggle(name):
    device = devices.get(name)
    if device:
        if device.value:
            device.off()
        else:
            device.on()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
