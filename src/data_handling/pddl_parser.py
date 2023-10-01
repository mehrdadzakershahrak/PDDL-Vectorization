class PDDLParser:
    def __init__(self, pddl_text):
        self.pddl_text = pddl_text

    def extract_domain_name(self):
        # Extract domain name using simple string methods or regex
        lines = self.pddl_text.split("\n")
        for line in lines:
            if "domain" in line:
                return line.split()[-1]
        return None

    def extract_problem_name(self):
        # Extract problem name
        lines = self.pddl_text.split("\n")
        for line in lines:
            if "problem" in line:
                return line.split()[-1]
        return None

    def extract_actions(self):
        # Extract actions
        # For simplicity, we'll just return a list of action names
        # Advanced parsing can be done to extract action details (preconditions, effects, etc.)
        actions = []
        lines = self.pddl_text.split("\n")
        in_action = False
        for line in lines:
            if ":action" in line:
                in_action = True
                action_name = line.split(":action")[-1].strip()
                actions.append(action_name)
            elif in_action and ")" in line:
                in_action = False
        return actions

    # TODO Similarly, you can add methods to extract predicates, objects, etc.
