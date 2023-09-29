from src.decoder.decoder_model import PDDLDecoder

class ActionDecoder:
    def __init__(self):
        self.decoder = PDDLDecoder()

    def decode_actions(self, actions):
        """
        Decode the vector changes back into PDDL actions.
        
        Args:
        - actions (list): The sequence of vector changes.

        Returns:
        - list: The decoded sequence of PDDL actions.
        """
        # Placeholder code
        pddl_actions = []
        return pddl_actions
