import sys
import pandas as pd
import numpy as np

def get_metrics(output_scores = False):
    overall_metrics = 0.5
    scores = pd.DataFrame() # empty dataframe
    if output_scores:
        scores = pd.DataFrame(np.random.randn(50, 4))

    return overall_metrics, scores


if __name__ == "__main__":
    f()
    print(a)