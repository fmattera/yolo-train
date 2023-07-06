import os

# Set the path to the folder containing the .txt files
folder_paths = [
r'C:\Users\Shadow\Documents\NeoLocus\11_04_23_backup\yolo-train\test\labels',
r'C:\Users\Shadow\Documents\NeoLocus\11_04_23_backup\yolo-train\train\labels',
r'C:\Users\Shadow\Documents\NeoLocus\11_04_23_backup\yolo-train\valid\labels',]



#[CUPBPORD,LAMP,SHELF]

for folder_path in folder_paths:
    # Get the list of .txt files in the folder
    file_list = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

    # Iterate over each file
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        
        # Read the contents of the file
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Modify the lines
        modified_lines = []
        for line in lines:
            parts = line.strip().split(' ')
            parts[0] = str(int(parts[0]) + 80)  # Modify the first element
            
            modified_line = ' '.join(parts) + '\n'
            modified_lines.append(modified_line)
        
        # Write the modified lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(modified_lines)




