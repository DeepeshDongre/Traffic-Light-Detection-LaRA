
[//]: # (Image References)
[real0000]: ./examples/real0000.png

# Traffic Light Detection and Classification with TensorFlow Object Detection API

The project is forked from https://github.com/coldKnight/TrafficLight_Detection-TensorFlowAPI.git

A brief introduction to the project is available [here](https://medium.com/@Vatsal410/traffic-light-detection-tensorflow-api-c75fdbadac62)


### Get the dataset

[Drive location](https://drive.google.com/file/d/0B-Eiyn-CUQtxdUZWMkFfQzdObUE/view?usp=sharing)


### Get the tensorflow models lib

Do `git clone https://github.com/tensorflow/models.git` and update directory in .sh files

Follow the instructions at [this page](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md) for installing some simple dependencies.

Location of pre-trained models:
[pre-trained models zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md)

Download the required model tar.gz files and untar them into `models/` directory with `tar -xvzf name_of_tar_file`.


### Creating TFRecord files:

`python data_conversion.py --input_yaml data/training_data/annotations_train.yaml --output_path data/train.record`

`python data_conversion.py --input_yaml data/training_data/annotations_eval.yaml --output_path data/eval.record`


## Using Faster-RCNN / Inception SSD v2 / MobileNet SSD v1 model

#### Training, Evaluating, and Tensorboarding

`sh train.sh <faster_rcnn | ssd_inception | ssd_mobilenet>`

`sh evaluate.sh <faster_rcnn | ssd_inception | ssd_mobilenet>`

`tensorboard --logdir=models --port=8052`

*note you'd better not run train & evaluate together because they will use up GPU memory*

#### Saving Weights for Inference

`sh freeze.sh <faster_rcnn | ssd_inception | ssd_mobilenet> <model checkpoint version num>`
---


**Inference results can be viewed using the TrafficLightDetection-Inference.ipynb or .html files.**

### Camera Image and Model's Detection Sample
![alt-text][real0000]
