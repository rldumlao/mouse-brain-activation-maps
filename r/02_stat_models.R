library(tidyverse)

behavior <- read_csv("results/tables/behavior_summary.csv")
activation <- read_csv("results/tables/region_activation.csv") # if available

# Quick example plot
ggplot(behavior, aes(x = frame, y = speed)) +
  geom_line(color = "steelblue") +
  labs(title = "Mouse Speed Over Time", y = "Speed (px/frame)")

# Placeholder: plot vs brain region
# ggplot(activation, aes(region, value)) + geom_col()

# Save plot
ggsave("results/figures/behavior_plots/speed_over_time.png")

