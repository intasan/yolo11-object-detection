from ultralytics import YOLO

# Project training configuration documented from the original environment.
MODEL = 'yolo11n.pt'
DATA = 'data.yaml'

model = YOLO(MODEL)
model.train(
    data=DATA,
    epochs=300,
    batch=8,
    imgsz=640,
    device=0,
    project='runs',
    name='yolo11n'
)
