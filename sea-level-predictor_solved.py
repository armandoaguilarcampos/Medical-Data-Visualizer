import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(df['Year'].min(), 2051))
    line = slope * years_extended + intercept
    plt.plot(years_extended, line, color='red')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(df_recent['Year'].min(), 2051))
    line = slope * years_extended + intercept
    plt.plot(years_extended, line, color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.grid()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()