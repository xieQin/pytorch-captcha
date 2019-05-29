### pytorch 基于CNN的验证码识别

#### 安装依赖
```python
pip3 install -r requirements.txt
```

#### 实现思路
- 获取图片
- 灰度二值化
- 裁切成单个数字或字母
- 基于CNN训练识别单个验证码的数据模型，单个验证码识别成功率98%

#### 使用方法

- 生成训练数据
```python
python main.py
```

- 训练数据集
```python
python captcha_train.py
```

- 测试数据集
```python
python captcha_test.py
```
