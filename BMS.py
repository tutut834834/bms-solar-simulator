# BMS.py (Expanded for full interaction)
import time
import matplotlib.pyplot as plt
from battery import Battery
from solar import SolarPanel
from inverter import Inverter
from controller import Controller
from motor import Motor

battery = Battery()
solar = SolarPanel()
inverter = Inverter()
controller = Controller()
motor = Motor()

# Setup real-time plotting
plt.ion()
fig, axs = plt.subplots(3, 2, figsize=(12, 9))
labels = ['Battery Voltage [V]', 'SOC [%]', 'Solar Output [W]', 'Inverter Output [W]', 'Motor Load [W]', 'System Mode']
data = [[] for _ in range(6)]
timestamps = []

for cycle in range(10000):
    now = cycle * 0.5
    timestamps.append(now)

    solar.simulate_cloud_cover()
    solar.simulate_dirt()
    solar_output = solar.generate_power()

    battery.simulate_imbalance()
    battery.update_status()
    motor.update_load()
    mode = controller.manage_power(battery.soc, solar_output, motor.load)

    energy_from_solar = solar.get_energy(0.5 / 60)  # per cycle
    power_to_motor = motor.consumption

    if mode == 'CHARGING':
        battery.charge(energy_from_solar)
    elif mode == 'SUPPLYING':
        battery.discharge(power_to_motor, 0.5 / 60)

    inverter_output = inverter.convert(solar_output if mode == 'CHARGING' else motor.load)
    inverter.adjust_efficiency()

    statuses = [
        battery.voltage,
        battery.soc,
        solar_output,
        inverter_output,
        motor.load,
        {'IDLE': 0, 'CHARGING': 1, 'SUPPLYING': 2, 'MAINTAINING': 3, 'CRITICAL': 4}[mode]
    ]

    for i in range(6):
        data[i].append(statuses[i])
        axs[i//2][i%2].cla()
        axs[i//2][i%2].plot(timestamps, data[i], label=labels[i])
        axs[i//2][i%2].set_title(labels[i])
        axs[i//2][i%2].legend()
        axs[i//2][i%2].grid(True)

    plt.tight_layout()
    plt.pause(0.1)

plt.ioff()
plt.show()

print("\nFinal Statuses:")
print("Battery:", battery.get_status())
print("Solar:", solar.get_status())
print("Inverter:", inverter.get_status())
print("Motor:", motor.get_status())
print("Controller:", controller.get_status())
