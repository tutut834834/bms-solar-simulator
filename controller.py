# controller.py (Expanded)
class Controller:
    def __init__(self):
        self.mode = 'IDLE'
        self.logs = []
        self.override = False
        self.forced_mode = None
        self.last_command_time = 0.0

    def manage_power(self, battery_soc, solar_output, motor_load):
        if self.override and self.forced_mode:
            self.mode = self.forced_mode
            self._log(f"Override mode: {self.mode}")
            return self.mode

        if battery_soc < 15:
            self.mode = 'CRITICAL'
        elif battery_soc < 80 and solar_output > 150:
            self.mode = 'CHARGING'
        elif battery_soc >= 95 and solar_output < 100:
            self.mode = 'IDLE'
        elif motor_load > 500:
            self.mode = 'SUPPLYING'
        else:
            self.mode = 'MAINTAINING'

        self._log(f"Mode set to: {self.mode} "
                  f"(SOC: {battery_soc}%, Solar: {solar_output}W, Load: {motor_load}W)")
        return self.mode

    def force_mode(self, mode):
        valid_modes = ['IDLE', 'CHARGING', 'SUPPLYING', 'MAINTAINING', 'CRITICAL']
        if mode in valid_modes:
            self.override = True
            self.forced_mode = mode
            self._log(f"Force mode enabled: {mode}")
        else:
            self._log(f"Attempted to force invalid mode: {mode}")

    def release_override(self):
        if self.override:
            self._log("Override released")
            self.override = False
            self.forced_mode = None
        else:
            self._log("No override to release")

    def get_status(self):
        return {
            'mode': self.mode,
            'override': self.override,
            'forced_mode': self.forced_mode,
            'log_count': len(self.logs),
            'recent_log': self.logs[-1] if self.logs else 'No logs yet.'
        }

    def get_logs(self, last_n=5):
        return self.logs[-last_n:]

    def _log(self, message):
        self.logs.append(message)
        if len(self.logs) > 100:
            self.logs.pop(0)
