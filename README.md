# corrector

## 文件存储说明

**gpu001:**  
**fin_news**- '/data/sharedata/cv/shannon_vision/lm/corpus/fin_news'  
**wiki**- '/data/sharedata/cv/shannon_vision/lm/corpus/wiki'  

**gpu003**  
**fin_news**- '/home/zhangge/data/corpus/fin_news'  
**wiki**- '/home/zhangge/data/corpus/wiki'  

### 子目录
train/valid/test- 最原始的语料，文件夹中是所有的txt文件。  
train_ocr/valid_ocr/test_ocr- 对应的可用于ocr预测的合并后的文本，以及ocr识别后的文本  
prediction- 不同文件夹代表不同的blurry level，里面包括ocr在各个数据集上的识别结果，其中test应该包含概率  

## ocr 预测数据的规格
预测数据集：test  
ocr预测方式：首先将所有文本都拼接成一个字符串，然后按 $$m=15$$ ， $$\mu=3$$ 的高斯分布切分文本为多行，ocr模型按行预测。  
预测结果：返回dict，3个key：'gold_text'，'ocr_preciction'，'ocr_probabilities'(top 30)  


## 不同blurry level 的参数设定
* clear- 运行inference.py 时将blurry level 设为 clear 即可  
* blurry- [config](./config/blurry.py)   
* blurry2- [config](./config/blurry2.py) 在fin_news test 上的准确率为0.96左右  
* blurry3- [config](./config/blurry3.py) 在fin_news test 上的准确率为0.94左右  
* blurry4- [config](./config/blurry4.py) 在fin_news test 上的准确率为0.92左右  

## 纠正效果
### OCR+LM
|Model |Error Rate |        | Dataset        |
|------|-----------|--------|----------------|
|OCR   |0.093000   |0.907000|fin_news_blurry4|
|1\*3  |0.091557   |0.908443|                |
|V\*3  |0.091028   |0.908972|                |
|1\*W x \[tanh W\*V x V\*3\]  |0.093355   |0.906645|                |
