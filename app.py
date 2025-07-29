import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd

template_segment = [
    {"R": (3, 5), "FM": (4, 5), "Label": "1. Loyal Customers",       "Color": "#4285F4FF"},
    {"R": (4, 5), "FM": (3, 3), "Label": "2. Potential Loyalists",  "Color": "#00ACC1FF"},
    {"R": (4, 5), "FM": (1, 2), "Label": "3. Recent Customers",    "Color": "#34A853FF"},
    {"R": (3, 3), "FM": (3, 3), "Label": "4. Need Attention",      "Color": "#FBBC05FF"},
    {"R": (1, 2), "FM": (5, 5), "Label": "5. Can't lose them",     "Color": "#EA222AFF"},
    {"R": (1, 2), "FM": (3, 4), "Label": "6. At Risk",             "Color": "#FB8C05FF"},
    {"R": (1, 3), "FM": (1, 2), "Label": "7. Lost Customers",      "Color": "#9E9E9EFF"},
]

df_segment = pd.DataFrame(template_segment)

segments = []
for row in df_segment.itertuples(index=False, name=None):
    # print(row)  # Each row is a tuple
    _temp_dict = {"R": row[0], "FM": row[1], "Label": row[2], "Color": row[3], "Count": row[4], "Percent": row[5]}
    segments.append(_temp_dict)

    
st.set_page_config(layout="wide")
st.title("RFM Nasional - Segmentation Treemap")
st.caption("Apr 2022 - Mar 2024")

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0.5, 5.5)
ax.set_ylim(0.5, 5.5)
ax.set_xticks(range(1, 6))
ax.set_yticks(range(1, 6))
ax.set_xlabel("Recency (days)", fontsize=12, fontweight='bold')
ax.set_ylabel("Frequency + Monetary (orders + revenue)", fontsize=12, fontweight='bold')

for seg in segments:
    rmin, r_max = seg["R"]
    x = rmin - 1
    width = r_max - rmin + 1

    fm_min, fm_max = seg["FM"]
    y = fm_min - 1
    height = fm_max - fm_min + 1

    rect = patches.Rectangle(
        (x + 0.5, y + 0.5),
        width, height,
        linewidth=1, edgecolor='white', facecolor=seg["Color"]
    )
    ax.add_patch(rect)

    text_x = (x + 0.5) + width - 0.05
    text_y = (y + 0.5) + height - 0.05
    ax.text(text_x - 0.04, text_y - 0.04, seg["Label"],
            ha='right', va='top', fontsize=10, fontweight='bold', color="white")

ax.tick_params(axis='both', which='both', length=0)
ax.set_xticklabels(["1", "2", "3", "4", "5"], fontsize=12)
ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=12)
ax.grid(False)
for spine in ax.spines.values():
    spine.set_visible(False)

legend_handles = [patches.Patch(color=seg["Color"], label=seg["Label"]) for seg in segments]
ax.legend(handles=legend_handles, loc="upper left", bbox_to_anchor=(1, 1))

st.pyplot(fig)
