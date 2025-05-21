class WeatherExpertSystem:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, lp_conditions, lp_result):
        self.rules.append((lp_conditions, lp_result))

    def infer(self):
        for conditions, result in self.rules:
            if all(condition in self.facts for condition in conditions):
                return result
        return "Default"

expert_system = WeatherExpertSystem()
expert_system.add_fact("high_temperature")
expert_system.add_fact("low_humidity")  
expert_system.add_fact("fog")  
expert_system.add_fact("Night") 
expert_system.add_fact("wind")  
expert_system.add_fact("low_temperature")  
expert_system.add_rule(["low_temperature", "wind"], "Not Comfortable")
expert_system.add_rule(["high_temperature", "low_humidity"], "Comfortable")
expert_system.add_rule(["fog", "Night"], "Low visibility")

result = expert_system.infer()
print(result)  