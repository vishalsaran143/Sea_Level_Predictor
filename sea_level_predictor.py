import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_sea_level_plot():
    # Read data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Perform linear regression
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Predict sea level rise in 2050 using all data
    plt.plot([df['Year'].min(), 2050], [slope * df['Year'].min() + intercept, slope * 2050 + intercept], color='red', label='Line of Best Fit (All Data)')

    # Filter data from year 2000
    df_recent = df[df['Year'] >= 2000]

    # Perform linear regression for recent data
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Predict sea level rise in 2050 using recent data
    plt.plot([2000, 2050], [slope_recent * 2000 + intercept_recent, slope_recent * 2050 + intercept_recent], color='green', label='Line of Best Fit (Recent Data)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Add legend
    plt.legend()

    # Save and show plot
    plt.tight_layout()
    plt.savefig('sea_level_rise.png')
    plt.show()

if __name__ == "__main__":
    draw_sea_level_plot()
