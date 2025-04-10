# solar.py (Expanded)
import random

class SolarPanel:
    def __init__(self):
        self.power_output = 0.0  # in Watts
        self.efficiency = 0.18  # Panel efficiency
        self.surface_area = 1.6  # m²
        self.sunlight_intensity = 0.0  # W/m²

    def generate_power(self):
        self.sunlight_intensity = round(random.uniform(200, 1000), 2)
        self.power_output = round(self.surface_area * self.sunlight_intensity * self.efficiency, 2)
        return self.power_output

    def get_energy(self, duration_hrs):
        return round((self.power_output / 1000) * duration_hrs, 3)  # kWh

    def simulate_cloud_cover(self):
        if random.random() < 0.3:
            self.sunlight_intensity *= random.uniform(0.4, 0.8)

    def simulate_dirt(self):
        if random.random() < 0.2:
            self.efficiency -= random.uniform(0.01, 0.03)
            self.efficiency = max(0.10, self.efficiency)

    def clean_panel(self):
        self.efficiency = min(0.18, self.efficiency + 0.01)

    def get_status(self):
        return {
            'power_output': self.power_output,
            'efficiency': round(self.efficiency, 2),
            'sunlight_intensity': self.sunlight_intensity,
            'surface_area': self.surface_area
        }
