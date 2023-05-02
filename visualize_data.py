import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def visualize():
    # Load the data from the CSV file
    df = pd.read_csv('real_estate_data.csv')

    # Create a scatter plot of the latitude and longitude, colored by neighbourhood and sized by price
    sns.scatterplot(x='Longitude', y='Latitude', data=df, hue='Neighbourhood', size='Price', sizes=(50, 500))

    # Set the title and axis labels
    plt.title('Real Estate Prices in Toronto')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    # Show the plot
    plt.show()


if __name__ == '__main__':
    visualize()
