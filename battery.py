# battery.py (Expanded)
import random

class Battery:
    def __init__(self, cell_count=12):
        self.cell_count = cell_count
        self.cells = self._init_cells()
        self.voltage = 0.0  # in Volts
        self.temperature = 25.0  # in Celsius
        self.soc = 100.0  # State of Charge in percentage
        self.capacity = 2.5  # kWh
        self.energy_stored = self.capacity  # kWh
        self.health = 100.0  # percentage
        self.nominal_voltage = 3.7 * cell_count
        self.internal_resistance = 0.05  # Ohms

    def _init_cells(self):
        return [{
            'voltage': round(random.uniform(3.0, 4.2), 2),
            'temperature': round(random.uniform(20, 40), 1),
            'resistance': round(random.uniform(0.03, 0.06), 3)
        } for _ in range(self.cell_count)]

    def update_status(self):
        self.voltage = round(sum(cell['voltage'] for cell in self.cells), 2)
        self.temperature = round(sum(cell['temperature'] for cell in self.cells) / self.cell_count, 1)
        energy_drawn = random.uniform(0.01, 0.05)
        self.energy_stored = max(0.0, self.energy_stored - energy_drawn)
        self.soc = round((self.energy_stored / self.capacity) * 100, 1)
        self.health = max(50.0, self.health - random.uniform(0.01, 0.05))
        return self.get_status()

    def charge(self, energy_input):
        efficiency = 0.95 if self.health >= 60 else 0.85
        added_energy = energy_input * efficiency
        self.energy_stored = min(self.capacity, self.energy_stored + added_energy)
        self.soc = round((self.energy_stored / self.capacity) * 100, 1)

    def discharge(self, power_output, duration_hrs):
        energy_needed = (power_output / 1000) * duration_hrs
        self.energy_stored = max(0.0, self.energy_stored - energy_needed)
        self.soc = round((self.energy_stored / self.capacity) * 100, 1)

    def simulate_imbalance(self):
        if random.random() < 0.1:
            cell = random.choice(self.cells)
            cell['voltage'] = round(random.uniform(2.8, 3.2), 2)
            cell['temperature'] = round(random.uniform(45, 60), 1)

    def get_total_internal_resistance(self):
        return round(sum(cell['resistance'] for cell in self.cells), 3)

    def balance_cells(self):
        avg_voltage = sum(cell['voltage'] for cell in self.cells) / self.cell_count
        for cell in self.cells:
            deviation = cell['voltage'] - avg_voltage
            cell['voltage'] = round(avg_voltage - (deviation * 0.2), 2)

    def get_status(self):
        return {
            'voltage': self.voltage,
            'temperature': self.temperature,
            'soc': self.soc,
            'energy_stored': round(self.energy_stored, 2),
            'capacity': self.capacity,
            'health': self.health,
            'internal_resistance': self.get_total_internal_resistance()
        }
