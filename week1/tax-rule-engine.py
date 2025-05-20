class RuleEngine():
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, result):
        self.rules.append((condition, result))

    def apply_rules(self, input_value):
        for condition, result in self.rules:
            if condition(input_value):
                return result
        return "No rule found"

engine = RuleEngine()
engine.add_rule(lambda x: x < 12570, "0%")
engine.add_rule(lambda x: 12571 <= x < 50270, "20%")
engine.add_rule(lambda x: 50271 <= x < 125140, "40%")
engine.add_rule(lambda x: x > 125140, "45%")

result = engine.apply_rules(12671546456)
print(result)  
