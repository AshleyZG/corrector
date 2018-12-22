# ocr-lm

## ocr 预测数据的规格
预测数据集：test  
ocr预测方式：首先将所有文本都拼接成一个字符串，然后按$m=15$，$\mu=3$的高斯分布切分文本为多行，ocr模型按行预测。  
预测结果：返回dict，3个key：'gold_text'，'ocr_preciction'，'ocr_probabilities'(top 30)  


## 不同blurry level 的参数设定
* clear- 将augmentation 设置为False即可  
* blurry- [configuration](./config/blurry.py)   
* blurry2- not set yet  
