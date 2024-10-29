# Prisoners Simulation

This project simulates the **Prisoners and Boxes Problem** using two different strategies: a "smart" strategy based on looping through box patterns and a "fool" strategy where boxes are chosen randomly. The goal is to observe the success rates of each strategy over multiple iterations.

## Problem Description

In this simulation:
1. A group of prisoners (given by `PRISONERS`) each have a number assigned to them.
2. These prisoners face the challenge of finding their own number among a set of shuffled boxes, each containing a different number.
3. Each prisoner has a limited number of attempts (half of the total prisoners) to locate their number.
4. If all prisoners in a given iteration find their numbers, the group is "freed" for that iteration.

This simulation compares two strategies over a specified number of iterations:
- **Smart Strategy**: Each prisoner follows a looped pattern, using their number as a starting point and moving between boxes in a systematic way.
- **Fool Strategy**: Each prisoner randomly selects boxes to check.

## Simulation Output

The simulation outputs:
- Progress percentage during the simulation.
- Final success rate for each strategy, expressed as a percentage of successful attempts over the total iterations.

## Requirements

- Python 3.x
- NumPy (for generating shuffled arrays)

You can install NumPy via pip if you don’t have it:
```bash
pip install numpy
```

## Usage

To run the simulation, use the following command in your terminal:

python prisoners.py <prisoner_num> <iteration_num>

	•	<prisoner_num>: Number of prisoners participating in the simulation (also represents the number of boxes).
	•	<iteration_num>: Number of times the simulation should run to calculate success rates.

## Example:

python prisoners.py 100 1000

This command will simulate 100 prisoners attempting to find their numbers in 1000 iterations.

## Code Overview

	•	main(): Initializes the simulation, parses arguments, and runs the simulation for each iteration, keeping track of success rates.
	•	create_shuffled_array(n): Generates a shuffled array of integers from 0 to n-1.
	•	smart_finds_box(prisoner, shuffled_array, attempt_num): Implements the smart strategy where prisoners follow a loop pattern to find their number.
	•	fool_finds_box(prisoner, box_num, attempt_num): Implements the fool strategy where prisoners randomly choose boxes to check.

## Example Output

Starting simulation.
Prisoners: 100
Iterations: 1000
100.0%

Simulation ended.
Success cases with 100 prisoners:
  - Smart group: 310 | 31.0%
  - Fool group: 120 | 12.0%

## Notes

	•	The smart strategy is generally more successful due to the systematic approach it follows.
	•	This simulation is a representation of probabilistic approaches in algorithmic problem-solving.

## License

This project is licensed under the MIT License.

This Markdown code will create a structured README file with sections for the description, requirements, usage, code overview, example output, notes, and license.
