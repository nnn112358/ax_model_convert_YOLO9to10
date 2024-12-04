# ax_model_convert_YOLO9to10


### Dockerの起動

```
$ sudo docker run -it --net host --rm -v $PWD:/data pulsar2:temp-58aa62e4
```

### ultralyticsのインストール

```
$ pip install ultralytics
```


### モデル変換の実施

```
$ python yolov10_download.py
$ python yolov10_cut-onnx.py
$ python yolov9_cut-onnx.py
$ python yolov9_download.py
$ ./ax_model_convert.sh
```

```
# ls model/*axmodel
model/yolov10n.axmodel  model/yolov10s.axmodel  model/yolov9s.axmodel  model/yolov9t.axmodel
```


# LLM　モジュールでの実行

```
./ax_yolov10_u -i m52.jpg -m yolov10s.axmodel
./ax_yolov10_u -i m52.jpg -m yolov10m.axmodel
./ax_yolov10_u -i m52.jpg -m yolov10n.axmodel
./ax_yolov10_u -i m52.jpg -m yolov10n.axmodel
./ax_yolov9_u -i m52.jpg -m yolov9t.axmodel
./ax_yolov9_u -i m52.jpg -m yolov9s.axmodel
```
