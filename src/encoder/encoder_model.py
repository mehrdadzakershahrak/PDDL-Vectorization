from tokenizers import WhitespaceTokenizer

class PDLEncoder:
    def __init__(self, vocabulary, tokenizer=None):
        self.vocabulary = vocabulary
        self.token_to_id = {token: idx for idx, token in enumerate(vocabulary)}
        self.tokenizer = tokenizer or WhitespaceTokenizer()

    def encode(self, pddl_text):
        """
        Encode the PDDL text into a vector representation.
        
        Args:
        - pddl_text (str): The PDDL description to be encoded.

        Returns:
        - list: The vector representation of the PDDL.
        """
        tokens = self.tokenizer.tokenize(pddl_text)
        vector_representation = [self.token_to_id.get(token, -1) for token in tokens]
        return vector_representation
