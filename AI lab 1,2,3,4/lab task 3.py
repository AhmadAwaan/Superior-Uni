class ModelBasedReflexAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature
        self.model = {}  

    def perceive(self, room, current_temperature):
        
        self.model[room] = current_temperature
        return current_temperature

    def act(self, room):
        current_temperature = self.model.get(room)
        if current_temperature is None:
            return "No temperature data for this room."

        if current_temperature < self.desired_temperature:
            action = "Turn on heater"
        else:
            action = "Turn off heater"
        return action


rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24
}

desired_temperature = 22
agent = ModelBasedReflexAgent(desired_temperature)

for room, temperature in rooms.items():
    agent.perceive(room, temperature)  
    action = agent.act(room)           
    print(f"{room}: Current temperature = {temperature}°C. {action}.")
