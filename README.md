# ax_model_convert_YOLO9to10


## Docker

Dockerのロード

```
$ sudo docker load -i ax_pulsar2_3.2_patch1_temp_vlm.tar.gz
```

Dockerの起動
```
$ sudo docker run -it --net host --rm -v $PWD:/data pulsar2:temp-58aa62e4
```


```
$ python yolo11_cut-onnx.py


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
