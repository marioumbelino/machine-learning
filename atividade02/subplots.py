# Questão 06

import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5),
                        layout="constrained")

for row in range(2):
    for col in range(2):
        axs[row, col].annotate(f"axs[{row}, {col}]", (0.5, 0.5),
                                transform=axs[row, col].transAxes,
                                ha="center", va="center", fontsize=18,
                                color="darkgray")

fig.suptitle('plt.subplot()')

plt.show()