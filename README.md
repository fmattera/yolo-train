# yolo-train


1) Gather different datasets (one per object works just fine) from roboflow.com
2) Change the labels in the .txt files starting from 80 (e.g. 80, 81, 82, ...)
3) Resize the images to 640 or 1024
4) Build the data.yaml config file 
5) Train YOLO 


## Example of working data.yaml

train: /home/f_mattera_it/yolo-train/train/images
val: /home/f_mattera_it/yolo-train/valid/images
test: /home/f_mattera_it/yolo-train/test/images

nc: 82

names: ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
        'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
        'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
        'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
        'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
        'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
        'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
        'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
        'hair drier', 'toothbrush', 'cabinet','shelf','lamp']


## Fine tuning YOLO 

from a pretrained model having the 79 classes:

yolo task=detect mode=train model=yolov8m.pt data=data.yaml epochs=100 imgsz=640

model can be [yolov8n.pt, yolov8s.pt, yolov8m.pt, yolov8l.pt, yolov8x.pt]


## Train YOLO from skratch

yolo task=detect mode=train model=yolov8m.yaml data=data.yaml epochs=100 imgsz=640

model can be [yolov8n.yaml, yolov8s.yaml, yolov8m.yaml, yolov8l.yaml, yolov8x.yaml]