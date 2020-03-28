# BadApple 视频转字符动画

## 运行 `play.py` 的方法：

``` bash
./play.py
```

推荐在 Posix 系统下运行。

## 运行 `main.py` 的方法：

### 0 安装 OpenCV

``` bash
pip3 install opencv-python
```

不保证能成功。

接下来看看到底有没有安装成功：

``` bash
python3 -c "import cv2; print(cv2.__version__)"
```

如果输出了诸如 `4.2.0` 之类的版本号，就大概成功了。

### 1 下载 BadApple 的 mp4 视频

HTTPS URL：`https://wshtan.net/ar/badapple.mp4`

也不保证能成功。

### 2 运行 `main.py`

``` bash
./main.py
```

