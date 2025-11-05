import medical_data_visualizer

# Test the categorical plot
print("Drawing categorical plot...")
cat_fig = medical_data_visualizer.draw_cat_plot()
cat_fig.savefig('catplot.png')

# Test the heat map
print("Drawing heat map...")
heat_fig = medical_data_visualizer.draw_heat_map()
heat_fig.savefig('heatmap.png')

print("Visualizations saved as catplot.png and heatmap.png")

# Run unit tests (if available)
# from unittest import main
# main(module='test_module', exit=False)
