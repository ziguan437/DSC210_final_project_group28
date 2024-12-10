import os
import random
from torchvision.datasets import CIFAR10
from PIL import Image
from sklearn.model_selection import train_test_split

def download_and_prepare_cifar10(root_dir, val_split=0.2):
    # Download CIFAR-10 dataset
    cifar10 = CIFAR10(root=root_dir, download=True)

    # Create directories for train and validation sets
    for class_name in cifar10.classes:
        train_class_dir = os.path.join(root_dir, 'cifar10', 'train', class_name)
        val_class_dir = os.path.join(root_dir, 'cifar10', 'val', class_name)
        os.makedirs(train_class_dir, exist_ok=True)
        os.makedirs(val_class_dir, exist_ok=True)

    # Split the dataset into train and validation sets
    indices = list(range(len(cifar10)))
    train_indices, val_indices = train_test_split(indices, test_size=val_split, stratify=cifar10.targets)

    # Save images to the respective class directories
    for idx in train_indices:
        img, target = cifar10[idx]
        class_name = cifar10.classes[target]
        img_path = os.path.join(root_dir, 'cifar10', 'train', class_name, f'{idx}.png')
        img.save(img_path)

    for idx in val_indices:
        img, target = cifar10[idx]
        class_name = cifar10.classes[target]
        img_path = os.path.join(root_dir, 'cifar10', 'val', class_name, f'{idx}.png')
        img.save(img_path)

# Define the root directory where the dataset will be stored
root_dir = './data'
download_and_prepare_cifar10(root_dir)