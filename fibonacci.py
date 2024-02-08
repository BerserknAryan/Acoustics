import matplotlib.pyplot as plt
import numpy as np

def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def plot_exponential_fibonacci_spiral(num_terms, initial_radius, final_radius, scale_factor):
    phi = (1 + np.sqrt(5)) / 2  # Golden ratio
    
    theta = np.pi * (3 - np.sqrt(5))  # Angle increment
    
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    
    current_radius = initial_radius
    spiral_points = []
    
    for i in range(num_terms):
        angle = i * theta
        x = np.cos(angle) * current_radius
        y = np.sin(angle) * current_radius
        spiral_points.append((x, y))
        
        # Update radius for next circular segment
        current_radius *= phi
    
    # Find a segment where the radius increases from initial_radius to final_radius
    for i in range(len(spiral_points) - 1):
        x1, y1 = spiral_points[i]
        x2, y2 = spiral_points[i + 1]
        radius1 = np.sqrt(x1 ** 2 + y1 ** 2)
        radius2 = np.sqrt(x2 ** 2 + y2 ** 2)
        if initial_radius <= radius1 <= final_radius and initial_radius <= radius2 <= final_radius:
            ax.plot([x1, x2], [y1, y2], color='red')  # Plot the segment in red
            break
    
    plt.show()

# Parameters
num_terms = 1000  # Number of terms in the Fibonacci sequence
initial_radius = 9  # Initial radius (corresponds to 18-inch diameter)
final_radius = 10.5  # Final radius (corresponds to 21-inch diameter)
scale_factor = 1  # Scale factor for adjusting the size of the plot

# Plot exponential Fibonacci spiral
plot_exponential_fibonacci_spiral(num_terms, initial_radius, final_radius, scale_factor)

