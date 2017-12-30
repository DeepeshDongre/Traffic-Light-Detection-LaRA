# LaRA Traffic Lights Recognition (TLR) public benchmarks

On-board vehicle acquisition in a dense urban environment:

- 11179 frames (8min 49sec, @25FPS)
- 640×480 (RGB, 8bits)
- Paris (France)

Links:

- Download [Dataset download link](http://s150102174.onlinehome.fr/Lara/files/Lara_UrbanSeq1_JPG.zip)

- Download [Ground truth labels](http://s150102174.onlinehome.fr/Lara/files/Lara_UrbanSeq1_GroundTruth_GT.txt)

- [A detailed dataset description](http://www.lara.prd.fr/benchmarks/trafficlightsrecognition)


## Make TFRecord files for Tensorflow model training

cd to `./lara`

Manually preprocess `Lara_UrbanSeq1_GroundTruth_GT.txt` to `ground_truth.txt`

`python to_annotations.py` to split data into training and test set, and generate annotation files in YAML format.