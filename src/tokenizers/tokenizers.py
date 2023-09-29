# tokenizers.py

class BaseTokenizer:
    """Base class for all tokenizer strategies."""
    def tokenize(self, text):
        raise NotImplementedError

    def detokenize(self, tokens):
        raise NotImplementedError

class WhitespaceTokenizer(BaseTokenizer):
    """Tokenization strategy based on whitespace."""
    def tokenize(self, text):
        return text.split()

    def detokenize(self, tokens):
        return " ".join(tokens)

# TODO Add other tokenization strategies as needed. For example:
# class AnotherTokenizer(BaseTokenizer):

# A registry to map tokenizer names to their corresponding classes.
TOKENIZER_REGISTRY = {
    "WhitespaceTokenizer": WhitespaceTokenizer,
    # "AnotherTokenizer": AnotherTokenizer,
    # ...
}

def create_tokenizer(name):
    """Utility function to create a tokenizer based on its name."""
    return TOKENIZER_REGISTRY[name]()
