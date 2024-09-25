import csv
import os

def process_large_csv(file_path):
    # Define the base directory where you want to store your token folders
    # We assume this is called "token_data" and is located in the same directory as the script
    base_dir = 'token_data'

    # Ensure the base directory exists
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Skip header row and save it for file writing
        
        for row in reader:
            if not row:  # Skip empty rows if there are any
                continue
            
            token_address = row[0]
            token_directory = os.path.join(base_dir, token_address)
            
            # Ensure the token directory exists
            if not os.path.exists(token_directory):
                os.makedirs(token_directory)
            
            token_file_path = os.path.join(token_directory, 'token_transfer.csv')
            
            # Check if the file already exists, if not create and write the header
            if not os.path.exists(token_file_path):
                with open(token_file_path, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(header)  # Write the header for the new file
            
            # Append the transaction to the token file
            with open(token_file_path, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(row)

# Usage
# Assuming the CSV file is located at 'path_to_your_large_file.csv'
process_large_csv('sample_data/sample_token_transfer.csv')

