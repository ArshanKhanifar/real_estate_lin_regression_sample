import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


def train_and_eval():
    # Load the data from the CSV file
    df = pd.read_csv('real_estate_data.csv')

    # Encode the neighbourhoods as numerical values
    neighbourhood_map = {'North End': 0, 'East End': 1, 'West End': 2, 'Downtown': 3}
    df['Neighbourhood'] = df['Neighbourhood'].map(neighbourhood_map)

    # Split the data into training and testing sets
    train_data = df.sample(frac=0.8, random_state=0)
    test_data = df.drop(train_data.index)

    # Train a linear regression model on the training data
    X_train = train_data[['Latitude', 'Longitude', 'Neighbourhood']]
    y_train = train_data['Price']
    reg = LinearRegression().fit(X_train, y_train)

    # Evaluate the model on the testing data
    X_test = test_data[['Latitude', 'Longitude', 'Neighbourhood']]
    y_test = test_data['Price']
    score = reg.score(X_test, y_test)

    # Print the R^2 score of the model
    print(f'R^2 score: {score:.2f}')

    # Predict the price of a new property
    lat = 43.76
    lon = -79.45
    neighbourhood = neighbourhood_map['West End']
    price = reg.predict([[lat, lon, neighbourhood]])
    print(f'Predicted price: ${price[0]:,.2f}')
    visualize(df, lon, lat, price)


def visualize(df, lon, lat, predicted_price):
    # Compute the size of the circle
    max_size = df['Price'].max()

    # Create a scatter plot of the latitude and longitude, colored by neighbourhood and sized by price
    ax = sns.scatterplot(x='Longitude', y='Latitude', data=df, hue='Neighbourhood', size='Price', sizes=(50, 500))

    # Plot the predicted point
    ax.scatter(lon, lat, color='red', marker='x', label=f'Predicted price: ${predicted_price[0]:,.2f}')

    # Show the price of each house on the plot
    for i in range(len(df)):
        price = df['Price'][i]
        x = df['Longitude'][i]
        y = df['Latitude'][i]
        ax.text(x, y, f'${price:,.0f}', fontsize=8, ha='center', va='center')

    ax.text(lon, lat, f'${predicted_price[0]:,.0f}', fontsize=8, ha='center', va='center')

    # Set the title and axis labels
    plt.title('Real Estate Prices in Toronto')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()


if __name__ == '__main__':
    train_and_eval()
