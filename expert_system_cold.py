class ExpertSystem:
    def __init__(self):
        self.rules = {
            "rule1": {"symptom": "cough", "result": "cold"},
            "rule2": {"symptom": "sneezing", "result": "cold"},
            "rule3": {"symptom": "fever", "result": "cold"},
            "rule4": {"symptom": "headache", "result": "cold"},
            "rule5": {"symptom": "fatigue", "result": "cold"},
        }

    def predict_disease(self, symptoms):
        for rule_id, rule in self.rules.items():
            if rule["symptom"] in symptoms:
                return rule["result"]

        return "no specific prediction"

# Usage example:
if __name__ == "__main__":
    expert_system = ExpertSystem()

    print("Welcome to the Disease Prediction Expert System!")
    print("Please enter the symptoms you are experiencing (comma-separated):")
    user_input = input().strip().split(',')

    prediction = expert_system.predict_disease(user_input)
    print(f"Based on the symptoms you provided, the system predicts you may have: {prediction}.")
