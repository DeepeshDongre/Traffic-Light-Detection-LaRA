#!/bin/bash
model=$1 #= faster_rcnn, ssd_inception, ssd_mobilenet
tf_research_path=/nfs/private/models/research

mkdir -p models/training_$model
python $tf_research_path/object_detection/train.py \
    --pipeline_config_path=config/$model.config \
    --train_dir=models/training_$model
