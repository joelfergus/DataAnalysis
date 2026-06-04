import numpy as np


scores = np.array([88, 74, 91, 85, 62, 95, 80, 77, 83, 71, 87, 79, 93, 75, 82, 76, 89, 84, 68, 81])
print(f"Mean score: {scores.mean()}")
print(f"Median score: {np.median(scores)}")
print(f"Standard Deviation: {scores.std()}")
print(f"employees above 85: {scores[scores > 85].size}")
print(f"75th percentile: {np.percentile(scores, 75)}")
print(f"normalized scores: {(scores - scores.min()) / (scores.max() - scores.min())}")