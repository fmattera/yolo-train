# yolo-train


1) Gather different datasets (one per object works just fine) from roboflow.com
2) Change the labels in the .txt files starting from 80 (e.g. 80, 81, 82, ...)
3) Resize the images to 640 or 1024
4) Build the data.yaml config file 
5) Train YOLO 


## Example of working data.yaml

You can find the best model so far in runs/detect/train6


## Fine tuning YOLO 

from a pretrained model having the 79 classes:

yolo task=detect mode=train model=yolov8l.pt data=data.yaml epochs=180 imgsz=640 workers=1 batch=10

model can be [yolov8n.pt, yolov8s.pt, yolov8m.pt, yolov8l.pt, yolov8x.pt]


## Train YOLO from skratch

yolo task=detect mode=train model=yolov8m.yaml data=data.yaml epochs=100 imgsz=640

model can be [yolov8n.yaml, yolov8s.yaml, yolov8m.yaml, yolov8l.yaml, yolov8x.yaml]

## Predict on the test set data
yolo predict model=runs\detect\train6\weights\best.pt source=C:\Users\Shadow\Documents\NeoLocus\11_04_23_backup\yolo-train\test\images
