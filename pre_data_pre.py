from data_preprocess import process_raw_data, editnet_data_to_editnetID

# Load data from files
with open('data/INT.txt', 'r') as f:
    comp_txt = f.read().splitlines()

with open('data/ELE.txt', 'r') as f:
    simp_txt = f.read().splitlines()

# Step 1: Process raw data
processed_data = process_raw_data(comp_txt, simp_txt)

# Step 2: Convert data to EditNTS format and save to a pickle file
editnet_data_to_editnetID(processed_data, 'processed_data.pkl')