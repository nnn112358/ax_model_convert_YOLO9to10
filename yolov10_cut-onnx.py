import onnx
import os

def extract_onnx_model(input_path, output_path):
   
   input_names = ["images"]
   output_names = [
       "/model.23/Concat_output_0",
       "/model.23/Concat_1_output_0", 
       "/model.23/Concat_2_output_0"
   ]

   onnx.utils.extract_model(input_path, output_path, input_names, output_names)

# Usage
os.chdir('./model')
extract_onnx_model("yolov10n.onnx", "yolov10n-cut.onnx")
extract_onnx_model("yolov10s.onnx", "yolov10s-cut.onnx")
extract_onnx_model("yolov10m.onnx", "yolov10m-cut.onnx")
extract_onnx_model("yolov10l.onnx", "yolov10l-cut.onnx")
extract_onnx_model("yolov10x.onnx", "yolov10x-cut.onnx")

