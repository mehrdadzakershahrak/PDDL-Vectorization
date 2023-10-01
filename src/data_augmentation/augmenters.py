import random

class NoiseInjectionAugmenter:
    def __init__(self, noise_probability=0.05):
        self.noise_probability = noise_probability

    def augment(self, pddl_text):
        words = pddl_text.split()
        augmented_words = []
        for word in words:
            if random.random() < self.noise_probability:
                word = self._introduce_noise(word)
            augmented_words.append(word)
        return " ".join(augmented_words)

    def _introduce_noise(self, word):
        # Simple noise: swapping two adjacent characters
        if len(word) > 1:
            idx = random.randint(0, len(word)-2)
            word = word[:idx] + word[idx+1] + word[idx] + word[idx+2:]
        return word

class PDDLMutationAugmenter:
    def __init__(self, mutation_probability=0.05):
        self.mutation_probability = mutation_probability

    def augment(self, pddl_text):
        # Placeholder implementation
        # Depending on the PDDL structure, introduce new actions, change predicates, etc.
        # For simplicity, let's introduce a random comment as a mutation
        if random.random() < self.mutation_probability:
            pddl_text += "\n; Augmented comment"
        return pddl_text

# TODO add more augmenters or enhance existing ones for more sophisticated augmentations.
