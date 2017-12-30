#!/bin/bash
model=$1
rm models/evaluating_$model/events.out.*
rm models/training_$model/events.out.*
rm -r models/evaluating_$model
rm -r models/training_$model
rm -r models/frozen_$model
