import numpy as np
import pandas as pd

def generate():
    # Define the neighbourhoods and their respective price multipliers
    neighbourhoods = {'Downtown': 2.0, 'West End': 1.5, 'East End': 1.2, 'North End': 1.0}

    # Generate random location data for 100 properties
    latitudes = np.random.uniform(43.6, 43.8, 100)
    longitudes = np.random.uniform(-79.5, -79.2, 100)

    # Assign neighbourhoods based on latitude and longitude ranges
    neighbourhood = []
    for lat, lon in zip(latitudes, longitudes):
        if lat >= 43.75 and lon >= -79.35:
            neighbourhood.append('Downtown')
        elif lat >= 43.7 and lon <= -79.4:
            neighbourhood.append('West End')
        elif lat <= 43.68 and lon <= -79.4:
            neighbourhood.append('East End')
        else:
            neighbourhood.append('North End')

    # Compute prices based on neighbourhood multipliers and random variation
    prices = [np.random.normal(750000 * neighbourhoods[n], 100000) for n in neighbourhood]

    # Create a DataFrame with the data
    data = {'Latitude': latitudes, 'Longitude': longitudes, 'Neighbourhood': neighbourhood, 'Price': prices}
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv('real_estate_data.csv', index=False)


if __name__ == '__main__':
    generate()
