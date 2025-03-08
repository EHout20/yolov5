import os

# Path to the train_images directory
# train_images_dir = 'parking_dataset/train_images'
train_images_dir = 'parking_dataset/val_images'

# Iterate through all files in the train_images directory
for filename in os.listdir(train_images_dir):
    # Check if the file has a .txt extension
    if filename.endswith('.txt'):
        # Construct the full file path
        file_path = os.path.join(train_images_dir, filename)
        # Remove the file
        os.remove(file_path)
        print(f"Removed: {file_path}")

print("All .txt files removed from train_images directory.")