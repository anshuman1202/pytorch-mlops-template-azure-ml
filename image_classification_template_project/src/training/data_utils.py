import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
import torch
import urllib

from torchvision import datasets, transforms
from zipfile import ZipFile


def download_data():
    """Download and extract the training data."""
    
    # download data
    print("Downloading archive file...")
    archive_file = "../data/fowl_data.zip"
    download_url = "https://azureopendatastorage.blob.core.windows.net/testpublic/temp/fowl_data.zip"
    urllib.request.urlretrieve(download_url, filename=archive_file)

    # extract files
    with ZipFile(archive_file, "r") as zip:
        print("Extracting files...")
        zip.extractall("../data")
        print("Finished extracting!")
        data_dir = os.path.join("../data", zip.namelist()[0])

    # delete zip file
    os.remove(archive_file)
    return data_dir


def load_data(data_dir):
    """Load the train/val data."""

    # Data augmentation and normalization for training
    # Just normalization for validation
    data_transforms = {
        "train": transforms.Compose([
            transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
        "val": transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
    }

    image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x),
                                              data_transforms[x])
                      for x in ["train", "val"]}
    
    dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=4,
                                                  shuffle=True, num_workers=4)
                   for x in ["train", "val"]}
    
    dataset_sizes = {x: len(image_datasets[x]) for x in ["train", "val"]}
    
    class_names = image_datasets["train"].classes

    return dataloaders, dataset_sizes, class_names


def imshow(img):
    img = img / 2 + 0.5 # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0))) # transpose dimensions from Pytorch format to default numpy format
    plt.show()