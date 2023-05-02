# Define the name of the CSV file
CSV_FILE := real_estate_data.csv

.PHONY: $(CSV_FILE)

# Install the required packages in a new conda environment
install:
	conda create --name real-estate python
	conda activate real-estate
	pip install -r requirements.txt

# Generate the real estate data if the file does not exist
$(CSV_FILE):
	test -f $(CSV_FILE) || python generate_data.py

# Visualize the real estate data
visualize_data: $(CSV_FILE)
	python visualize_data.py

# Train and run the linear regression model
run: $(CSV_FILE)
	python run_model.py
