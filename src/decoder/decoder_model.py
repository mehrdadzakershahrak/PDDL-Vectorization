from tokenizers import WhitespaceTokenizer

class PDDLDecoder:
    def __init__(self, vocabulary, tokenizer=None):
        self.vocabulary = vocabulary
        self.id_to_token = {idx: token for idx, token in enumerate(vocabulary)}
        self.tokenizer = tokenizer or WhitespaceTokenizer()

    def decode(self, vector_representation):
        """
        Decode the vector representation back into PDDL text.
        
        Args:
        - vector_representation (list): The vector to be decoded.

        Returns:
        - str: The decoded PDDL description.
        """
        tokens = [self.id_to_token.get(idx, "<UNK>") for idx in vector_representation]
        pddl_text = self.tokenizer.detokenize(tokens)
        return pddl_text
