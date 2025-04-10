# inverter.py (Expanded)
class Inverter:
    def __init__(self):
        self.input_power = 0.0  # in Watts
        self.output_power = 0.0  # in Watts
        self.efficiency = 0.9
        self.status = 'IDLE'
        self.temperature = 30.0

    def convert(self, input_power):
        self.input_power = input_power
        self.output_power = round(input_power * self.efficiency, 2)
        self._update_temperature()
        self.status = 'ACTIVE' if input_power > 0 else 'IDLE'
        return self.output_power

    def _update_temperature(self):
        if self.output_power > 500:
            self.temperature += 2.5
        else:
            self.temperature -= 1.0
        self.temperature = max(25.0, min(80.0, round(self.temperature, 1)))

    def adjust_efficiency(self):
        if self.temperature > 60:
            self.efficiency -= 0.01
        elif self.temperature < 30:
            self.efficiency += 0.005
        self.efficiency = max(0.85, min(0.95, round(self.efficiency, 3)))

    def get_energy_output(self, duration_hrs):
        return round((self.output_power / 1000) * duration_hrs, 3)

    def get_status(self):
        return {
            'input_power': self.input_power,
            'output_power': self.output_power,
            'efficiency': self.efficiency,
            'temperature': self.temperature,
            'status': self.status
        }
