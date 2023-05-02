import random
def gen_sample_data():

    # Set parameters for the data
    num_properties = 100
    min_price = 500000
    max_price = 2000000

    # Generate random data for real estate prices
    prices = [random.randint(min_price, max_price) for _ in range(num_properties)]

    # Print the prices
    print(prices)

if __name__ == '__main__':
    print_hi('PyCharm')
