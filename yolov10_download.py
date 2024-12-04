from ultralytics import YOLO
import os
os.chdir('./model')

# Load a model,Export to onnx with simplify
model = YOLO("yolov10n.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
model = YOLO("yolov10s.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
model = YOLO("yolov10m.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
model = YOLO("yolov10l.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
model = YOLO("yolov10x.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)





