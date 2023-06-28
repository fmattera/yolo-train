import os

def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            process_file(file_path)

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.strip().split() for line in lines if len(line.strip().split()) == 5]
        processed_lines = [' '.join(line) for line in lines]
    
    with open(file_path, 'w') as file:
        file.write('\n'.join(processed_lines))


folder_path = r'C:\Users\Shadow\Documents\NeoLocus\11_04_23_backup\yolo-train\valid\labels'
process_folder(folder_path)
