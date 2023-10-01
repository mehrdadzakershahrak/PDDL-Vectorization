from src.data_handling.pddl_parser import PDDLParser

sample_pddl = """
(define (domain sample_domain)
  ...
  (:action move
    ...
  )
  (:action pick
    ...
  )
)
"""

parser = PDDLParser(sample_pddl)
print("Domain Name:", parser.extract_domain_name())
print("Actions:", parser.extract_actions())

########## second experiment
from src.data_augmentation.augmenters import NoiseInjectionAugmenter, PDDLMutationAugmenter

sample_pddl = """
(define (domain sample_domain)
  (:action move
    ...
  )
  (:action pick
    ...
  )
)
"""

noise_augmenter = NoiseInjectionAugmenter()
print(noise_augmenter.augment(sample_pddl))

mutation_augmenter = PDDLMutationAugmenter()
print(mutation_augmenter.augment(sample_pddl))
