import numpy as np
import os
import random

DATA_PATH = "./Data_zoo/VOCtrainval_11-May-2012/VOCdevkit/VOC2012/"
def read_dateset():
    segtxt = DATA_PATH + "ImageSets/Segmentation/"
    train_rec = get_rec(segtxt, "train") 
    val_rec = get_rec(segtxt, "val") 
    return train_rec, val_rec

def get_rec(segtxt, name):
    lst = []
    filename = segtxt + name + ".txt" 
    fin = open(filename)
    for line in fin.readlines():
        fn = line.strip()
        image = DATA_PATH + "JPEGImages/" + fn + ".jpg"
        ann = DATA_PATH + "SegmentationClass/" + fn + ".png"
        lst.append(dict({
            "image": image,
            "annotation":ann
        }))
    return lst
