import sys
import numpy as np

def main():
    """
    Main function to simulate the prisoner's problem.

    This function takes the number of prisoners and the number of iterations from the command-line arguments.
    It simulates a situation where each prisoner attempts to find their number in a random set of boxes. 
    There are two strategies simulated:
    - A 'smart' strategy that follows a looped pattern.
    - A 'fool' strategy that checks random boxes.

    If the arguments are invalid, it prints the correct usage and exits.
    """
    try:
        # Get the number of prisoners and iterations from command line arguments
        PRISONERS = int(sys.argv[1])
        ITERATIONS = int(sys.argv[2])
    except:
        print("\nUsage: python prisoners.py <prisoner_num> <iteration_num>\n")
        sys.exit()

    print(f"\nStarting simulation.\nPrisoners: {PRISONERS}\nIterations: {ITERATIONS}")

    # Initialize success counters for smart and fool strategies
    smart_success_num = 0
    fool_success_num = 0
    ATTEMPT_NUM = PRISONERS // 2  # Max attempts a prisoner can make

    last_percentage = ""  # Track progress percentage
    for iteration in range(1, ITERATIONS + 1):
        # Create a shuffled array for each iteration
        shuffled_array = create_shuffled_array(PRISONERS)

        # Initialize success flags for each strategy
        smart_freed = True
        fool_freed = True

        for prisoner in range(PRISONERS):
            # Check if each prisoner can find their number in the boxes
            if not smart_finds_box(prisoner, shuffled_array, ATTEMPT_NUM):
                smart_freed = False
            if not fool_finds_box(prisoner, PRISONERS, ATTEMPT_NUM):
                fool_freed = False

            # Break early if both strategies fail in the current iteration
            if not smart_freed and not fool_freed:
                break

        # Update success counts based on results
        if smart_freed:
            smart_success_num += 1
        if fool_freed:
            fool_success_num += 1

        # Print the progress percentage
        percentage = f"{100 * (iteration / ITERATIONS):.1f}"
        if last_percentage != percentage:
            last_percentage = percentage
            print(f"{percentage}%", end="\r")

    # Print final results after simulation
    print("\n\nSimulation ended.")
    print(f"Success cases with {PRISONERS} prisoners:")
    print(f"  - Smart group: {smart_success_num} | {100 * (smart_success_num / ITERATIONS):.1f}%")
    print(f"  - Fool group: {fool_success_num} | {100 * (fool_success_num / ITERATIONS):.1f}%\n")


def create_shuffled_array(n):
    """
    Generate a shuffled array of integers from 0 to n-1.

    Parameters:
    n (int): Number of elements in the array.

    Returns:
    np.ndarray: Shuffled array of integers.
    """
    array = np.arange(n)
    np.random.shuffle(array)
    return array


def smart_finds_box(prisoner, shuffled_array, attempt_num):
    """
    Simulate the 'smart' strategy where the prisoner follows a looped pattern.

    Parameters:
    prisoner (int): The prisoner number (index).
    shuffled_array (np.ndarray): Array representing shuffled boxes.
    attempt_num (int): Maximum number of attempts allowed.

    Returns:
    bool: True if the prisoner finds their number, False otherwise.
    """
    box = prisoner  # Start at the box matching the prisoner number
    for _ in range(attempt_num):
        num = shuffled_array[box]
        if num == prisoner:
            return True
        box = num  # Follow the loop to the next box
    return False


def fool_finds_box(prisoner, box_num, attempt_num):
    """
    Simulate the 'fool' strategy where the prisoner checks random boxes.

    Parameters:
    prisoner (int): The prisoner number (index).
    box_num (int): Total number of boxes.
    attempt_num (int): Maximum number of attempts allowed.

    Returns:
    bool: True if the prisoner finds their number, False otherwise.
    """
    # Generate a random selection of boxes to check
    boxes_to_check = create_shuffled_array(box_num)
    boxes_to_check = boxes_to_check[:attempt_num + 1]
    for box in boxes_to_check:
        if box == prisoner:
            return True
    return False


if __name__ == "__main__":
    main()