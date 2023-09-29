import yaml
from tokenizers import WhitespaceTokenizer  # and other tokenizers
from src.encoder.encoder_model import PDLEncoder
from src.decoder.decoder_model import PDDLDecoder
# TODO Check import 

def validate_scenario(scenario):
    """Validate that the scenario file contains all necessary configurations."""
    required_sections = ["tokenization", "encoding", "decoding"]
    for section in required_sections:
        if section not in scenario:
            # You can use logging here
            return False
    return True

def setup_scenario_from_file(file_path):
    """Set up components based on the given scenario file."""
    with open(file_path, 'r') as file:
        scenario = yaml.safe_load(file)

    if not validate_scenario(scenario):
        # Log an error message if the scenario is invalid
        return None, None

    # Set up tokenization
    tokenizer_name = scenario['tokenization']['strategy']
    tokenizer = create_tokenizer(tokenizer_name)

    # Set up encoder and decoder using the tokenizer and other parameters
    # ...

    return encoder, decoder  # Return other components as needed