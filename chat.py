# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 1. Set Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")

# 2. Generate synthetic business data
data = {
    "Product": ["A", "B", "C", "D", "E"],
    "Revenue": [120000, 95000, 143000, 76000, 112000]
}
df = pd.DataFrame(data)

# 3. Create the figure (8x8 inches at 64 dpi → 512x512 px)
plt.figure(figsize=(8, 8))

# 4. Create barplot
ax = sns.barplot(
    x="Product",
    y="Revenue",
    data=df,
    palette="crest"
)

# 5. Add title and labels
ax.set_title("Quarterly Revenue by Product", fontsize=18, weight="bold")
ax.set_xlabel("Product", fontsize=14)
ax.set_ylabel("Revenue (USD)", fontsize=14)

# 6. Save chart as 512x512 PNG
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
