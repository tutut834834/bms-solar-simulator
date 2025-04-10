# motor.py (Expanded)
import random

class Motor:
    def __init__(self):
        self.load = 0.0  # in Watts
        self.consumption = 0.0  # in Watts
        self.rpm = 0
        self.torque = 0.0  # Nm
        self.temperature = 30.0

    def update_load(self):
        self.load = round(random.uniform(100.0, 1500.0), 2)
        self.rpm = int((self.load / 10) + random.uniform(-50, 50))
        self.torque = round(random.uniform(0.2, 2.0), 2)
        self.consumption = round(self.load * 0.9, 2)
        self._update_temperature()

    def _update_temperature(self):
        self.temperature += (self.load / 1000) * 1.5
        self.temperature = max(30.0, min(90.0, round(self.temperature, 1)))

    def cool_down(self):
        self.temperature = max(30.0, self.temperature - random.uniform(1.0, 3.0))

    def get_energy_used(self, duration_hrs):
        return round((self.consumption / 1000) * duration_hrs, 3)

    def get_status(self):
        return {
            'load': self.load,
            'consumption': self.consumption,
            'rpm': self.rpm,
            'torque': self.torque,
            'temperature': self.temperature
        }
