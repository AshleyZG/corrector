# ocr-lm

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
* blurry- [configuration](./config/blurry.py)   
* blurry2- [configuration](./config/blurry2.py)  
