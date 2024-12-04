import onnx
import os

def extract_onnx_model(input_path, output_path):
   
   input_names = ["images"]
   output_names = [
       "/model.22/Concat_output_0",
       "/model.22/Concat_1_output_0", 
       "/model.22/Concat_2_output_0"
   ]

   onnx.utils.extract_model(input_path, output_path, input_names, output_names)

# Usage
os.chdir('./model')
extract_onnx_model("yolov9s.onnx", "yolov9s-cut.onnx")
extract_onnx_model("yolov9t.onnx", "yolov9t-cut.onnx")
extract_onnx_model("yolov9m.onnx", "yolov9m-cut.onnx")
#extract_onnx_model("yolov9e.onnx", "yolov9e-cut.onnx")
#extract_onnx_model("yolov9c.onnx", "yolov9c-cut.onnx")



