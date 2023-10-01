class EvaluationMetrics:
    def __init__(self, action_costs=None):
        """
        Args:
        - action_costs (dict, optional): A dictionary mapping action names to their associated costs.
        """
        self.action_costs = action_costs if action_costs else {}

    def evaluate_plan(self, plan):
        """
        Evaluate the quality of a generated plan.
        
        Args:
        - plan (list): The sequence of actions.

        Returns:
        - dict: A dictionary containing various quality scores of the plan.
        """
        scores = {}
        
        # Plan Length
        scores['length'] = len(plan)
        
        # Action Costs
        total_cost = sum(self.action_costs.get(action, 1) for action in plan)  # Default cost is 1 if not specified
        scores['total_cost'] = total_cost
        
        # You can add more domain-specific metrics here
        
        return scores
