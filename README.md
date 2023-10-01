# PDDL Vectorization and Plan Generation

This project focuses on encoding PDDL (Planning Domain Definition Language) textual descriptions into vector representations and decoding them back. It also provides tools to generate plans based on these vector representations.

## Project Structure

PDDL-Vectorization/
|-- run_experiment.py (Main execution script)
|-- scenarios/ (Contains YAML scenario setup files)
|-- src/
| |-- encoder/ (Encoder implementations)
| |-- decoder/ (Decoder implementations)
| |-- utils/ (Utility functions and classes)
| | |-- scenario_utils.py (Scenario setup and validation)
| | |-- logger_config.py (Logging configurations)
| |-- data_handling/ (Data processing and augmentation)
| | |-- pddl_parser.py (PDDL structure extraction)
| | |-- augmenters.py (Data augmentation techniques)
| |-- evaluation/ (Performance metrics and evaluations)
| | |-- metrics.py (Evaluation metrics)
| |-- problem_generators/ (Domain-specific problem generators)
| | |-- rover_domain.py (Rover domain problem generator)


## Features

- **Encoder-Decoder Architecture**: Convert PDDL textual descriptions into vector representations and vice versa.
- **Vector Space Representation**: Facilitate structured exploration for plan generation in the vector space.
- **Plan Generation and Search**: Navigate from the initial state vector to the goal state vector, representing a plan.
- **Evaluation and Optimization**: Metrics and utilities to evaluate the quality of generated plans and vector representations.
- **Data Handling**: Tools to parse PDDL structures and augment data.
- **Problem Generators**: Create synthetic PDDL problems for specific domains (e.g., rover domain).

## Getting Started

1. Setup the desired scenario using a YAML file in the `scenarios/` directory.
2. Run the main script, `run_experiment.py`, to execute experiments based on the scenario setup.

## Future Work

- Integrate advanced machine learning models for encoding and decoding.
- Expand the problem generators to cover more domains.
- Optimize search strategies in the vector space.
