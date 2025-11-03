# Load libraries
library(tidyverse)
library(umap)

# Load mock activation matrix (rows = samples, cols = regions)
# Example assumes you have multiple samples and regions
# Replace this with real data later
activation_matrix <- read_csv(results/tables/multi_sample_activation_matrix.csv)

# Optional: scale the data
activation_scaled <- activation_matrix %>%
  column_to_rownames(sample_id) %>%
  scale()

# Run UMAP
umap_result <- umap(activation_scaled)

# Combine UMAP result with metadata
umap_df <- as_tibble(umap_result) %>%
  mutate(sample_id = rownames(activation_scaled))

# Plot UMAP
ggplot(umap_df, aes(x = V1, y = V2)) +
  geom_point(size = 3, alpha = 0.8, color = darkgreen) +
  labs(title = UMAP of Brain Activation Patterns, x = UMAP1, y = UMAP2) +
  theme_minimal()

# Save plot
ggsave(results/figures/activation_heatmaps/umap_activation.png, width = 6, height = 5)

