[//]: # (Image References)
[i3738]: ./examples/frame_003738.jpg
[aloss]: ./examples/TotLoss.png

# Traffic Light Detection

Implemented with TensorFlow Object Detection API. 

Tested on LaRA dataset.

Model inference example:

![alt-text][i3738]

Check out the rendered video in 
[Youtube](https://youtu.be/BcPy9m__bY4) or 
[BaiduPan](https://pan.baidu.com/s/1slwWdBJ)


## LaRA Traffic Lights Recognition (TLR) Public Benchmarks

On-board vehicle acquisition in a dense urban environment:

- 11179 frames (8min 49sec, @25FPS)
- 640×480 (RGB, 8bits)
- Paris (France)

Links:

- Download [Dataset download link](http://s150102174.onlinehome.fr/Lara/files/Lara_UrbanSeq1_JPG.zip)

- Download [Ground truth labels](http://s150102174.onlinehome.fr/Lara/files/Lara_UrbanSeq1_GroundTruth_GT.txt)

- [A detailed dataset description](http://www.lara.prd.fr/benchmarks/trafficlightsrecognition)

To make TFRecord files for Tensorflow tranning, read [this](lara/README.md)


## Performance

Here records an informal test performance on 592 unseen images:

- Model = SSD MobileNet, pre-trained on COCO 
- Infer time per image = 9 ms 
- Green  light AP@0.5IOU = 0.385
- Red    light AP@0.5IOU = 0.725
- Yellow light AP@0.5IOU = 0.385
- Precision   mAP@0.5IOU = 0.620

*Running on Tesla P40 GPU*

Training total loss:

![alt-text][aloss]


### Get the tensorflow models lib

Do `git clone https://github.com/tensorflow/models.git` and update directory in .sh files

Follow the instructions at [this page](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md) for installing some simple dependencies.

Location of pre-trained models:
[pre-trained models zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md)

Download the required model tar.gz files and untar them into `models/` directory with `tar -xvzf name_of_tar_file`.


### Creating TFRecord files:

`python data_conversion.py --input_yaml lara/annotations_train.yaml --output_path lara/train.record`

`python data_conversion.py --input_yaml lara/annotations_test.yaml --output_path lara/test.record`


### Training, Evaluating, and Tensorboarding

`sh train.sh <faster_rcnn | ssd_inception | ssd_mobilenet>`

`sh evaluate.sh <faster_rcnn | ssd_inception | ssd_mobilenet>`

`tensorboard --logdir=models --port=8052`

*note you'd better not run train & evaluate together because they will use up GPU memory*


### Saving Weights for Inference

`sh freeze.sh <faster_rcnn | ssd_inception | ssd_mobilenet> <model checkpoint version num>`


### Infer Results, Visualize, and Make Video
using the `TrafficLightDetection-Inference.ipynb`


###