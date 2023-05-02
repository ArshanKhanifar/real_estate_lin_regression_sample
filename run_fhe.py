import pandas as pd
from concrete.ml.sklearn import LinearRegression


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
    model = LinearRegression().fit(X_train, y_train)

    # Evaluate the model on the testing data
    X_test = test_data[['Latitude', 'Longitude', 'Neighbourhood']]
    y_test = test_data['Price']
    score = model.score(X_test, y_test)

    # Print the R^2 score of the model
    print(f'R^2 score: {score:.2f}')

    # We then compile on a representative set
    model.compile(X_train)

    # Predict the price of a new property
    lat = 43.76
    lon = -79.45
    neighbourhood = neighbourhood_map['West End']
    price_clear = model.predict([[lat, lon, neighbourhood]])
    price_fhe = model.predict([[lat, lon, neighbourhood]], fhe="execute")

    print(f'Predicted price: ${price_clear[0][0]:,.2f}')
    print(f'FHE price: ${price_fhe[0][0]:,.2f}')


if __name__ == '__main__':
    train_and_eval()
