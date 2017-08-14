import numpy as np
import os
import random

def read_dateset(data_path):
    train_rec = get_rec(data_path, "train") 
    val_rec = get_rec(data_path, "val") 
    return train_rec, val_rec

def get_rec(segtxt, name):
    segtxt = data_path + "ImageSets/Segmentation/"
    lst = []
    filename = segtxt + name + ".txt" 
    fin = open(filename)
    for line in fin.readlines():
        fn = line.strip()
        image = data_path + "JPEGImages/" + fn + ".jpg"
        ann = data_path + "SegmentationClass/" + fn + ".png"
        lst.append(dict({
            "image": image,
            "annotation":ann
        }))
    return lst
