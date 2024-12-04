from ultralytics import YOLO
import os
os.chdir('./model')

# Load a model,Export to onnx with simplify
model = YOLO("yolov9t.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
model = YOLO("yolov9s.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
model = YOLO("yolov9m.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
#model = YOLO("yolov9e.pt")
#model.info()
#model.export(format='onnx', simplify=True,opset=17)


# Load a model,Export to onnx with simplify
#model = YOLO("yolov9c.pt")
#model.info()
#model.export(format='onnx', simplify=True,opset=17)




