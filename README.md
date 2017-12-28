
[//]: # (Image References)
[left0000]: ./examples/left0000.jpg
[left0003]: ./examples/left0003.jpg
[left0011]: ./examples/left0011.jpg
[left0027]: ./examples/left0027.jpg
[left0140]: ./examples/left0140.jpg
[left0701]: ./examples/left0701.jpg

[real0000]: ./examples/real0000.png
[real0140]: ./examples/real0140.png
[real0701]: ./examples/real0701.png

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

#### Training

`sh train.sh <faster_rcnn | ssd_inception | ssd_mobilene>`

#### Saving Weights for Inference

`sh freeze.sh <faster_rcnn | ssd_inception | ssd_mobilene> <model checkpoint version num>`
---


**Inference results can be viewed using the TrafficLightDetection-Inference.ipynb or .html files.**

### Camera Image and Model's Detections      
![alt-text][left0000]
![alt-text][real0000]
