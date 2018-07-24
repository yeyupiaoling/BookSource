# 第六章
## 目录介绍
1. `code`为存放代码的文件夹
2. `images`为存放裁剪前的验证码,裁剪后的验证码,下载的验证码和做预测临时的图片
3. `model`为存放训练后的模型,因为没有上传,可能不存在
4. `data`为存放每个类别的图像数据列表和数据说明

## 代码介绍
1. `train.py`为训练模型的程序
2. `infer.py`为预测数据的程序
3. `vgg.py`为VGG升级网络的定义
4. `CreateDataList.py`创建用于训练与测试的图像列表
5. `DownloadYanZhengMa.py`下载验证码程序
6. `MyReader.py`读取图像列表
7. `CorpYanZhengMa.py`把验证码裁剪成四个图片
8. `cnn.py`为LeNet-5神经网络的定义



## 测试环境
1. Python 2.7
2. PaddlePaddle 0.11.0

