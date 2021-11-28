import json
import os
import glob

train_folder_list = os.listdir('./Training/')
category_list = os.listdir('./Training/{}'.format(train_folder_list[0]))
data_folder_list = os.listdir('./Training/{}/{}'.format(train_folder_list[0], category_list[0]))
data_list = os.listdir('./Training/{}/{}/{}'.format(train_folder_list[0], category_list[0], data_folder_list[0]))
print(data_list[0])

data_path = './Training/{}/{}/{}/{}'.format(train_folder_list[0], category_list[0], data_folder_list[0], data_list[0])
print(data_path)

with open(data_path, 'r')as f:
    print(json.load(f))
