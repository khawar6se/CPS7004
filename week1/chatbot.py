class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, response):
        self.rules.append({"condition": condition, "response": response})

    def apply_rules(self, text):
        for rule in self.rules:
            if rule["condition"] in text.lower():
                return f"Bot: {rule['response']}"
        return "Bot: I don't understand."

# Example usage
rule_engine = RuleEngine()

# Add rules
rule_engine.add_rule("hello", "Hi there!")
rule_engine.add_rule("good bye", "Goodbye!")
rule_engine.add_rule("goodbye", "Have a nice day!")
rule_engine.add_rule("what is your name", "I am a chat bot!")
rule_engine.add_rule("hi", "Hello")
rule_engine.add_rule("Hello", "Hi!!")
rule_engine.add_rule("Hi", "Hey how are you doing")
rule_engine.add_rule("Hey", "Hello there")

# Have conversation
while True:
    user_input = input("You: ")
    response = rule_engine.apply_rules(user_input)
    print(response)
    
    if user_input.lower() == "goodbye":
      break