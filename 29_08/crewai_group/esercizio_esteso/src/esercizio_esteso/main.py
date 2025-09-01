#!/usr/bin/env python
import warnings
from flow_documentation import kickoff as flow_kickoff, plot as flow_plot

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run_flow():
    """
    Run the documentation generation flow.
    """
    try:
        result = flow_kickoff()
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the flow: {e}")

def plot_flow():
    """
    Generate flow visualization.
    """
    try:
        flow_plot()
    except Exception as e:
        raise Exception(f"An error occurred while plotting the flow: {e}")


if __name__ == "__main__":
    run_flow()
    plot_flow()
