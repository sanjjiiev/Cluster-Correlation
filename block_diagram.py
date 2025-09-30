import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Function to draw a single block
def draw_block(ax, text, xy, width=3, height=1, fontsize=10, color="#AED6F1"):
    x, y = xy
    box = FancyBboxPatch((x, y), width, height,
                         boxstyle="round,pad=0.3",
                         edgecolor="black", facecolor=color)
    ax.add_patch(box)
    ax.text(x + width/2, y + height/2, text,
            ha="center", va="center", fontsize=fontsize)

# Function to draw an arrow
def draw_arrow(ax, start, end):
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="->", lw=2))

# Create figure
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 14)
ax.axis("off")

# --- 1D pipeline blocks ---
draw_block(ax, "1D Dataset (CSV)\nboneage, gender...", (1, 12))
draw_block(ax, "Preprocessing & Scaling", (1, 10.5))
draw_block(ax, "K-Means Clustering (2)\n→ CSV Clusters", (1, 9))

# --- 2D pipeline blocks ---
draw_block(ax, "2D Dataset (Images)\nX-ray images", (8, 12))
draw_block(ax, "Preprocessing & Resize", (8, 10.5))
draw_block(ax, "PCA Feature Reduction", (8, 9))
draw_block(ax, "K-Means Clustering (4)\n→ Image Clusters", (8, 7.5))

# --- Merge and correlation ---
draw_block(ax, "Merge Clusters on Common ID", (4.5, 5))
draw_block(ax, "Correlation Analysis\n(Cramér's V, NMI, ARI)", (4.5, 3.5))
draw_block(ax, "Insights: Relationship\nbetween 1D & 2D clusters", (4.5, 2))

# --- Arrows 1D pipeline ---
draw_arrow(ax, (2.5, 12), (2.5, 10.5))
draw_arrow(ax, (2.5, 10.5), (2.5, 9))
draw_arrow(ax, (2.5, 9), (5.5, 5))

# --- Arrows 2D pipeline ---
draw_arrow(ax, (9.5, 12), (9.5, 10.5))
draw_arrow(ax, (9.5, 10.5), (9.5, 9))
draw_arrow(ax, (9.5, 9), (9.5, 7.5))
draw_arrow(ax, (9.5, 7.5), (5.5, 5))

# --- Arrows for merged steps ---
draw_arrow(ax, (6, 5), (6, 3.5))
draw_arrow(ax, (6, 3.5), (6, 2))

plt.show()
