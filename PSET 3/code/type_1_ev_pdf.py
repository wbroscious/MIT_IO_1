from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


beta = 1.0
x_minus_mu = np.linspace(-4, 8, 1_000)
pdf = (1 / beta) * np.exp(
    -(x_minus_mu / beta) - np.exp(-(x_minus_mu / beta))
)

plt.plot(x_minus_mu, pdf)
plt.xlabel(r"$x-\mu$")
plt.ylabel("Probability density")
plt.title(r"Type I Extreme Value PDF ($\beta=1$)")
plt.grid(alpha=0.3)
plt.tight_layout()

figures_dir = Path(__file__).parent.parent / "figures"
figures_dir.mkdir(exist_ok=True)
plt.savefig(figures_dir / "type_1_ev_pdf.png", dpi=300)

plt.show()