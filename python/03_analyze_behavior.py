import pandas as pd
import matplotlib.pyplot as plt

track_file = data/raw/behavior_tracking/mouse_behavior.csv
df = pd.read_csv(track_file, header=[0, 1], index_col=0)

# Use snout as example point
x = df[('snout', 'x')]
y = df[('snout', 'y')]

# Simple metrics
speed = ((x.diff() ** 2 + y.diff() ** 2) ** 0.5)
summary = {
    mean_speed: speed.mean(),
    max_speed: speed.max(),
    distance_traveled: speed.sum()
}

print(Behavior Summary:)
for k, v in summary.items():
    print(f{k}: {v:.2f} px/frame)

# Save for R
out_df = pd.DataFrame({frame: df.index, x: x, y: y, speed: speed})
out_df.to_csv(results/tables/behavior_summary.csv, index=False)

