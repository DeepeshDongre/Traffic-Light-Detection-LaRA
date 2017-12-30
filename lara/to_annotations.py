import pickle
import sys
import os
import datetime
import argparse
import logging
import StringIO
import csv
import json
import gzip, shutil
import hashlib
import subprocess
import random

TEST_RATIO = 0.1

def write_image_yaml(o, idx, boxes):
    o.write('- annotations:\n')
    for box in boxes:
        o.write(box + '\n')

    tail = '''  class: image
  filename: Lara3D_UrbanSeq1_JPG/frame_{idx}.jpg'''.format(idx='%06d'%idx)
    o.write(tail + '\n')

def convert(fin, fout_prefix):
    images = {}
    with open(fin) as f:
        for line in f.readlines():
            idx_, x1, y1, x2, y2, _, name = line.strip().split()
            idx = int(idx_)
            dx = int(x2) - int(x1)
            dy = int(y2) - int(y1)
            if dx < 1 or dy < 1:
                continue
            
            box = '  - {class: %s, x_width: %d, xmin: %s, y_height: %d, ymin: %s}' % (name, dx, x1, dy, y1)
            images.setdefault(idx, []).append(box)

    
    with open(fout_prefix + '_train.yaml', 'w') as tr:
        with open(fout_prefix + '_test.yaml', 'w') as te:
            for idx, boxes in images.items():
                if random.random() < TEST_RATIO:
                    write_image_yaml(te, idx, boxes)
                else:
                    write_image_yaml(tr, idx, boxes)

if __name__ == '__main__':
    convert('ground_truth.txt', 'annotations')
