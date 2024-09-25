import csv
import os

#This will sort the CSV file by 'block_number' and save it in the same directory
def sort_and_save_csv(input_file_path, output_file_path):
    # This function reads the CSV at input_file_path, sorts it by 'block_number', and saves it to output_file_path
    try:
        with open(input_file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)  # Extract header
            sorted_data = sorted(reader, key=lambda x: int(x[-1]))  # Sort by block_number assumed to be the last column

        with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)  # Write header first
            writer.writerows(sorted_data)  # Write sorted data
    except Exception as e:
        print(f"An error occurred while processing {input_file_path}: {str(e)}")

#This will run the CSV on all the directories
def process_directories(base_dir):
    # Walk through each directory and subdirectory starting from the base directory
    for root, dirs, files in os.walk(base_dir):
        for filename in files:
            if filename == 'token_transfer.csv':
                input_file = os.path.join(root, filename)
                output_file = os.path.join(root, 'ordered_token_transfer.csv')
                print(f"Sorting and writing to: {output_file}")
                sort_and_save_csv(input_file, output_file)

# Define the base directory that contains all token subdirectories
base_directory = 'token_data'

# Process each directory
process_directories(base_directory)

