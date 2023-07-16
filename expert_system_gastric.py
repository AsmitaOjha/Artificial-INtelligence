class ExpertSystemGastric:
    def __init__(self):
        self.rules = {
            "rule1": {"question": "Do you experience frequent heartburn?", "result": "Gastroesophageal reflux disease (GERD)"},
            "rule2": {"question": "Do you often feel bloated after eating?", "result": "Gastric distension"},
            "rule3": {"question": "Do you have a burning sensation in your stomach?", "result": "Gastritis"},
            "rule4": {"question": "Have you been experiencing stomach pain?", "result": "Peptic ulcer"},
            # Add more rules for other gastric issues...
        }

    def diagnose_gastric_issue(self):
        print("Welcome to the Gastric Issue Diagnosis Expert System!")
        print("Please answer the following questions with 'yes' or 'no'.")

        symptoms = []
        for rule_id, rule in self.rules.items():
            answer = input(f"{rule['question']} ").strip().lower()
            if answer == 'yes':
                symptoms.append(rule_id)

        if symptoms:
            print(f"Based on your symptoms, the system suggests you may have: {', '.join(self.rules[symptom]['result'] for symptom in symptoms)}.")
        else:
            print("The system couldn't identify any specific gastric issue based on the symptoms provided.")

# Usage example:
if __name__ == "__main__":
    expert_system_gastric = ExpertSystemGastric()
    expert_system_gastric.diagnose_gastric_issue()
