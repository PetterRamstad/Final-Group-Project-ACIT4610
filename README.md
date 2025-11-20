# ACIT4610 Final Group Project

This repository contains the implementation for the ACIT4610 Final Group Project. It explores various optimization algorithms and machine learning techniques to solve complex problems, including Bin Packing, function optimization, the Knapsack problem, and Reinforcement Learning.

## Project Overview

The project is consolidated into a single Jupyter Notebook (`Final_Group_Project_ACIT4610.ipynb`) and covers the following problems:

1.  **Problem 1: One-Dimensional Bin Packing**
    - **Algorithm:** Ant Colony Optimization (ACO)
    - **Context:** E-commerce Fulfillment optimization.
2.  **Problem 2: Optimization of Benchmark Functions**

    - **Algorithm:** Particle Swarm Optimization (PSO)
    - **Objective:** Optimizing classic benchmark functions.

3.  **Problem 3: 0–1 Knapsack Problem**

    - **Algorithm:** Bees Algorithm (BA)
    - **Data:** Uses instances from the `Knapsack instances` directory.

4.  **Problem 5: Reinforcement Learning**
    - **Algorithm:** Q-learning
    - **Environment:** FrozenLake.

## Repository Structure

- `Final_Group_Project_ACIT4610.ipynb`: The main Jupyter Notebook containing all code, implementations, and visualizations.
- `Binpacks/`: Directory containing data files for the Bin Packing problem (e.g., `binpack2.txt`).
- `Knapsack instances/`: Directory containing data files for the Knapsack problem (e.g., `mknap1.txt`).
- `Final Group Projct 2025.pdf`: Project requirements and description document.

## Prerequisites

To run this project, you need Python installed along with the following libraries:

- Python 3.x
- Jupyter Notebook or JupyterLab
- NumPy
- Matplotlib
- Seaborn

## Installation

1.  **Clone the repository** (or download the files):

    ```bash
    git clone <repository-url>
    cd Final-Group-Project-ACIT4610
    ```

2.  **Install the required Python packages**:
    It is recommended to use a virtual environment.
    ```bash
    pip install numpy matplotlib seaborn jupyter gymnasium
    ```

## Usage

1.  Start the Jupyter Notebook server:

    ```bash
    jupyter notebook
    ```

2.  In the browser interface, navigate to and open `Final_Group_Project_ACIT4610.ipynb`.

3.  Run the cells sequentially to execute the algorithms and view the results.
    - **Note:** Ensure the `Binpacks` and `Knapsack instances` directories are in the same folder as the notebook so the data loading functions work correctly.

## Authors

- Lauritz Pedersen
  Petter Ramstad
  Miriam Throndsen
