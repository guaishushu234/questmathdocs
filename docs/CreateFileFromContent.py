import os

# Define the path to the content file
content_file_path = 'content.txt'

# Read the content file
try:
    with open(content_file_path, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"The file {content_file_path} does not exist.")
    exit()

# Process each line
for line in lines:
    # Split the line into title and file location
    title, file_path = line.strip().split(': ')

    # Create the directory if it does not exist
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Write the title to the file
    with open(file_path, 'w') as file:
        file.write(f"# {title}\n")

print("The files have been created and the titles have been written.")
