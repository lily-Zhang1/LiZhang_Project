from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

import csv
import os

from PIL import Image

normalize = transforms.Normalize(
    mean=[0.485, 0.456, 0.406],
    std=[0.229, 0.224, 0.225]
)
preprocess = transforms.Compose([
    transforms.RandomSizedCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    normalize
])

def default_loader(path):
    img_pil =  Image.open(path)
    if img_pil.mode == "RGBA":
        r,g,b,a = img_pil.split()
        img_pil = Image.merge("RGB", (r,g,b))

    img_tensor = preprocess(img_pil)
    return img_pil

class TrainSet(Dataset):

    def __init__(self, transforms, loader=default_loader, size='z19',loc = "manhattan", csv_file = 'train.csv'):
        self.images, self.target, self.names = self.get_data(size, loc, csv_file)
        self.loader = loader
        self.trans = transforms


    def __getitem__(self, index):
        fn = self.images[index]
        img_pil = Image.open(fn)

        img = self.loader(fn)
        img = self.trans(img)
        target = self.target[index]
        name = self.names[index]
        #print("labels:",target)
        return {'input': img, 'target': target, 'name': name}

    #return the number of images
    def __len__(self):
        return len(self.images)

	#return image list and tag list
    def get_data(self, size, loc, csv_file = "train.csv"):
        loc = "tiles_"+loc
        file_dir = os.path.join("train_map",loc, loc+"_2019")
        imgs = []
        tags = []
        names = []
        with open(csv_file, "r") as f:
            reader = csv.reader(f)
            #print(len(reader))

            for row in reader:
            	 #the first column is the image name
                if(csv_file == './test/test.csv'):
                    print(row)
                file_name = os.path.join(file_dir, size , row[0]+".png")
                #if(csv_file == './test/test.csv'):
                #  print(file_name)
                #exit(0)
                names.append(row[0])
                if os.path.exists(file_name):
                	#image list
                    imgs.append(file_name)
                    #Converts four binary tags to a decimal tag
                    tag = float(row[4]) * 8 + float(row[5]) * 4 + float(row[6]) * 2 + float(row[7])
                    # tag list
                    tags.append(int(tag))
                else:
                    pass
                    #print('wrong! ', file_name)

        print(len(imgs))
        return imgs, tags, names

#set = TrainSet()
