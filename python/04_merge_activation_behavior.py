import pandas as pd

# Load activation per brain region
activation_file = results/tables/region_activation.csv
behavior_file = results/tables/behavior_summary.csv

activation = pd.read_csv(activation_file)
behavior = pd.read_csv(behavior_file)

# Summarize behavior metrics (can be mean across time or final values)
behavior_summary = {
    mean_speed: behavior[speed].mean(),
    max_speed: behavior[speed].max(),
    distance_traveled: behavior[speed].sum()
}
behavior_df = pd.DataFrame([behavior_summary])

# Pivot activation table: one row with regions as columns
activation_wide = activation.pivot_table(index=None, columns=region, values=value)
activation_wide.columns.name = None  # clean up

# Merge into a single row per sample
merged = pd.concat([activation_wide, behavior_df], axis=1)

# Save merged table
out_file = results/tables/activation_behavior_merged.csv
merged.to_csv(out_file, index=False)
print(fMerged data saved to: {out_file})

