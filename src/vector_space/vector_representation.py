from src.encoder.encoder_model import PDLEncoder

class VectorSpaceRepresentation:
    def __init__(self):
        self.encoder = PDLEncoder()

    def represent(self, pddl_text):
        """
        Represent the PDDL text in vector space.
        
        Args:
        - pddl_text (str): The PDDL description to be represented.

        Returns:
        - list: The vector space representation of the PDDL.
        """
        return self.encoder.encode(pddl_text)
