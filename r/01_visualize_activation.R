# Load required libraries
library(tidyverse)
library(ComplexHeatmap)  # Optional for more advanced heatmaps

# Load region activation data (assumed to come from image quantification)
activation <- read_csv(results/tables/region_activation.csv)

# Basic bar plot of activation per region
ggplot(activation, aes(x = reorder(region, value), y = value)) +
  geom_col(fill = steelblue) +
  coord_flip() +
  labs(
    title = Activation by Brain Region,
    x = Brain Region,
    y = Signal Intensity
  ) +
  theme_minimal()

# Save the plot
ggsave(results/figures/activation_heatmaps/region_activation_barplot.png, width = 8, height = 6)

