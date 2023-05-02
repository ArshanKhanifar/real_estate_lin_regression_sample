# Real Estate Price Prediction

This project uses machine learning to predict real estate prices in Toronto. It includes code to generate a realistic dataset of real estate prices using Python's `pandas` library, visualize the data using `matplotlib` and `seaborn`, and train a linear regression model using `scikit-learn`.

## Getting Started

To get started, you'll need to have Python 3.9 and `conda` installed on your machine. You can install `conda` by following the instructions on the [official conda website](https://docs.conda.io/en/latest/miniconda.html).

Once you have `conda` installed, you can create a new environment and install the required packages by running the following commands in your terminal or command prompt:

```sh
conda create --name real-estate python=3.9
conda activate real-estate
pip install -r requirements.txt
```

This will create a new environment called `real-estate` and install the necessary packages listed in the `requirements.txt` file.

### use the makefile (untested)
Or just run `make install` (haven't tested it but should work)

## Generating the Data

To generate the real estate data, you can run the following command:

```sh
make gen_data
```

This will generate a file called `real_estate_data.csv` in the current directory. This file contains information about the location, size, and price of different properties in Toronto.

## Visualizing the Data

To visualize the real estate data, you can run the following command:

```sh
make visualize_data
```

This will create a scatter plot of the real estate data using `matplotlib` and `seaborn`. The plot shows the location of each property on a map of Toronto, with the size and color of each point representing the price of the property.

## Training and Running the Model

To train and run the linear regression model, you can run the following command:

```sh
make run
```

This will train the model using the real estate data and print out the mean squared error (MSE) of the model on the training data. It will also make a scatter plot of the real estate data with the predicted prices shown as circles.

## Conclusion

This project demonstrates how to use machine learning to predict real estate prices in Toronto using Python. You can modify the code to use different datasets, train different models, and make different visualizations. Feel free to experiment and see what works best for your use case.
