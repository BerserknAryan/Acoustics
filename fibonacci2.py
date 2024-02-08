import matplotlib.pyplot as plt
import pandas as pd


try:
    import ipywidgets as widgets
    from IPython.display import display
except ImportError as e:
    print(f"Error importing required module: {e}")


# Initialize DataFrame to store Fibonacci sequences
fibonacci_df = pd.DataFrame(columns=['n_Terms', 'Scale', 'Sequence'])


def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


def plot_fibonacci_sequence(sequence, scale=1):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    x, y = 0, 0
    for num in sequence:
        ax.add_patch(plt.Rectangle((x, y), num*scale, num*scale, edgecolor='black', facecolor='none'))
        x += num*scale
        y += num*scale
    plt.xlim(0, x)  # Adjust x-axis limit
    plt.ylim(0, y)  # Adjust y-axis limit
    plt.show()


def update_plot(num_terms, scale_factor):
    try:
        sequence = fibonacci_sequence(num_terms)
        plot_fibonacci_sequence(sequence, scale=scale_factor)
    except Exception as e:
        print(f"Error occurred: {e}")


def add_to_dataframe(num_terms, scale_factor):
    try:
        sequence = fibonacci_sequence(num_terms)
        global fibonacci_df
        new_row = {'n_Terms': num_terms, 'Scale': scale_factor, 'Sequence': sequence}
        fibonacci_df = fibonacci_df.append(new_row, ignore_index=True)
        update_dropdown()
    except Exception as e:
        print(f"Error occurred: {e}")


def update_dropdown():
    try:
        dropdown_options = [(f"{row['n_Terms']} terms, Scale {row['Scale']}", index)
                            for index, row in fibonacci_df.iterrows()]
        dropdown.options = dropdown_options
    except Exception as e:
        print(f"Error occurred: {e}")


def dropdown_eventhandler(change):
    index = change.new
    if index is not None:
        try:
            row = fibonacci_df.loc[index]
            num_terms, scale_factor = row['n_Terms'], row['Scale']
            update_plot(num_terms, scale_factor)
        except Exception as e:
            print(f"Error occurred: {e}")


# Widgets for user interaction
num_terms_slider = widgets.IntSlider(value=10, min=1, max=20, step=1, description='n_Terms:')
scale_factor_slider = widgets.FloatSlider(value=1.0, min=0.1, max=5.0, step=0.1, description='Scale:')
add_button = widgets.Button(description='Add Sequence')
dropdown = widgets.Dropdown(options=[], description='Select Sequence:', layout={'width': '400px'})


# Event handlers
def add_button_clicked(b):
    add_to_dataframe(num_terms_slider.value, scale_factor_slider.value)


add_button.on_click(add_button_clicked)
dropdown.observe(dropdown_eventhandler, names='value')

# Display widgets
display(num_terms_slider)
display(scale_factor_slider)
display(add_button)
display(dropdown)
