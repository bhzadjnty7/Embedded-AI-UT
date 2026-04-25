import matplotlib.pyplot as plt

# Data from the execution results
numbers = list(range(-15, 15))
errors = [0] * len(numbers)  # Since all matches were valid

plt.figure(figsize=(10, 4))
plt.plot(numbers, errors, 'g-o', label='Reconstruction Error')
plt.title('Reconstruction Error for Signed Range [-15, 14]')
plt.xlabel('Input Number')
plt.ylabel('Error (Input - Recovered)')
plt.grid(True)
plt.yticks([-1, 0, 1])
plt.legend()
plt.show()

import matplotlib.pyplot as plt

def plot_rns_architecture():
    """
    Visualizes the parallel nature of RNS arithmetic operations.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Coordinates
    input_y = 0.8
    channel_y = 0.5
    output_y = 0.2
    
    # Inputs
    ax.text(0.5, input_y, "Input Numbers (A, B)", ha='center', va='center', 
            bbox=dict(boxstyle="round", facecolor="wheat"), fontsize=12)
    
    # Arrows to channels
    ax.annotate("", xy=(0.2, channel_y+0.1), xytext=(0.5, input_y-0.05), arrowprops=dict(arrowstyle="->"))
    ax.annotate("", xy=(0.5, channel_y+0.1), xytext=(0.5, input_y-0.05), arrowprops=dict(arrowstyle="->"))
    ax.annotate("", xy=(0.8, channel_y+0.1), xytext=(0.5, input_y-0.05), arrowprops=dict(arrowstyle="->"))
    
    # Channels (Moduli)
    channels = ["Channel 1\n(Mod 3)", "Channel 2\n(Mod 4)", "Channel 3\n(Mod 5)"]
    positions = [0.2, 0.5, 0.8]
    colors = ['lightblue', 'lightgreen', 'lightpink']
    
    for pos, txt, col in zip(positions, channels, colors):
        circle = plt.Circle((pos, channel_y), 0.1, color=col, alpha=0.6)
        ax.add_patch(circle)
        ax.text(pos, channel_y, txt, ha='center', va='center', fontsize=10, weight='bold')
        # Independent operations text
        ax.text(pos, channel_y - 0.15, "OP % m_i", ha='center', va='center', fontsize=9, style='italic')

    # Arrows to output
    ax.annotate("", xy=(0.5, output_y+0.05), xytext=(0.2, channel_y-0.1), arrowprops=dict(arrowstyle="->"))
    ax.annotate("", xy=(0.5, output_y+0.05), xytext=(0.5, channel_y-0.1), arrowprops=dict(arrowstyle="->"))
    ax.annotate("", xy=(0.5, output_y+0.05), xytext=(0.8, channel_y-0.1), arrowprops=dict(arrowstyle="->"))
    
    # Output
    ax.text(0.5, output_y, "Reconstructed Result\n(CRT / MRC)", ha='center', va='center', 
            bbox=dict(boxstyle="round", facecolor="wheat"), fontsize=12)
            
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.title("RNS Parallel Arithmetic Architecture", fontsize=14)
    plt.show()

plot_rns_architecture() # Uncomment to execute if plotting is supported