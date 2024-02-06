from tqdm import tqdm
import time

def loading_bar(total_iterations):
    """
    Display a loading bar for a given number of iterations.

    :param total_iterations: Total number of iterations to simulate.
    """
    for i in tqdm(range(total_iterations), desc="Loading", leave=False):
        time.sleep(0.1)  # Simulate some work being done.
loading_bar(100)