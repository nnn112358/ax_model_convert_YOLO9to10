# ax_model_convert_YOLO9to10

### 目的
[axera-tech](https://github.com/AXERA-TECH/ax-samples/)のサンプルプログラムの内、
yolov9とyolov10のプログラムの実行に必要なモデルの変換を行う。
ソースコードは、ax620e/ax_yolov9_ultralytics_steps.ccとax620e/ax_yolov10_ultralytics_steps.ccに対応する。

https://github.com/AXERA-TECH/ax-samples/


### Dockerの起動

Dockerに、Pulsar2のイメージをロード。

```
sudo docker load -i ax_pulsar2_3.2_patch1_temp_vlm.tar.gz
```

### ultralyticsのインストール

```
$ pip install ultralytics
```


### モデル変換の実施

以下のPythonプログラムを実行。

```
$ python yolov10_download.py
$ python yolov10_cut-onnx.py
$ python yolov9_cut-onnx.py
$ python yolov9_download.py
```

dockerでpulsar2を起動してスクリプトを実行。
```
$ sudo docker run -it --net host --rm -v $PWD:/data pulsar2:temp-58aa62e4
$ ./ax_model_convert.sh
```

axmodelを生成
```
# ls model/*axmodel
model/yolov10n.axmodel  model/yolov10s.axmodel  model/yolov9s.axmodel  model/yolov9t.axmodel
```


### M5Stack Module-LLMでの実行

 Module-LLMにコピーして、実行。
 
```
./ax_yolov10_u -i m52.jpg -m yolov10s.axmodel
./ax_yolov10_u -i m52.jpg -m yolov10m.axmodel
./ax_yolov10_u -i m52.jpg -m yolov10n.axmodel
./ax_yolov10_u -i m52.jpg -m yolov10n.axmodel
./ax_yolov9_u -i m52.jpg -m yolov9t.axmodel
./ax_yolov9_u -i m52.jpg -m yolov9s.axmodel
```
