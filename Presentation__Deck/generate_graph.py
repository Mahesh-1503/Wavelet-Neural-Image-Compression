import matplotlib.pyplot as plt
import numpy as np

def generate_performance_graph():
    # Data representing the project benchmarks
    methods = ['JPEG 2000', 'Huffman', 'PNG-DEFLATE', 'Proposed (SIREN + Wavelet)']
    compression_ratios = [35, 30, 45, 55] # in percentage
    psnr_values = [30, 32, 36, 40] # in dB

    x = np.arange(len(methods))
    width = 0.35

    # Create figure and axis
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plotting Compression Ratio (Blue Bars)
    bars1 = ax1.bar(x - width/2, compression_ratios, width, label='Compression Ratio (%)', color='#3498db')
    ax1.set_ylabel('Compression Ratio (%)', color='#2980b9', fontsize=12, fontweight='bold')
    ax1.tick_params(axis='y', labelcolor='#2980b9')
    ax1.set_ylim(0, 70)

    # Secondary axis for PSNR (Red Bars)
    ax2 = ax1.twinx()
    bars2 = ax2.bar(x + width/2, psnr_values, width, label='PSNR (dB)', color='#e74c3c')
    ax2.set_ylabel('PSNR (dB)', color='#c0392b', fontsize=12, fontweight='bold')
    ax2.tick_params(axis='y', labelcolor='#c0392b')
    ax2.set_ylim(0, 50)

    # Formatting and Titles
    ax1.set_xticks(x)
    ax1.set_xticklabels(methods, rotation=15, ha="right", fontsize=11, fontweight='bold')
    plt.title('Performance Comparison: Proposed System vs Existing Methods', fontsize=15, fontweight='bold', pad=15)

    # Legends
    lines_labels = [ax.get_legend_handles_labels() for ax in [ax1, ax2]]
    lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
    ax1.legend(lines, labels, loc='upper left', fontsize=11)

    # Add text values on top of bars
    for bar in bars1:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, yval + 1.5, f"{yval}%", ha='center', va='bottom', fontsize=10, fontweight='bold', color='#2980b9')

    for bar in bars2:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, yval + 1.5, f"{yval}dB", ha='center', va='bottom', fontsize=10, fontweight='bold', color='#c0392b')

    # Polish and display
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.tight_layout()
    print("Graph generated successfully! Displaying window...")
    plt.show()

if __name__ == '__main__':
    try:
        generate_performance_graph()
    except ImportError:
        print("Error: 'matplotlib' is required to generate the graph.")
        print("Please run: pip install matplotlib")
