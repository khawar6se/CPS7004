class WeatherExpertSystem:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, conditions, result):
        self.rules.append((conditions, result))

    def infer(self):
        for conditions, result in self.rules:
            if all(condition in self.facts for condition in conditions):
                return result
        return "Default"

expert_system = WeatherExpertSystem()
expert_system.add_fact("high_temperature") 
expert_system.add_fact("low_temperature") 
expert_system.add_fact("high_humidity") 
expert_system.add_fact("low_humidity") 
expert_system.add_fact("high speed of air") 
expert_system.add_fact("Tstrom") 

expert_system.add_rule(["high_temperature", "low_humidity"], "Comfortable")
expert_system.add_rule(["low_temperature", "high_humidity"], "Comfortable")
result = expert_system.infer()
print(result)