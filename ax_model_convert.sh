#!/bin/bash

# ログファイルの設定
LOG_FILE="build_$(date +%Y%m%d_%H%M%S).log"
exec 1> >(tee -a "$LOG_FILE")
exec 2> >(tee -a "$LOG_FILE" >&2)

echo "Build process started at $(date)"

# モデルビルド関数
build_model() {
    local input=$1
    local output=$2
    local config=$3
    
    echo "Building model: $input"
    pulsar2 build --input "$input" --output_dir output --config "$config" --target_hardware AX620E
    if [ $? -eq 0 ]; then
        cp output/compiled.axmodel "$output"
        echo "Successfully built and copied to $output"
    else
        echo "Error building model $input" >&2
        return 1
    fi
}

# YOLO検出モデル
build_model "model/yolov10n-cut.onnx" "model/yolov10n.axmodel" "config/yolov10_config.json"
build_model "model/yolov10s-cut.onnx" "model/yolov10s.axmodel" "config/yolov10_config.json"
build_model "model/yolov10m-cut.onnx" "model/yolov10m.axmodel" "config/yolov10_config.json"
build_model "model/yolov10l-cut.onnx" "model/yolov10l.axmodel" "config/yolov10_config.json"
build_model "model/yolov10x-cut.onnx" "model/yolov10x.axmodel" "config/yolov10_config.json"

build_model "model/yolov9t-cut.onnx" "model/yolov9t.axmodel" "config/yolov9_config.json"
build_model "model/yolov9s-cut.onnx" "model/yolov9s.axmodel" "config/yolov9_config.json"
build_model "model/yolov9m-cut.onnx" "model/yolov9m.axmodel" "config/yolov9_config.json"



echo "Build process completed at $(date)"