# jieba_parsing

##  1、jieba基本功能总结

### 1.1 jieba.test.demo模块展示的功能如下


```python
from __future__ import unicode_literals

import jieba
import jieba.posseg
import jieba.analyse
```


```python
print('='*40)
print('1. 分词')
print('-'*40)
```

    ========================================
    1. 分词
    ----------------------------------------
    


```python
seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式
```

    Building prefix dict from the default dictionary ...
    Loading model from cache C:\Users\86185\AppData\Local\Temp\jieba.cache
    Loading model cost 1.158 seconds.
    Prefix dict has been built successfully.
    

    Full Mode: 我/ 来到/ 北京/ 清华/ 清华大学/ 华大/ 大学
    


```python
seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 默认模式
```

    Default Mode: 我/ 来到/ 北京/ 清华大学
    


```python
seg_list = jieba.cut("他来到了网易杭研大厦")
print(", ".join(seg_list))
```

    他, 来到, 了, 网易, 杭研, 大厦
    


```python
seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))
```

    小明, 硕士, 毕业, 于, 中国, 科学, 学院, 科学院, 中国科学院, 计算, 计算所, ，, 后, 在, 日本, 京都, 大学, 日本京都大学, 深造
    


```python
print('='*40)
print('2. 添加自定义词典/调整词典')
print('-'*40)
```

    ========================================
    2. 添加自定义词典/调整词典
    ----------------------------------------
    


```python
print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
```

    如果/放到/post/中将/出错/。
    

Signature: jieba.suggest_freq(segment, tune=False)
Docstring:
Suggest word frequency to force the characters in a word to be
joined or splitted.
* 建议词频，以迫使一个词中的字符连接或分裂。

Parameter:
    - segment : The segments that the word is expected to be cut 
    into,If the word should be treated as a whole, use a str.
            
    - tune : If True, tune the word frequency.调单词频率。

Note that HMM may affect the final result. If the result doesn't change,
set HMM=False.

注意，HMM可能会影响最终结果。如果结果不变，则设置HMM=False。


```python
print(jieba.suggest_freq(('中', '将'), True))
```

    494
    


```python
print('/'.join(jieba.cut('如果放到post中将出错。')))
```

    如果/放到/post/中/将/出错/。
    


```python
print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
```

    如果/放到/post/中/将/出错/。
    


```python
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))
```

    「/台/中/」/正确/应该/不会/被/切开
    


```python
#「/台/中/」/正确/应该/不会/被/切开
print(jieba.suggest_freq('台中', True))
```

    69
    


```python
tokenizer.FREQ.get('台中')
```




    3




```python
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))
```

    「/台中/」/正确/应该/不会/被/切开
    


```python
print('='*40)
print('3. 关键词提取')
print('-'*40)
print(' TF-IDF')
print('-'*40)
```

    ========================================
    3. 关键词提取
    ----------------------------------------
     TF-IDF
    ----------------------------------------
    


```python
s = "此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。"
for x, w in jieba.analyse.extract_tags(s, withWeight=True):
    print('%s %s' % (x, w))
```

    欧亚 0.7300142700289363
    吉林 0.659038184373617
    置业 0.4887134522112766
    万元 0.3392722481859574
    增资 0.33582401985234045
    4.3 0.25435675538085106
    7000 0.25435675538085106
    2013 0.25435675538085106
    139.13 0.25435675538085106
    实现 0.19900979900382978
    综合体 0.19480309624702127
    经营范围 0.19389757253595744
    亿元 0.1914421623587234
    在建 0.17541884768425534
    全资 0.17180164988510638
    注册资本 0.1712441526
    百货 0.16734460041382979
    零售 0.1475057117057447
    子公司 0.14596045237787234
    营业 0.13920178509021275
    


```python
print('-'*40)
print(' TextRank')
print('-'*40)
```

    ----------------------------------------
     TextRank
    ----------------------------------------
    


```python
for x, w in jieba.analyse.textrank(s, withWeight=True):
    print('%s %s' % (x, w))
```

    吉林 1.0
    欧亚 0.9966893354178172
    置业 0.6434360313092776
    实现 0.5898606692859626
    收入 0.43677859947991454
    增资 0.4099900531283276
    子公司 0.35678295947672795
    城市 0.34971383667403655
    商业 0.34817220716026936
    业务 0.3092230992619838
    在建 0.3077929164033088
    营业 0.3035777049319588
    全资 0.303540981053475
    综合体 0.29580869172394825
    注册资本 0.29000519464085045
    有限公司 0.2807830798576574
    零售 0.27883620861218145
    百货 0.2781657628445476
    开发 0.2693488779295851
    经营范围 0.2642762173558316
    


```python
print('='*40)
print('4. 词性标注')
print('-'*40)
```

    ========================================
    4. 词性标注
    ----------------------------------------
    


```python
words = jieba.posseg.cut("我爱北京天安门")
for word, flag in words:
    print('%s %s' % (word, flag))
```

    我 r
    爱 v
    北京 ns
    天安门 ns
    


```python
print('='*40)
print('6. Tokenize: 返回词语在原文的起止位置')  #5呢？？？？
print('-'*40)
print(' 默认模式')
print('-'*40)
```

    ========================================
    6. Tokenize: 返回词语在原文的起止位置
    ----------------------------------------
     默认模式
    ----------------------------------------
    


```python
result = jieba.tokenize('永和服装饰品有限公司')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))
```

    word 永和		 start: 0 		 end:2
    word 服装		 start: 2 		 end:4
    word 饰品		 start: 4 		 end:6
    word 有限公司		 start: 6 		 end:10
    


```python
print('-'*40)
print(' 搜索模式')
print('-'*40)
```

    ----------------------------------------
     搜索模式
    ----------------------------------------
    


```python
result = jieba.tokenize('永和服装饰品有限公司', mode='search')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))
```

    word 永和		 start: 0 		 end:2
    word 服装		 start: 2 		 end:4
    word 饰品		 start: 4 		 end:6
    word 有限		 start: 6 		 end:8
    word 公司		 start: 8 		 end:10
    word 有限公司		 start: 6 		 end:10
    

#### demo.py总结

jieba的主要功能有：
    * 1、分词：jieba.cut
        * 1.1 cut的两种模式：cut_all=True or False（默认）
        * 1.2 cut_for_search
        * 1.3 是否使用HMM算法
        * 1.4 加载自定义词典或者通过设置词频，指导分词；需要关闭HMM
    * 2、关键词提取
        * 2.1 TFIDF方法
        * 2.2 TextRank方法
    * 3、分词显示词序
        * Tokenizer
    * 4、词性标注 posseg

## 2、jieba-master源码分析

jieba全部模块见下图

![jupyter](././图片/源码jieba-master.png)

### 2.1、分词模块分析

#### 2.1.1、DAG分词：jieba.\__init\__

##### 2.1.1.1、类  class Tokenizer

##### （1）功能简介：
* 1、基于Trie树结构实现高效的词图扫描，生成句子中汉字所有可能成词情况所构成的有向无环图（DAG)
* 2、采用了动态规划查找最大概率路径, 找出基于词频的最大切分组合
* 3、对于未登录词，采用了基于汉字成词能力的HMM模型，使用了Viterbi算法

##### （2）包含方法如下：

1、 \__init\__(self, dictionary=DEFAULT_DICT):

2、\__repr\__(self): 返回字典大小

3、gen_pfdict(self, f):

4、initialize(self, dictionary=None):

5、check_initialized(self):

6、calc(self, sentence, DAG, route):

7、get_DAG(self, sentence):

8、_cut_all(self, sentence):

9、_cut_DAG_NO_HMM(self, sentence): #关键

10、_cut_DAG(self, sentence):  #关键

11、cut(self, sentence, cut_all=False, HMM=True):

12、cut_for_search(self, sentence, HMM=True):

13、lcut(self, *args, \*\*kwargs):

14、lcut_for_search(self, *args, **kwargs):

15、_lcut_no_hmm(self, sentence): #关键

16、_lcut_all(self, sentence): #关键

17、_lcut_for_search_no_hmm(self, sentence):

18、get_dict_file(self):

19、load_userdict(self, f):

20、add_word(self, word, freq=None, tag=None):
加一个词到词典:
可以省略freq和tag, freq默认为计算值这就保证了这个词可以被删掉。
加到FRWQ字典中
将词拆成字，如果该字不在FREQ中，逐个加入FREQ中，频率设为0
如果freq设置为0，则将

21、del_word(self, word):

22、suggest_freq(self, segment, tune=False):

23、tokenize(self, unicode_sentence, mode="default", HMM=True):
    * Tokenize a sentence and yields tuples of (word, start, end)
24、set_dictionary(self, dictionary_path):


##### (3) 分词剖析

jieba分词流程图如下：

![jupyter](https://img-blog.csdn.net/20180721150943819?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE3MzM2NTU5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

结巴分词从流程图中可看到分为两部分，一个是登录词的分词，另一个是未登录词的分词；

登录词分词，从流程图中可看到，是通过建立DAG词图和计算全局概率Route分词的。

    def cut(self, sentence, cut_all=False, HMM=True):
        '''
        The main function that segments an entire sentence that contains
        Chinese characters into separated words.

        Parameter:
            - sentence: The str(unicode) to be segmented.
            - cut_all: Model type. True for full pattern, False for accurate pattern.
            - HMM: Whether to use the Hidden Markov Model.
            
        给定待分词的句子, 使用正则(re_han)获取匹配的中文字符(和英文字符)切分成的短语列表；
        根据cut_block指定具体的方法(__cut_all,__cut_DAG,__cut_DAG_NO_HMM)对每个短语使用DAG进行分词
        
        如cut_block=__cut_DAG时则使用DAG(查字典)和动态规划, 得到最大概率路径, 对DAG中那些没有在字典中查到的字, 
        组合成一个新的片段短语, 使用HMM模型进行分词, 也就是作者说的识别新词, 即识别字典外的新词；
        '''
        sentence = strdecode(sentence)

        if cut_all:
            re_han = re_han_cut_all #中文正则
            re_skip = re_skip_cut_all#正则
        else:
            re_han = re_han_default  #汉字正则
            re_skip = re_skip_default  #正则
        if cut_all:
            cut_block = self.__cut_all 
        elif HMM:
            cut_block = self.__cut_DAG #不是cut_all，如果HMM=True，则采用DAG+HMM分词，否则采用__cut_DAG_NO_HMM
        else:
            cut_block = self.__cut_DAG_NO_HMM
        blocks = re_han.split(sentence) #正则分块：用标点符号分块？
        for blk in blocks:
            if not blk:
                continue
            if re_han.match(blk): #如果该正则匹配上了，则采用cut_block，
                for word in cut_block(blk): #
                    yield word
            else:
                tmp = re_skip.split(blk)
                for x in tmp:
                    if re_skip.match(x):
                        yield x
                    elif not cut_all:
                        for xx in x:
                            yield xx
                    else:
                        yield x



重要方法def __cut_DAG(self, sentence) #cut_block

    def __cut_DAG(self, sentence):
        '''
        使用DAG(查字典)和动态规划, 得到最大概率路径, 对DAG中那些没有在字典中查到的字, 
        组合成一个新的片段短语, 使用HMM模型进行分词, 也就是作者说的识别新词, 即识别字典外的新词；
        '''
        
        DAG = self.get_DAG(sentence)
        route = {}
        self.calc(sentence, DAG, route)  #更新route：基于DAG计算最大分词概率路径
        x = 0
        buf = ''
        N = len(sentence)
        while x < N:
            y = route[x][1] + 1
            l_word = sentence[x:y]
            if y - x == 1: #词为一个字
                buf += l_word
            else:  #词大于一个字
                if buf:
                    if len(buf) == 1:
                        yield buf
                        buf = ''
                    else:
                        if not self.FREQ.get(buf): #未登录分块
                            recognized = finalseg.cut(buf) #调HMM分词（viterbi算法，求最大路径）
                            for t in recognized:
                                yield t
                        else:
                            for elem in buf:
                                yield elem
                        buf = ''
                yield l_word
            x = y

        if buf:
            if len(buf) == 1:
                yield buf
            elif not self.FREQ.get(buf): #
                recognized = finalseg.cut(buf)
                for t in recognized:
                    yield t
            else:
                for elem in buf:
                    yield elem

#### __cut_DAG(self, sentence)方法其中的规则比较难懂，拆箱查看！


```python
import json
from jieba import finalseg
sentence = 'I love你，不以为耻，反以为rong, 如来，你是哪棵cong，快要刮大风风火火，blog, 卫斯理'
DAG = tokenizer.get_DAG(sentence)
print("DAG:\n", DAG)
route = {}
tokenizer.calc(sentence, DAG, route)  #更新route：基于DAG计算最大分词概率路径
print("route:\n", json.dumps(route, indent=2))
x = 0
buf = ''
N = len(sentence)
while x < N:
    y = route[x][1] + 1 #最大路径结点
    l_word = sentence[x:y]
    print('(x, y-1, l_word):',(x, y-1, l_word))
    if y - x == 1: #单字词
        buf += l_word #将挨着的单字词链接
        print('buf += l_word:',buf)
    else:  #出现多字词
        if buf: #多字词的上一组单字词链接缓存
            if len(buf) == 1: #如果缓存长度为1
                #yield buf
                print('if len(buf) == 1:',buf) #不用HMM分词，直接输出
                buf = ''
            else: #如果缓存长度大于1
                if not tokenizer.FREQ.get(buf): #如果该缓存未登录 
                    recognized = finalseg.cut(buf) #调HMM对缓存分词（viterbi算法，求最大路径）
                    for t in recognized:
                        #yield t
                        print('for t in recognized:', t)
                else: #如果缓存登录了
                    for elem in buf: #这个比较奇怪
                        #yield elem
                        print('for elem in buf', elem)
                buf = ''
        #yield l_word
        print('yield l_word:', l_word)
    x = y

if buf:#遍历完，最后没有出现多字词，对剩余的缓存进行切分
    if len(buf) == 1:
        #yield buf
        print('buf:',buf)
    elif not tokenizer.FREQ.get(buf): #
        recognized = finalseg.cut(buf)
        for t in recognized:
            #yield t
            print('t:', t)
    else:
        for elem in buf:
            #yield elem
            print('elem:', elem)
```

    DAG:
     {0: [0], 1: [1], 2: [2], 3: [3], 4: [4], 5: [5], 6: [6], 7: [7], 8: [8, 9, 11], 9: [9, 10], 10: [10], 11: [11], 12: [12], 13: [13], 14: [14, 15], 15: [15], 16: [16], 17: [17], 18: [18], 19: [19], 20: [20], 21: [21], 22: [22, 23], 23: [23], 24: [24], 25: [25], 26: [26], 27: [27], 28: [28], 29: [29], 30: [30], 31: [31], 32: [32], 33: [33], 34: [34, 35], 35: [35], 36: [36], 37: [37, 38], 38: [38, 39, 41], 39: [39, 40], 40: [40], 41: [41], 42: [42], 43: [43], 44: [44], 45: [45], 46: [46], 47: [47], 48: [48], 49: [49, 51], 50: [50], 51: [51]}
    route:
     {
      "52": [
        0,
        0
      ],
      "51": [
        -9.073726763747516,
        51
      ],
      "50": [
        -18.661671449159165,
        50
      ],
      "49": [
        -15.27249579813996,
        51
      ],
      "48": [
        -33.18404892589518,
        48
      ],
      "47": [
        -51.0956020536504,
        47
      ],
      "46": [
        -69.00715518140562,
        46
      ],
      "45": [
        -86.91870830916085,
        45
      ],
      "44": [
        -104.83026143691606,
        44
      ],
      "43": [
        -122.74181456467127,
        43
      ],
      "42": [
        -140.65336769242649,
        42
      ],
      "41": [
        -149.51498396969853,
        41
      ],
      "40": [
        -158.37660024697058,
        40
      ],
      "39": [
        -163.9925498929686,
        40
      ],
      "38": [
        -154.31642557813234,
        41
      ],
      "37": [
        -160.3497228635493,
        37
      ],
      "36": [
        -171.07816428956122,
        36
      ],
      "35": [
        -177.02838869036324,
        35
      ],
      "34": [
        -182.59780030392383,
        35
      ],
      "33": [
        -200.50935343167905,
        33
      ],
      "32": [
        -218.42090655943426,
        32
      ],
      "31": [
        -236.33245968718947,
        31
      ],
      "30": [
        -254.24401281494468,
        30
      ],
      "29": [
        -272.1555659426999,
        29
      ],
      "28": [
        -283.35052429693417,
        28
      ],
      "27": [
        -291.8579811182936,
        27
      ],
      "26": [
        -296.18093558068654,
        26
      ],
      "25": [
        -301.7269069082454,
        25
      ],
      "24": [
        -319.6384600360006,
        24
      ],
      "23": [
        -325.5577465501797,
        23
      ],
      "22": [
        -332.0009370788606,
        23
      ],
      "21": [
        -349.9124902066158,
        21
      ],
      "20": [
        -367.824043334371,
        20
      ],
      "19": [
        -385.73559646212624,
        19
      ],
      "18": [
        -403.64714958988145,
        18
      ],
      "17": [
        -421.55870271763666,
        17
      ],
      "16": [
        -439.4702558453919,
        16
      ],
      "15": [
        -444.78385641515274,
        15
      ],
      "14": [
        -448.66036966752114,
        15
      ],
      "13": [
        -457.0614778308498,
        13
      ],
      "12": [
        -474.973030958605,
        12
      ],
      "11": [
        -487.1976087300204,
        11
      ],
      "10": [
        -492.5112092997813,
        10
      ],
      "9": [
        -496.3877225521497,
        10
      ],
      "8": [
        -489.4188481835605,
        11
      ],
      "7": [
        -507.3304013113157,
        7
      ],
      "6": [
        -512.8763726388745,
        6
      ],
      "5": [
        -530.7879257666298,
        5
      ],
      "4": [
        -548.699478894385,
        4
      ],
      "3": [
        -566.6110320221403,
        3
      ],
      "2": [
        -584.5225851498956,
        2
      ],
      "1": [
        -602.4341382776508,
        1
      ],
      "0": [
        -620.3456914054061,
        0
      ]
    }
    (x, y-1, l_word): (0, 0, 'I')
    buf += l_word: I
    (x, y-1, l_word): (1, 1, ' ')
    buf += l_word: I 
    (x, y-1, l_word): (2, 2, 'l')
    buf += l_word: I l
    (x, y-1, l_word): (3, 3, 'o')
    buf += l_word: I lo
    (x, y-1, l_word): (4, 4, 'v')
    buf += l_word: I lov
    (x, y-1, l_word): (5, 5, 'e')
    buf += l_word: I love
    (x, y-1, l_word): (6, 6, '你')
    buf += l_word: I love你
    (x, y-1, l_word): (7, 7, '，')
    buf += l_word: I love你，
    (x, y-1, l_word): (8, 11, '不以为耻')
    for t in recognized: I
    for t in recognized:  
    for t in recognized: love
    for t in recognized: 你
    for t in recognized: ，
    yield l_word: 不以为耻
    (x, y-1, l_word): (12, 12, '，')
    buf += l_word: ，
    (x, y-1, l_word): (13, 13, '反')
    buf += l_word: ，反
    (x, y-1, l_word): (14, 15, '以为')
    for t in recognized: ，
    for t in recognized: 反
    yield l_word: 以为
    (x, y-1, l_word): (16, 16, 'r')
    buf += l_word: r
    (x, y-1, l_word): (17, 17, 'o')
    buf += l_word: ro
    (x, y-1, l_word): (18, 18, 'n')
    buf += l_word: ron
    (x, y-1, l_word): (19, 19, 'g')
    buf += l_word: rong
    (x, y-1, l_word): (20, 20, ',')
    buf += l_word: rong,
    (x, y-1, l_word): (21, 21, ' ')
    buf += l_word: rong, 
    (x, y-1, l_word): (22, 23, '如来')
    for t in recognized: rong
    for t in recognized: , 
    yield l_word: 如来
    (x, y-1, l_word): (24, 24, '，')
    buf += l_word: ，
    (x, y-1, l_word): (25, 25, '你')
    buf += l_word: ，你
    (x, y-1, l_word): (26, 26, '是')
    buf += l_word: ，你是
    (x, y-1, l_word): (27, 27, '哪')
    buf += l_word: ，你是哪
    (x, y-1, l_word): (28, 28, '棵')
    buf += l_word: ，你是哪棵
    (x, y-1, l_word): (29, 29, 'c')
    buf += l_word: ，你是哪棵c
    (x, y-1, l_word): (30, 30, 'o')
    buf += l_word: ，你是哪棵co
    (x, y-1, l_word): (31, 31, 'n')
    buf += l_word: ，你是哪棵con
    (x, y-1, l_word): (32, 32, 'g')
    buf += l_word: ，你是哪棵cong
    (x, y-1, l_word): (33, 33, '，')
    buf += l_word: ，你是哪棵cong，
    (x, y-1, l_word): (34, 35, '快要')
    for t in recognized: ，
    for t in recognized: 你
    for t in recognized: 是
    for t in recognized: 哪棵
    for t in recognized: cong
    for t in recognized: ，
    yield l_word: 快要
    (x, y-1, l_word): (36, 36, '刮')
    buf += l_word: 刮
    (x, y-1, l_word): (37, 37, '大')
    buf += l_word: 刮大
    (x, y-1, l_word): (38, 41, '风风火火')
    for t in recognized: 刮大
    yield l_word: 风风火火
    (x, y-1, l_word): (42, 42, '，')
    buf += l_word: ，
    (x, y-1, l_word): (43, 43, 'b')
    buf += l_word: ，b
    (x, y-1, l_word): (44, 44, 'l')
    buf += l_word: ，bl
    (x, y-1, l_word): (45, 45, 'o')
    buf += l_word: ，blo
    (x, y-1, l_word): (46, 46, 'g')
    buf += l_word: ，blog
    (x, y-1, l_word): (47, 47, ',')
    buf += l_word: ，blog,
    (x, y-1, l_word): (48, 48, ' ')
    buf += l_word: ，blog, 
    (x, y-1, l_word): (49, 51, '卫斯理')
    for t in recognized: ，
    for t in recognized: blog
    for t in recognized: , 
    yield l_word: 卫斯理
    

    def get_DAG(self, sentence):
        '''
        首先检测(check_initialized)进程是否已经加载词库，若未初始化词库则调用initialize函数进行初始化，
        initialize中判断有无已经缓存的前缀词典cache_file文件，若有相应的cache文件则直接使用 marshal.load 
        方法加载前缀词典，若无则通过gen_pfdict对指定的词库dict.txt进行计算生成前缀词典，到jieba进程的初始
        化工作完成后就调用get_DAG获得句子的DAG。
        '''
        self.check_initialized()
        DAG = {}    #DAG空字典，用来构建DAG有向无环图
        N = len(sentence) #赋值N词的长度
        for k in xrange(N): #创建N词长度的列表，进行遍历
            tmplist = []  #从字开始能在FREQ中的匹配到的词末尾位置所在的list
            i = k
            frag = sentence[k] #取传入词中的值，例如k=0,frag=我
            while i < N and frag in self.FREQ: # 当传入的词，在FREQ中时，就给tmplist赋值，构建字开始可能去往的所有的路径列表
                if self.FREQ[frag]: #每个词，在FREQ中查找，查到，则将下标传入templist中
                    tmplist.append(i)   #添加词语所在位置
                i += 1      #查找我，后继续查找“我们”是否也在语料库中，直到查不到推出循环
                frag = sentence[k:i + 1]  #截取传入值得词语，i=1,时截取 我，i=2时截取我们
            if not tmplist:  #当传入值，在语料库中查询不到时，
                tmplist.append(k) #新字
            DAG[k] = tmplist  #赋值DAG 词典
        return DAG

#### 函数calc(self, sentence, DAG, route)功能：动态规划查找最大概率路径, 计算全局概率Route

* 语句 xrange(N - 1, -1, -1)是从句子的末尾开始计算，
* max函数返回的是一个元组，计算方法是log(freq/total)+后一个字得到的最大概率路径的概率。即为动态规划查找最大概率路径。注意动态规划是从后往前。

* 动态规划查找最大概率路径
    
    def calc(self, sentence, DAG, route):
        N = len(sentence)
        route[N] = (0, 0) 
        # route[N]:最大路径的值,(0,0):当前这个词的末尾坐标
        
        # total 为dict.txt词表中，总词数（或总词频），共60101967 个词语（含重复）
        # 对概率值取对数:概率相乘变成对数相加,防止相乘造成下溢
        logtotal = log(self.total)
        
        # 从后往前遍历句子 反向计算最大概率路径
        for idx in xrange(N - 1, -1, -1):
        
            # 列表推倒求最大概率对数路径
            # route[idx] = max([ (概率对数，词语末字位置) for x in DAG[idx] ])
            # 以idx:(概率对数最大值，词语末字位置)键值对形式保存在route中
            # route[x+1][0] 表示 词路径[x+1,N-1]的最大概率对数,
            # [x+1][0]即表示取句子x+1位置对应元组(概率对数，词语末字位置)的概率对数
            route[idx] = max((log(self.FREQ.get(sentence[idx:x + 1]) or 1) -
                              logtotal + route[x + 1][0], x) for x in DAG[idx])
                    
            #当前位置idx到x路径概率大小表示：log(freq/total)          
            #当前位置idx到x的概率 + 词路径[x+1,N-1]的最大概率对数，两者之和取最大：max(log(freq/total) + route[x + 1][0],x)


```python
max([(-10,1),(-11,2)])
```




    (-10, 1)



###  2.1.2 新词发现 jieba.finalseg.\__init__

中文分词的难点

分词规范，词的定义还不明确 (《统计自然语言处理》宗成庆)

歧义切分问题，交集型切分问题，多义组合型切分歧义等

    结婚的和尚未结婚的 =>
    结婚／的／和／尚未／结婚／的
    结婚／的／和尚／未／结婚／的
    未登录词问题

有两种解释：一是已有的词表中没有收录的词，二是已有的训练语料中未曾出现过的词，第二种含义中未登录词又称OOV(Out of Vocabulary)。对于大规模

真实文本来说，未登录词对于分词的精度的影响远超歧义切分。一些网络新词，自造词一般都属于这些词。

因此可以看到，未登录词是分词中的一个重要问题，jieba分词中对于OOV的解决方法是：
#### 采用了基于汉字成词能力的 HMM 模型，使用了 Viterbi 算法。

参考：https://blog.csdn.net/daniel_ustc/article/details/48248393

#### 函数  finalseg.cut(sentence) 切分未登录词
    def cut(sentence):
        sentence = strdecode(sentence)
        blocks = re_han.split(sentence)
        for blk in blocks:
            if re_han.match(blk):
                for word in __cut(blk):  #采用HMM切分未登录词
                    if word not in Force_Split_Words:
                        yield word
                    else:
                        for c in word:
                            yield c
            else:
                tmp = re_skip.split(blk)
                for x in tmp:
                    if x:
                        yield x
    def __cut(sentence):
        global emit_P
        prob, pos_list = viterbi(sentence, 'BMES', start_P, trans_P, emit_P) #维特比算法
        #初始状态矩阵，状态转移矩阵，发射矩阵，可能状态BMES
        
        begin, nexti = 0, 0
        # print pos_list, sentence
        for i, char in enumerate(sentence):
            pos = pos_list[i]
            if pos == 'B':
                begin = i
            elif pos == 'E':
                yield sentence[begin:i + 1] #
                nexti = i + 1
            elif pos == 'S':
                yield char
                nexti = i + 1
        if nexti < len(sentence):
            yield sentence[nexti:]

![jupyter](https://img-blog.csdn.net/20171204192545422)

![jupyter](https://img-blog.csdn.net/20171204192653714)
![jupyter](https://img-blog.csdn.net/20171204192754364)
![jupyter](https://img-blog.csdn.net/20180925105839852?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE2MjM0NjEz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

维特比算法的基础可以概括为下面三点（来源于吴军：数学之美）： 

1、如果概率最大的路径经过篱笆网络的某点，则从开始点到该点的子路径也一定是从开始到该点路径中概率最大的。 

2、假定第i时刻有k个状态，从开始到i时刻的k个状态有k条最短路径，而最终的最短路径必然经过其中的一条。 

3、根据上述性质，在计算第i+1状态的最短路径时，只需要考虑从开始到当前的k个状态值的最短路径和当前状态值到第i+1状态值的最短路径即可，如求t=3时的最短路径，等于求t=2时的所有状态结点x2i的最短路径加上t=2到t=3的各节点的最短路径。

参考：https://blog.csdn.net/hudashi/article/details/87875259

    参考：
    https://blog.csdn.net/sinat_26811377/article/details/100693627?utm_medium=distribute.pc_relevant.none-task-blog-baidujs-1
    https://blog.csdn.net/hudashi/article/details/87875259
    def viterbi(obs, states, start_p, trans_p, emit_p):
        V = [{}]  # tabular
        path = {}
        # 时刻t = 0，初始状态
        for y in states:  
            #在0时刻各种可能状态的概率 log(P(y)) + log(P(obs[0]|y))
            V[0][y] = start_p[y] + emit_p[y].get(obs[0], MIN_FLOAT)
            path[y] = [y]
        # 时刻t = 1,...,len(obs) - 1
        for t in xrange(1, len(obs)):
            V.append({})
            newpath = {}
            # 当前时刻所处的各种可能的状态
            for y in states:
                # 获取t时刻各种可能的发射概率
                em_p = emit_p[y].get(obs[t], MIN_FLOAT)
                # log(P())
                # 其中，PrevStatus[y]是当前时刻的状态所对应上一时刻可能的状态
                (prob, state) = max(
                    [(V[t - 1][y0] + trans_p[y0].get(y, MIN_FLOAT) + em_p, y0) for y0 in PrevStatus[y]])
                V[t][y] = prob
                # 将上一时刻最优的状态 + 这一时刻的状态
                newpath[y] = path[state] + [y]
            path = newpath

        # 最后一个时刻
        (prob, state) = max((V[len(obs) - 1][y], y) for y in 'ES')

        # 返回最大概率对数和最优路径
        return (prob, path[state])


    
    PrevStatus = {
    'B': 'ES',
    'M': 'MB',
    'S': 'SE',
    'E': 'BM'
    }

### 2.1.3 Tokenizer类运行分析


```python
from jieba import Tokenizer
tokenizer = Tokenizer()
tokenizer, tokenizer.__dict__
```




    (<Tokenizer dictionary=None>,
     {'lock': <unlocked _thread.RLock object owner=0 count=0 at 0x0000021703499240>,
      'dictionary': None,
      'FREQ': {},
      'total': 0,
      'user_word_tag_tab': {},
      'initialized': False,
      'tmp_dir': None,
      'cache_file': None})



tokenizer初始化


```python
#tokenizer.initialize() 加载用时分析
import timeit
fun = tokenizer.initialize  
timeit.timeit(stmt=fun,number=1)
```

    Building prefix dict from the default dictionary ...
    Dumping model to file cache C:\Users\86185\AppData\Local\Temp\jieba.cache
    Loading model cost 0.985 seconds.
    Prefix dict has been built successfully.
    




    1.0771776999899885




```python
tokenizer.__dict__
```




    {'lock': <unlocked _thread.RLock object owner=0 count=0 at 0x000002177229DD80>,
     'dictionary': None,
     'FREQ': {'AT&T': 3,
      'A': 0,
      'AT': 0,
      'AT&': 0,
      'B超': 3,
      'B': 0,
      'c#': 3,
      'c': 0,
      'C#': 3,
      'C': 0,
      'c++': 3,
      'c+': 0,
      'C++': 3,
      'C+': 0,
      'T恤': 4,
      'T': 0,
      'A座': 3,
      'A股': 3,
      'A型': 3,
      'A轮': 3,
      'AA制': 3,
      'AA': 0,
      'AB型': 3,
      'AB': 0,
      'B座': 3,
      'B股': 3,
      'B型': 3,
      'B轮': 3,
      'BB机': 3,
      'BB': 0,
      'BP机': 3,
      'BP': 0,
      'C盘': 3,
      'C座': 3,
      'C语言': 3,
      'C语': 0,
      'CD盒': 3,
      'CD': 0,
      'CD机': 3,
      'CALL机': 3,
      'CA': 0,
      'CAL': 0,
      'CALL': 0,
      'D盘': 3,
      'D': 0,
      'D座': 3,
      'D版': 3,
      'E盘': 3,
      'E': 0,
      'E座': 3,
      'E化': 3,
      'E通': 3,
      'F盘': 3,
      'F': 0,
      'F座': 3,
      'G盘': 3,
      'G': 0,
      'H盘': 3,
      'H': 0,
      'H股': 3,
      'I盘': 3,
      'I': 0,
      'IC卡': 3,
      'IC': 0,
      'IP卡': 3,
      'IP': 0,
      'IP电话': 3,
      'IP电': 0,
      'IP地址': 3,
      'IP地': 0,
      'K党': 3,
      'K': 0,
      'K歌之王': 3,
      'K歌': 0,
      'K歌之': 0,
      'N年': 3,
      'N': 0,
      'O型': 3,
      'O': 0,
      'PC机': 3,
      'P': 0,
      'PC': 0,
      'PH值': 3,
      'PH': 0,
      'SIM卡': 3,
      'S': 0,
      'SI': 0,
      'SIM': 0,
      'U盘': 3,
      'U': 0,
      'VISA卡': 3,
      'V': 0,
      'VI': 0,
      'VIS': 0,
      'VISA': 0,
      'Z盘': 3,
      'Z': 0,
      'Q版': 3,
      'Q': 0,
      'QQ号': 3,
      'QQ': 0,
      'RSS订阅': 3,
      'R': 0,
      'RS': 0,
      'RSS': 0,
      'RSS订': 0,
      'T盘': 3,
      'X光': 3,
      'X': 0,
      'X光线': 3,
      'X射线': 3,
      'X射': 0,
      'γ射线': 3,
      'γ': 0,
      'γ射': 0,
      'T恤衫': 3,
      'T型台': 3,
      'T型': 0,
      'T台': 3,
      '4S店': 3,
      '4': 0,
      '4S': 0,
      '4s店': 3,
      '4s': 0,
      '江南style': 3,
      '江': 6083,
      '江南': 4986,
      '江南s': 0,
      '江南st': 0,
      '江南sty': 0,
      '江南styl': 0,
      '江南Style': 3,
      '江南S': 0,
      '江南St': 0,
      '江南Sty': 0,
      '江南Styl': 0,
      '1号店': 3,
      '1': 0,
      '1号': 0,
      '小S': 3,
      '小': 57969,
      '大S': 3,
      '大': 144099,
      '阿Q': 3,
      '阿': 6905,
      '一': 217830,
      '一一': 1670,
      '一一二': 11,
      '一一例': 3,
      '一一分': 8,
      '一一列举': 34,
      '一一列': 0,
      '一一对': 9,
      '一一对应': 43,
      '一一记': 2,
      '一一道来': 4,
      '一一道': 0,
      '一丁': 18,
      '一丁不识': 3,
      '一丁不': 0,
      '一丁点': 3,
      '一丁点儿': 24,
      '一七': 22,
      '一七八不': 3,
      '一七八': 0,
      '一万': 442,
      '一万一千': 4,
      '一万一': 0,
      '一万一千五百二十颗': 2,
      '一万一千五': 0,
      '一万一千五百': 0,
      '一万一千五百二': 0,
      '一万一千五百二十': 0,
      '一万一千八百八十斤': 2,
      '一万一千八': 0,
      '一万一千八百': 0,
      '一万一千八百八': 0,
      '一万一千八百八十': 0,
      '一万一千多间': 2,
      '一万一千多': 0,
      '一万一千零九十五册': 4,
      '一万一千零': 0,
      '一万一千零九': 0,
      '一万一千零九十': 0,
      '一万一千零九十五': 0,
      '一万七千': 5,
      '一万七': 0,
      '一万七千余': 2,
      '一万七千多': 2,
      '一万七千多户': 2,
      '一万万': 4,
      '一万万两': 4,
      '一万三千': 8,
      '一万三': 0,
      '一万三千五百一十七': 2,
      '一万三千五': 0,
      '一万三千五百': 0,
      '一万三千五百一': 0,
      '一万三千五百一十': 0,
      '一万三千五百斤': 4,
      '一万三千余种': 2,
      '一万三千余': 0,
      '一万三千块': 2,
      '一万两': 124,
      '一万两万': 4,
      '一万两千': 3,
      '一万个': 62,
      '一万九千': 2,
      '一万九': 0,
      '一万九千余': 2,
      '一万二': 10,
      '一万二千': 7,
      '一万二千两': 2,
      '一万二千五百': 4,
      '一万二千五': 0,
      '一万二千五百一十二': 2,
      '一万二千五百一': 0,
      '一万二千五百一十': 0,
      '一万二千五百余': 2,
      '一万二千五百余吨': 2,
      '一万二千亩': 2,
      '一万二千余': 2,
      '一万二千六百八十二箱': 2,
      '一万二千六': 0,
      '一万二千六百': 0,
      '一万二千六百八': 0,
      '一万二千六百八十': 0,
      '一万二千六百八十二': 0,
      '一万二千名': 3,
      '一万二千里': 3,
      '一万五': 6,
      '一万五千': 45,
      '一万五千一百四十四卷': 2,
      '一万五千一': 0,
      '一万五千一百': 0,
      '一万五千一百四': 0,
      '一万五千一百四十': 0,
      '一万五千一百四十四': 0,
      '一万五千两': 4,
      '一万五千个': 2,
      '一万五千二百余': 2,
      '一万五千二': 0,
      '一万五千二百': 0,
      '一万五千余': 9,
      '一万五千元': 3,
      '一万五千名': 4,
      '一万五千多': 2,
      '一万五千家': 2,
      '一万亿': 3,
      '一万亿美元': 5,
      '一万亿美': 0,
      '一万余': 41,
      '一万余吨': 2,
      '一万余顷': 2,
      '一万倍': 14,
      '一万元': 61,
      '一万八': 5,
      '一万八千': 7,
      '一万八千余': 8,
      '一万八千多元': 2,
      '一万八千多': 0,
      '一万公里': 2,
      '一万公': 0,
      '一万六千': 5,
      '一万六': 0,
      '一万六千三百户': 2,
      '一万六千三': 0,
      '一万六千三百': 0,
      '一万六千余户': 2,
      '一万六千余': 0,
      '一万六千多': 3,
      '一万册': 2,
      '一万刀': 7,
      '一万匹': 4,
      '一万卷': 2,
      '一万双': 6,
      '一万发': 2,
      '一万句': 11,
      '一万只': 9,
      '一万名': 16,
      '一万四千': 3,
      '一万四': 0,
      '一万四千二百四十三户': 2,
      '一万四千二': 0,
      '一万四千二百': 0,
      '一万四千二百四': 0,
      '一万四千二百四十': 0,
      '一万四千二百四十三': 0,
      '一万四千余顷': 2,
      '一万四千余': 0,
      '一万四千多元': 3,
      '一万四千多': 0,
      '一万回': 2,
      '一万块': 49,
      '一万声': 2,
      '一万多': 86,
      '一万多一点': 2,
      '一万多一': 0,
      '一万多两': 9,
      '一万多个': 10,
      '一万多例': 2,
      '一万多元': 10,
      '一万多只': 2,
      '一万多名': 26,
      '一万多块': 6,
      '一万多平方公里': 2,
      '一万多平': 0,
      '一万多平方': 0,
      '一万多平方公': 0,
      '一万多年': 4,
      '一万多斤': 3,
      '一万多顷': 2,
      '一万天': 2,
      '一万头': 2,
      '一万宗': 2,
      '一万家': 8,
      '一万左右': 3,
      '一万左': 0,
      '一万年': 39,
      '一万张': 3,
      '一万户': 5,
      '一万斤': 9,
      '一万条': 4,
      '一万次': 16,
      '一万步': 30,
      '一万盏': 4,
      '一万种': 2,
      '一万贯': 4,
      '一万遍': 9,
      '一万里': 4,
      '一万间': 5,
      '一万零五百亿斤': 2,
      '一万零': 0,
      '一万零五': 0,
      '一万零五百': 0,
      '一万零五百亿': 0,
      '一丈': 298,
      '一三': 19,
      '一三五': 6,
      '一三六八': 2,
      '一三六': 0,
      '一三四团': 3,
      '一三四': 0,
      '一上': 3,
      '一上午': 53,
      '一上台': 3,
      '一上场': 3,
      '一下': 13924,
      '一下一下': 22,
      '一下一': 0,
      '一下下': 37,
      '一下二十': 2,
      '一下二': 0,
      '一下余': 2,
      '一下全部': 3,
      '一下全': 0,
      '一下十三': 2,
      '一下十': 0,
      '一下半': 3,
      '一下周': 3,
      '一下四周': 6,
      '一下四': 0,
      '一下圈': 2,
      '一下场': 3,
      '一下头': 54,
      '一下子': 2333,
      '一下子全部': 3,
      '一下子全': 0,
      '一下子发': 2,
      '一下子多出': 2,
      '一下子多': 0,
      '一下子成': 16,
      '一下子打': 10,
      '一下子把': 61,
      '一下子站': 15,
      '一下子脸': 3,
      '一下床': 6,
      '一下张': 8,
      '一下手': 17,
      '一下眼': 10,
      '一下站': 25,
      '一下肚子': 2,
      '一下肚': 0,
      '一下脸': 10,
      '一下页': 2,
      '一下顶': 5,
      '一下顿': 2,
      '一下首': 2,
      '一不做': 87,
      '一不': 0,
      '一不压众': 3,
      '一不压': 0,
      '一不小心': 125,
      '一不小': 0,
      '一不怕苦': 10,
      '一不怕': 0,
      '一不扭众': 3,
      '一不扭': 0,
      '一不注意': 3,
      '一不注': 0,
      '一不留神': 3,
      '一不留': 0,
      '一专多能': 27,
      '一专': 0,
      '一专多': 0,
      '一世': 770,
      '一世之雄': 2,
      '一世之': 0,
      '一世英名': 3,
      '一世英': 0,
      '一世龙门': 3,
      '一世龙': 0,
      '一丘一壑': 3,
      '一丘': 0,
      '一丘一': 0,
      '一丘之貉': 12,
      '一丘之': 0,
      '一业': 37,
      '一业为主': 3,
      '一业为': 0,
      '一丛丛': 31,
      '一丛': 0,
      '一丝': 1186,
      '一丝一毫': 67,
      '一丝一': 0,
      '一丝不挂': 60,
      '一丝不': 0,
      '一丝不紊': 3,
      '一丝不苟': 112,
      '一丝丝': 58,
      '一丝两气': 3,
      '一丝两': 0,
      '一丝半粟': 3,
      '一丝半': 0,
      '一两': 382,
      '一两一': 2,
      '一两一两': 2,
      '一两万': 40,
      '一两万元': 6,
      '一两万块': 4,
      '一两万美元': 2,
      '一两万美': 0,
      '一两丈': 5,
      '一两下': 7,
      '一两个': 424,
      '一两九十元': 2,
      '一两九': 0,
      '一两九十': 0,
      '一两二两': 3,
      '一两二': 0,
      '一两五': 4,
      '一两件': 39,
      '一两倍': 4,
      '一两八': 5,
      '一两分': 7,
      '一两分钟': 17,
      '一两千': 38,
      '一两千元': 3,
      '一两千块': 2,
      '一两千平方米': 2,
      '一两千平': 0,
      '一两千平方': 0,
      '一两千架': 2,
      '一两半两': 2,
      '一两半': 0,
      '一两发': 2,
      '一两口': 7,
      '一两句': 68,
      '一两句话': 3,
      '一两只': 21,
      '一两叶': 2,
      '一两名': 8,
      '一两周': 4,
      '一两回': 8,
      '一两场': 10,
      '一两块': 4,
      '一两声': 24,
      '一两处': 14,
      '一两多': 5,
      '一两天': 169,
      '一两套': 7,
      '一两家': 13,
      '一两寸': 3,
      '一两尺': 2,
      '一两岁': 17,
      '一两年': 164,
      '一两张': 8,
      '一两成': 2,
      '一两手': 8,
      '一两折': 2,
      '一两招': 12,
      '一两支': 3,
      '一两日': 19,
      '一两月': 7,
      '一两本': 8,
      '一两条': 8,
      '一两杯': 5,
      '一两枚': 8,
      '一两株': 2,
      '一两样': 13,
      '一两根': 4,
      '一两次': 73,
      '一两款': 2,
      '一两步': 5,
      '一两点': 19,
      '一两片': 6,
      '一两百': 7,
      '一两百万': 4,
      '一两百个': 2,
      '一两百元': 5,
      '一两百年': 7,
      '一两碗': 2,
      '一两秒': 3,
      '一两篇': 5,
      '一两米': 6,
      '一两辆': 2,
      '一两遍': 2,
      '一两部': 6,
      '一两里': 3,
      '一两重': 5,
      '一两门': 3,
      '一两间': 4,
      '一两页': 17,
      '一两项': 6,
      '一两颗': 5,
      '一两首': 3,
      '一个': 142747,
      '一个一个把': 2,
      '一个一': 0,
      '一个一个': 0,
      '一个一千多年': 2,
      '一个一千': 0,
      '一个一千多': 0,
      '一个一号': 2,
      '一个一尺': 2,
      '一个一岁': 4,
      '一个一百多年': 2,
      '一个一百': 0,
      '一个一百多': 0,
      '一个一百多斤': 2,
      '一个一米': 3,
      '一个七八': 2,
      '一个七': 0,
      '一个七八岁': 8,
      '一个七十': 2,
      '一个七十岁': 2,
      '一个七品': 4,
      '一个七岁': 2,
      '一个万里': 2,
      '一个万': 0,
      '一个三十': 19,
      '一个三': 0,
      '一个三十余岁': 2,
      '一个三十余': 0,
      '一个三十出头': 3,
      '一个三十出': 0,
      '一个三十多岁': 25,
      '一个三十多': 0,
      '一个三十岁': 6,
      '一个三品': 3,
      '一个三四岁': 3,
      '一个三四': 0,
      '一个三四百': 2,
      '一个三天': 4,
      '一个三层': 4,
      '一个三岁': 7,
      '一个三维': 4,
      '一个三面': 3,
      '一个两万四千元': 2,
      '一个两': 0,
      '一个两万': 0,
      '一个两万四': 0,
      '一个两万四千': 0,
      '一个两万多': 4,
      '一个两岁': 7,
      '一个个': 2055,
      '一个九十度': 2,
      '一个九': 0,
      '一个九十': 0,
      '一个九品': 3,
      '一个九头': 4,
      '一个九岁': 3,
      '一个九曲': 2,
      '一个二两': 2,
      '一个二': 0,
      '一个二元': 7,
      '一个二十': 11,
      '一个二十七八岁': 3,
      '一个二十七': 0,
      '一个二十七八': 0,
      '一个二十三岁': 3,
      '一个二十三': 0,
      '一个二十五六岁': 7,
      '一个二十五': 0,
      '一个二十五六': 0,
      '一个二十五岁': 3,
      '一个二十多岁': 13,
      '一个二十多': 0,
      '一个二十岁': 6,
      '一个二维': 4,
      '一个二重': 3,
      '一个五六岁': 2,
      '一个五': 0,
      '一个五六': 0,
      '一个五十': 11,
      '一个五十两': 2,
      '一个五十余岁': 2,
      '一个五十余': 0,
      '一个五十多岁': 16,
      '一个五十多': 0,
      '一个五十岁': 3,
      '一个五十左右': 2,
      '一个五十左': 0,
      '一个五品': 5,
      '一个五尺': 2,
      '一个五岁': 12,
      '一个五百': 2,
      '一个五袋': 2,
      '一个亿': 24,
      '一个亿万': 4,
      '一个伍': 2,
      '一个八九十岁': 2,
      '一个八': 0,
      '一个八九': 0,
      '一个八九十': 0,
      '一个八九岁': 6,
      '一个八品': 2,
      '一个八岁': 2,
      '一个六七岁': 5,
      '一个六': 0,
      '一个六七': 0,
      '一个六十': 2,
      '一个六十七岁': 2,
      '一个六十七': 0,
      '一个六十多': 2,
      '一个六十多岁': 2,
      '一个六十岁': 2,
      '一个六口': 2,
      '一个六品': 16,
      '一个六尺': 2,
      '一个六层': 2,
      '一个六岁': 6,
      '一个几万': 6,
      '一个几': 0,
      '一个几亿': 17,
      '一个几千万元': 2,
      '一个几千': 0,
      '一个几千万': 0,
      '一个几岁': 3,
      '一个几百万': 5,
      '一个几百': 0,
      '一个劲': 42,
      '一个劲儿': 143,
      '一个劲地': 101,
      '一个包': 26,
      '一个十': 18,
      '一个十一': 4,
      '一个十一二岁': 7,
      '一个十一二': 0,
      '一个十七八岁': 8,
      '一个十七': 0,
      '一个十七八': 0,
      '一个十七岁': 6,
      '一个十七级': 2,
      '一个十三四岁': 11,
      '一个十三': 0,
      '一个十三四': 0,
      '一个十三岁': 4,
      '一个十个': 3,
      '一个十九岁': 3,
      '一个十九': 0,
      '一个十二': 22,
      '一个十二三岁': 9,
      '一个十二三': 0,
      '一个十二岁': 3,
      '一个十五六岁': 9,
      '一个十五': 0,
      '一个十五六': 0,
      '一个十五岁': 8,
      '一个十余丈': 4,
      '一个十余': 0,
      '一个十余岁': 2,
      '一个十八九岁': 7,
      '一个十八': 0,
      '一个十八九': 0,
      '一个十八岁': 11,
      '一个十六七岁': 12,
      '一个十六': 0,
      '一个十六七': 0,
      '一个十六岁': 4,
      '一个十几岁': 14,
      '一个十几': 0,
      '一个十四五岁': 9,
      '一个十四': 0,
      '一个十四五': 0,
      '一个十四岁': 4,
      '一个十多岁': 4,
      '一个十多': 0,
      '一个十岁': 10,
      '一个千': 15,
      '一个千年': 4,
      '一个半': 148,
      '一个半头': 4,
      '一个半月': 52,
      '一个半桩': 2,
      '一个双': 30,
      '一个名': 76,
      '一个响': 21,
      '一个四六级': 2,
      '一个四': 0,
      '一个四六': 0,
      '一个四十': 11,
      '一个四十余岁': 4,
      '一个四十余': 0,
      '一个四十出头': 2,
      '一个四十出': 0,
      '一个四十多岁': 19,
      '一个四十多': 0,
      '一个四十岁': 4,
      '一个四品': 6,
      '一个四圈': 2,
      '一个四岁': 5,
      '一个团': 89,
      '一个圈': 29,
      '一个多': 378,
      '一个多亿': 3,
      '一个多元': 8,
      '一个多头': 2,
      '一个多月': 406,
      '一个多项': 2,
      '一个天': 93,
      '一个头': 70,
      '一个套': 14,
      '一个家': 94,
      '一个少数派': 2,
      '一个少': 0,
      '一个少数': 0,
      '一个尺': 5,
      '一个巴掌拍不响': 9,
      '一个巴': 0,
      '一个巴掌': 0,
      '一个巴掌拍': 0,
      '一个巴掌拍不': 0,
      '一个帖': 8,
      '一个床': 9,
      '一个心眼': 3,
      '一个心': 0,
      '一个情节': 3,
      '一个情': 0,
      '一个愿打': 3,
      '一个愿': 0,
      '一个愿挨': 3,
      '一个打': 86,
      '一个拖拉机': 2,
      '一个拖': 0,
      '一个拖拉': 0,
      '一个排': 42,
      '一个支': 24,
      '一个数万': 3,
      '一个数': 0,
      '一个整': 13,
      '一个整团': 3,
      '一个月': 1811,
      '一个样': 62,
      '一个样儿': 5,
      '一个桶': 5,
      '一个点': 77,
      '一个班': 84,
      '一个瓢': 4,
      '一个甲子': 5,
      '一个甲': 0,
      '一个男孩': 3,
      '一个男': 0,
      '一个百里': 2,
      '一个百': 0,
      '一个盆': 5,
      '一个碗': 17,
      '一个程': 5,
      '一个第一次': 16,
      '一个第': 0,
      '一个第一': 0,
      '一个第三种': 2,
      '一个第三': 0,
      '一个筐': 5,
      '一个箭步': 3,
      '一个箭': 0,
      '一个系列': 14,
      '一个系': 0,
      '一个纸': 36,
      '一个组': 18,
      '一个终日': 2,
      '一个终': 0,
      '一个终生': 4,
      '一个肚子': 6,
      '一个肚': 0,
      '一个胎': 2,
      '一个脚印': 4,
      '一个脚': 0,
      '一个舒服': 3,
      '一个舒': 0,
      '一个萝卜一个坑': 8,
      '一个萝': 0,
      '一个萝卜': 0,
      '一个萝卜一': 0,
      '一个萝卜一个': 0,
      '一个角': 13,
      '一个身': 56,
      '一个通': 25,
      '一个遍': 7,
      '一个集': 20,
      '一个零': 10,
      '一个顶': 20,
      '一个鼻孔': 3,
      '一个鼻': 0,
      '一中': 5590,
      '一中一台': 45,
      '一中一': 0,
      '一中全会': 227,
      '一中全': 0,
      '一中院': 13,
      '一串': 687,
      '一串串': 4,
      '一串红': 2,
      '一串骊珠': 3,
      '一串骊': 0,
      '一丸': 3,
      '一举': 848,
      '一举一动': 190,
      '一举一': 0,
      '一举万里': 3,
      '一举万': 0,
      '一举三反': 3,
      '一举三': 0,
      '一举三得': 13,
      '一举两全': 3,
      '一举两': 0,
      '一举两得': 67,
      '一举中标': 3,
      '一举中': 0,
      '一举之劳': 3,
      '一举之': 0,
      '一举千里': 3,
      '一举千': 0,
      '一举四得': 4,
      '一举四': 0,
      '一举多得': 9,
      '一举多': 0,
      '一举成名': 204,
      '一举成': 0,
      '一举手一': 3,
      '一举手': 0,
      '一举数得': 11,
      '一举数': 0,
      '一久': 3,
      '一义': 3,
      '一之为甚': 3,
      '一之': 0,
      '一之为': 0,
      '一之已甚': 3,
      '一之已': 0,
      '一之谓甚': 3,
      '一之谓': 0,
      '一乐': 3,
      '一乙醇胺': 6,
      '一乙': 0,
      '一乙醇': 0,
      '一九': 25,
      '一九一一': 2,
      '一九一': 0,
      '一九一九年': 5,
      '一九一九': 0,
      '一九一二年': 2,
      '一九一二': 0,
      '一九一五年': 2,
      '一九一五': 0,
      '一九一六年': 4,
      '一九一六': 0,
      '一九一四年': 3,
      '一九一四': 0,
      '一九七': 20,
      '一九七一年': 8,
      '一九七一': 0,
      '一九七七': 4,
      '一九七七年': 18,
      '一九七三年': 8,
      '一九七三': 0,
      '一九七九年': 23,
      '一九七九': 0,
      '一九七二年': 12,
      '一九七二': 0,
      '一九七五年': 8,
      '一九七五': 0,
      '一九七八': 3,
      '一九七八年': 15,
      '一九七六': 3,
      '一九七六年': 28,
      '一九七四年': 5,
      '一九七四': 0,
      '一九七零年': 4,
      '一九七零': 0,
      '一九三': 6,
      '一九三一年': 4,
      '一九三一': 0,
      '一九三七年': 23,
      '一九三七': 0,
      '一九三三年': 4,
      '一九三三': 0,
      '一九三九年': 17,
      '一九三九': 0,
      '一九三二年': 3,
      '一九三二': 0,
      '一九三五年': 9,
      '一九三五': 0,
      '一九三八年': 17,
      '一九三八': 0,
      '一九三六年': 17,
      '一九三六': 0,
      '一九三四年': 4,
      '一九三四': 0,
      '一九九': 12,
      '一九九一年': 6,
      '一九九一': 0,
      '一九九七': 7,
      '一九九七年': 67,
      '一九九三': 2,
      '一九九三年': 9,
      '一九九九年': 18,
      '一九九九': 0,
      '一九九二': 2,
      '一九九二年': 13,
      '一九九五年': 20,
      '一九九五': 0,
      '一九九八': 3,
      '一九九八年': 47,
      '一九九六': 5,
      '一九九六年': 19,
      '一九九四年': 12,
      '一九九四': 0,
      '一九九零年': 3,
      '一九九零': 0,
      '一九二': 4,
      '一九二七年': 15,
      '一九二七': 0,
      '一九二九': 4,
      '一九二九年': 2,
      '一九二二年': 3,
      '一九二二': 0,
      '一九二五年': 5,
      '一九二五': 0,
      '一九二八年': 6,
      '一九二八': 0,
      '一九二四年': 6,
      '一九二四': 0,
      '一九五': 42,
      '一九五一年': 21,
      '一九五一': 0,
      '一九五七年': 22,
      '一九五七': 0,
      '一九五三年': 19,
      '一九五三': 0,
      '一九五九年': 13,
      '一九五九': 0,
      '一九五二年': 26,
      '一九五二': 0,
      '一九五五年': 17,
      '一九五五': 0,
      '一九五八年': 12,
      '一九五八': 0,
      '一九五六年': 10,
      '一九五六': 0,
      '一九五四年': 21,
      '一九五四': 0,
      '一九五零年': 2,
      '一九五零': 0,
      '一九八': 20,
      '一九八一年': 19,
      '一九八一': 0,
      '一九八七年': 5,
      '一九八七': 0,
      '一九八三年': 14,
      '一九八三': 0,
      '一九八九': 2,
      '一九八九年': 10,
      '一九八二年': 16,
      '一九八二': 0,
      '一九八五年': 9,
      '一九八五': 0,
      '一九八八年': 11,
      '一九八八': 0,
      '一九八六年': 13,
      '一九八六': 0,
      '一九八四年': 16,
      '一九八四': 0,
      '一九六': 17,
      '一九六一年': 8,
      '一九六一': 0,
      '一九六七年': 17,
      '一九六七': 0,
      '一九六三年': 22,
      '一九六三': 0,
      ...},
     'total': 60101967,
     'user_word_tag_tab': {},
     'initialized': True,
     'tmp_dir': None,
     'cache_file': None}




```python
print(tokenizer.get_dict_file())
print(tokenizer.cache_file)
print(tokenizer.tmp_dir)
print(tokenizer.total)
print(tokenizer.user_word_tag_tab)
```

    <_io.BufferedReader name='C:\\Users\\86185\\Documents\\文本挖掘\\jieba-master\\jieba\\dict.txt'>
    None
    None
    60101967
    {}
    

##### 手动添加新词

##### ‘冷却水泵’词频为空，说明没有该词


```python
tokenizer.FREQ.get('冷却水泵') #需要增加该词，那它的频率设为多少呢？？
```

suggest_freq 内部实现：

    ftotal = float(tokenizer.total) #全局词频
    word = segment
    freq = 1
    for seg in tokenizer.cut(word, HMM=False):  #用默认分词模式分词
        freq *= tokenizer.FREQ.get(seg, 1) / ftotal #所分子词词频除以全局词频，子词越多，则频率越小
    freq = max(int(freq * tokenizer.total) + 1, tokenizer.FREQ.get(word, 1)) #最小的频数为1


```python
ftotal = float(tokenizer.total) #全局词频
word = '冷却水泵'
freq = 1
ftotal
print(list(tokenizer.cut(word, HMM=False))) #['冷却', '水泵']
print(tokenizer.FREQ.get('冷却'),tokenizer.FREQ.get('水泵'))
for seg in tokenizer.cut(word, HMM=False):  
        freq *= tokenizer.FREQ.get(seg, 1) / ftotal 
print(freq)
freq = max(int(freq * tokenizer.total) + 1, tokenizer.FREQ.get(word, 1)) #只要该词未出现在原词典中，则，该词的词频设置为1
print(freq)
```

    ['冷却', '水泵']
    772 580
    1.239561053698521e-10
    1
    


```python
tokenizer.FREQ.get('中央空调系统')
```




    1



手动添加新词方法 tokenizer.add_word


```python
tokenizer.suggest_freq('中央空调系统', True) #不能加入新词'中央空调系统'
print(list(tokenizer.cut('中央空调系统设计', HMM=False))) #DAG分词
print(tokenizer.get_DAG('中央空调系统设计'))
#中央空调系统这个词没有加进词典，仍为未登录词
tokenizer.add_word('中央空调系统')   #可以加入新词'中央空调系统'
print(list(tokenizer.cut('中央空调系统设计', HMM=False))) #DAG分词
print(tokenizer.get_DAG('中央空调系统设计'))
tokenizer.del_word('中央空调系统')   #可以加入新词'中央空调系统'
```

    ['中央空调', '系统', '设计']
    {0: [0, 1, 3], 1: [1], 2: [2, 3], 3: [3], 4: [4, 5], 5: [5], 6: [6, 7], 7: [7]}
    ['中央空调系统', '设计']
    {0: [0, 1, 3, 5], 1: [1], 2: [2, 3], 3: [3], 4: [4, 5], 5: [5], 6: [6, 7], 7: [7]}
    


```python
sentence = '今天是个阳光明媚的好日子'
DAG = tokenizer.get_DAG(sentence)  
print(DAG) #DAG代表可能的分词路径
```

    {0: [0, 1], 1: [1], 2: [2], 3: [3], 4: [4, 5, 7], 5: [5, 6], 6: [6, 7], 7: [7], 8: [8], 9: [9, 11], 10: [10, 11], 11: [11]}
    


```python
route = {}
tokenizer.calc(sentence, DAG, route)  #关键方法：返回更新的路径词典route
route
```




    {12: (0, 0),
     11: (-8.054685595854318, 11),
     10: (-9.37201153267522, 11),
     9: (-12.358593542833603, 11),
     8: (-17.59774902869372, 8),
     7: (-29.92205349804869, 7),
     6: (-30.5188695696702, 7),
     5: (-39.1343634500467, 5),
     4: (-34.41068986778083, 7),
     3: (-40.581879214968744, 3),
     2: (-44.904833677361665, 2),
     1: (-52.325696091217054, 1),
     0: (-53.13854593411308, 1)}



## 2.2 关键词提取

### 2.2.1 基于TFIDF提取关键词 ：jieba.analyse.tfidf

原理介绍见：http://www.ruanyifeng.com/blog/2013/03/tf-idf.html

#### 某个词对文章的重要性越高，它的TF-IDF值就越大。所以，排在最前面的几个词，就是这篇文章的关键词。

![jupyter](http://www.ruanyifeng.com/blogimg/asset/201303/bg2013031506.png)
![jupyter](http://www.ruanyifeng.com/blogimg/asset/201303/bg2013031507.png)

#### 词频的几种计算方式:
![jupyter](http://www.ruanyifeng.com/blogimg/asset/201303/bg2013031503.png)
考虑到文章有长短之分，为了便于不同文章的比较，进行"词频"标准化。
![jupyter](http://www.ruanyifeng.com/blogimg/asset/201303/bg2013031504.png)
#### jieba采用的是上图这种

或者
![jupyter](http://www.ruanyifeng.com/blogimg/asset/201303/bg2013031505.png)

    def extract_tags(self, sentence, topK=20, withWeight=False, allowPOS=(), withFlag=False):
        """
        Extract keywords from sentence using TF-IDF algorithm.
        Parameter:
            - topK: return how many top keywords. `None` for all possible words.
            - withWeight: if True, return a list of (word, weight);
                          if False, return a list of words.
            - allowPOS: the allowed POS list eg. ['ns', 'n', 'vn', 'v','nr'].
                        if the POS of w is not in this list,it will be filtered.
            - withFlag: only work with allowPOS is not empty.
                        if True, return a list of pair(word, weight) like posseg.cut
                        if False, return a list of words
        """
        if allowPOS:
            allowPOS = frozenset(allowPOS)
            words = self.postokenizer.cut(sentence)
        else:
            words = self.tokenizer.cut(sentence)
        freq = {}
        for w in words: #先分词
            if allowPOS:
                if w.flag not in allowPOS:
                    continue
                elif not withFlag:
                    w = w.word
            wc = w.word if allowPOS and withFlag else w
            if len(wc.strip()) < 2 or wc.lower() in self.stop_words:
                continue
            freq[w] = freq.get(w, 0.0) + 1.0 #词在sentence中出现的次数--词频
        total = sum(freq.values()) #总词频
        for k in freq:
            kw = k.word if allowPOS and withFlag else k
            freq[k] *= self.idf_freq.get(kw, self.median_idf) / total #
            #对每个词求tfidf，其中TF = 词频 / total 标准化——解决文本长短不一问题

        if withWeight:
            tags = sorted(freq.items(), key=itemgetter(1), reverse=True)
        else:
            tags = sorted(freq, key=freq.__getitem__, reverse=True)
        if topK:
            return tags[:topK]
        else:
            return tags


```python
import time
from jieba.analyse.tfidf import TFIDF

start = time.time()
tfidf = TFIDF()
end = time.time()
print(end-start) #加载得很快
```

    0.2693009376525879
    


```python
print(tfidf.__dict__.keys())
tfidf.__dict__
```

    dict_keys(['tokenizer', 'postokenizer', 'stop_words', 'idf_loader', 'idf_freq', 'median_idf'])
    




    {'tokenizer': <Tokenizer dictionary=None>,
     'postokenizer': <POSTokenizer tokenizer=<Tokenizer dictionary=None>>,
     'stop_words': {'all',
      'an',
      'and',
      'are',
      'as',
      'at',
      'be',
      'by',
      'can',
      'for',
      'from',
      'has',
      'have',
      'if',
      'in',
      'is',
      'it',
      'not',
      'of',
      'on',
      'one',
      'or',
      'that',
      'the',
      'then',
      'this',
      'to',
      'we',
      'which',
      'with',
      'you'},
     'idf_loader': <jieba.analyse.tfidf.IDFLoader at 0x21707c2c208>,
     'idf_freq': {'劳动防护': 13.900677652,
      '生化学': 13.900677652,
      '奥萨贝尔': 13.900677652,
      '考察队员': 13.900677652,
      '岗上': 11.5027823792,
      '倒车档': 12.2912397395,
      '编译': 9.21854642485,
      '蝶泳': 11.1926274509,
      '外委': 11.8212361103,
      '故作高深': 11.9547675029,
      '尉遂成': 13.2075304714,
      '心源性': 11.1926274509,
      '现役军人': 10.642581114,
      '杜勃留': 13.2075304714,
      '包天笑': 13.900677652,
      '贾政陪': 13.2075304714,
      '托尔湾': 13.900677652,
      '多瓦': 12.5143832909,
      '多瓣': 13.900677652,
      '巴斯特尔': 11.598092559,
      '刘皇帝': 12.8020653633,
      '亚历山德罗夫': 13.2075304714,
      '社会公众': 8.90346537821,
      '五百份': 12.8020653633,
      '两点阈': 12.5143832909,
      '多瓶': 13.900677652,
      '冰天': 12.2912397395,
      '库布齐': 11.598092559,
      '龙川县': 12.8020653633,
      '银燕': 11.9547675029,
      '历史风貌': 11.8212361103,
      '信仰主义': 13.2075304714,
      '頷': 10.2897597393,
      '好色': 10.0088573539,
      '款款而行': 12.5143832909,
      '凳子': 8.36728816325,
      '二部': 9.93038573842,
      '卢巴': 12.1089181827,
      '五百五': 13.2075304714,
      '鳓': 11.0103058941,
      '畅叙': 11.598092559,
      '吴栅子': 13.2075304714,
      '智力竞赛': 13.900677652,
      '库邦': 13.2075304714,
      '非正义': 11.3357282945,
      '编订': 10.2897597393,
      '悲号': 12.8020653633,
      '陈庄搭': 13.2075304714,
      '二郎': 9.62401153296,
      '电光石火': 11.8212361103,
      '抢球': 11.9547675029,
      '南澳大利亚': 10.9562386728,
      '失散多年': 12.5143832909,
      '有理有据': 10.9562386728,
      '盈利': 5.72260018813,
      '弗龙堡': 13.900677652,
      '悚然': 10.604840786,
      '查吓': 13.2075304714,
      '滕县': 10.9049453784,
      '毛瑟枪': 12.2912397395,
      '好花': 11.2616203224,
      '潮州人': 13.900677652,
      '头羊': 11.5027823792,
      '提足': 12.5143832909,
      '书款': 12.2912397395,
      '嗤之以鼻': 10.642581114,
      '代金券': 11.9547675029,
      '公共财产': 11.4157710022,
      '文化素质': 10.765183436,
      '口称': 10.0505300503,
      '聚异丁烯': 12.1089181827,
      '终南山': 10.4349417492,
      '东安动力': 10.2630914922,
      '集训营': 13.2075304714,
      '截留': 9.94943393339,
      '热烈欢迎': 9.91169360541,
      '岗亭': 11.598092559,
      '浑球': 13.900677652,
      '让座': 10.4349417492,
      '迁户': 13.2075304714,
      '布尔热': 12.5143832909,
      '绣花针儿': 11.598092559,
      '二通': 11.8212361103,
      '滑雪运动': 11.7034530746,
      '程颢': 10.3743171274,
      '五百万': 10.9049453784,
      '旱荒': 12.5143832909,
      '标准线': 13.900677652,
      '时后梁': 12.2912397395,
      '外备': 12.5143832909,
      '绝对权': 13.2075304714,
      '蕉麻': 11.5027823792,
      '痎': 12.5143832909,
      '黎刹': 12.2912397395,
      '二十余年': 10.0720362555,
      '好苦': 10.8096351986,
      '镇心': 11.598092559,
      '残茬': 11.598092559,
      '从界岭': 12.1089181827,
      '湟': 10.2117981979,
      '国际经济组织': 11.8212361103,
      '五百两': 9.94943393339,
      '后手': 11.3357282945,
      '广播公司': 10.0720362555,
      '诞生地': 10.533381822,
      '二遍': 10.8561552143,
      '縌': 12.8020653633,
      '遂溪': 12.1089181827,
      '五百个': 10.8096351986,
      '不知高下': 13.900677652,
      '盈动': 11.9547675029,
      '程颐': 9.89334446674,
      '外头': 7.76079309975,
      '二道': 9.43476953332,
      '外夷': 11.0103058941,
      '喷洒车': 13.2075304714,
      '过会芳': 13.2075304714,
      '含金量': 9.72629038208,
      '外壁': 10.7226238216,
      '运猪': 13.900677652,
      '伶俐': 9.5186510173,
      '滑来滑去': 13.2075304714,
      '四轮驱动': 10.9562386728,
      '多病': 9.75754292558,
      '时至今日': 8.81308131674,
      '上': 2.52604920291,
      '卖火柴': 12.1089181827,
      '后接': 12.5143832909,
      '发射器': 8.52078029844,
      '迭宕': 13.900677652,
      '索尼': 9.6811699468,
      '鹿角霜': 12.8020653633,
      '双日': 11.5027823792,
      '用之不竭': 10.8561552143,
      '诊病': 11.1280889297,
      '职能': 6.70924832194,
      '军民联欢': 13.900677652,
      '周迥': 13.2075304714,
      '策源地': 10.5684731418,
      '后掌': 12.8020653633,
      '奸夫淫妇': 12.5143832909,
      '北五祖': 11.8212361103,
      '分析仪器': 11.0103058941,
      '加州大学': 11.1926274509,
      '服用者': 12.2912397395,
      '付出代价': 10.0505300503,
      '枯': 9.02548032877,
      '小兴安岭': 9.5186510173,
      '暴涨暴跌': 9.89334446674,
      '额窦': 12.5143832909,
      '库里': 10.2117981979,
      '和良渚': 12.5143832909,
      '后排': 8.81927328699,
      '张羽': 11.1280889297,
      '落脚点': 10.4349417492,
      '多会儿': 11.9547675029,
      '地动仪': 11.9547675029,
      '外境': 12.2912397395,
      '进贤县': 13.2075304714,
      '冰塔': 12.8020653633,
      '乳腺': 9.25628675283,
      '漆绘': 12.2912397395,
      '尤尔弗': 13.900677652,
      '岗位': 7.86519621945,
      '诊疗': 9.15574552361,
      '万公斤': 11.2616203224,
      '救下来': 11.7034530746,
      '折梅': 12.8020653633,
      '壑': 9.63799777493,
      '虎口脱险': 11.9547675029,
      '蜜蜂': 8.78868986362,
      '长角牛': 12.1089181827,
      '平滑肌': 9.4233408375,
      '外墙': 10.3743171274,
      '斯坦贝克': 11.4157710022,
      '后援': 10.8096351986,
      '多疑': 9.25628675283,
      '大水沟': 13.2075304714,
      '光机所': 13.900677652,
      '王治朝': 13.2075304714,
      '孤行': 12.5143832909,
      '诉讼法': 9.37888907493,
      '奥运会': 8.16733637508,
      '会合点': 11.7034530746,
      '票子': 9.48183704418,
      '二重': 10.0505300503,
      '声全息图': 13.900677652,
      '胡正卿': 12.1089181827,
      '教学进度': 13.900677652,
      '人证物证': 11.5027823792,
      '算进来': 12.8020653633,
      '积雨云': 11.0674643079,
      '人微言轻': 11.3357282945,
      '开路先锋': 11.3357282945,
      '董琬': 12.8020653633,
      '梁父吟': 12.2912397395,
      '两百二十册': 13.2075304714,
      '傅大人': 11.2616203224,
      '张家辉': 13.900677652,
      '百米': 9.02548032877,
      '连遭败绩': 12.8020653633,
      '暴发户': 9.87532596124,
      '多留': 10.0088573539,
      '分宜': 12.2912397395,
      '汝可先': 12.2912397395,
      '宇文泰和': 12.5143832909,
      '五百余': 10.4666904475,
      '寒潮': 9.05649056552,
      '大水池': 12.5143832909,
      '陈循': 13.900677652,
      '多番': 11.9547675029,
      '旱船': 11.7034530746,
      '十一名': 11.9547675029,
      '慢条斯理': 9.91169360541,
      '卢尔': 13.2075304714,
      '高低杠': 11.5027823792,
      '海西州': 13.2075304714,
      '官腔': 10.3743171274,
      '求贤若渴': 11.9547675029,
      '日喀则市': 11.4157710022,
      '多种营养': 12.2912397395,
      '新老交替': 13.2075304714,
      '手牵着': 11.0674643079,
      '书橱': 11.2616203224,
      '情郎': 11.7034530746,
      '江陵县': 10.4349417492,
      '通布卡': 13.900677652,
      '医药卫生': 10.2117981979,
      '渭川千亩': 13.900677652,
      '莫恰洛': 12.5143832909,
      '房舱': 13.2075304714,
      '冰壁': 10.4349417492,
      '焦庄户': 12.8020653633,
      '既想': 11.7034530746,
      '就业结构': 11.9547675029,
      '人类学': 8.81308131674,
      '潭州': 10.4666904475,
      '训练班': 9.71102290995,
      '骚动': 8.61241062128,
      '鸿业': 11.5027823792,
      '今年底': 8.78868986362,
      '好菜': 11.1280889297,
      '小亚丁': 13.900677652,
      '店伙': 12.8020653633,
      '马鞭': 9.66657114738,
      '高负荷': 13.900677652,
      '房舍': 8.96620371885,
      '悲剧': 7.55855623325,
      '缅甸': 7.81390292506,
      '泌尿器官': 13.900677652,
      '免罚': 13.900677652,
      '总商会': 11.4157710022,
      '口喊着': 13.2075304714,
      '截球': 13.2075304714,
      '最省': 12.1089181827,
      '减薪': 10.642581114,
      '辛丑和约': 12.2912397395,
      '外寇': 13.2075304714,
      '躲藏着': 12.5143832909,
      '浮来': 13.2075304714,
      '莫尔耶': 13.900677652,
      '撒手不管': 10.4994802703,
      '卢循': 12.1089181827,
      '垬': 7.63537643924,
      '枯木朽株': 13.900677652,
      '卢德': 12.1089181827,
      '多盘': 12.2912397395,
      '幽期密约': 13.900677652,
      '花生饼': 12.8020653633,
      '斯堪尼亚': 13.2075304714,
      '易中天': 13.2075304714,
      '左膀': 13.900677652,
      '多目': 12.8020653633,
      '郎咸平': 11.0103058941,
      '赏月': 10.0505300503,
      '寒威': 12.5143832909,
      '贺兰': 10.7226238216,
      '邪风': 12.5143832909,
      '好者': 13.900677652,
      '蒋御史': 13.900677652,
      '多相': 10.2630914922,
      '古观象台': 11.7034530746,
      '好耍': 11.0103058941,
      '老谋深算': 10.4041700905,
      '后悔': 7.32142643997,
      '游嬉恰': 13.900677652,
      '伤心落泪': 10.9049453784,
      '韩非则': 13.2075304714,
      '服用药': 13.2075304714,
      '格林卡': 11.5027823792,
      '正话': 10.8561552143,
      '叶碧秋': 8.49350588052,
      '姜丝排': 12.5143832909,
      '贺卡': 12.1089181827,
      '拖住': 9.21854642485,
      '悲凄': 11.0674643079,
      '葛翠琳': 13.900677652,
      '吴景超': 12.1089181827,
      '银灯': 13.2075304714,
      '悲凉': 9.35738286971,
      '睃': 9.91169360541,
      '外客': 12.1089181827,
      '外宣': 10.9049453784,
      '情报搜集': 11.598092559,
      '狗仔队': 13.2075304714,
      '裁汰': 10.7226238216,
      '践': 10.8561552143,
      '位于下面': 13.2075304714,
      '子禄父': 12.1089181827,
      '埃弗里': 12.5143832909,
      '乌尔斯': 13.2075304714,
      '外宾': 10.5684731418,
      '外宿': 13.900677652,
      '咱村': 9.96885201925,
      '从宽处理': 11.9547675029,
      '赊贷': 11.3357282945,
      '免纳': 11.7034530746,
      '蜕壳激素': 13.900677652,
      '表意文字': 12.1089181827,
      '趁心如意': 13.900677652,
      '悲叹': 10.604840786,
      '人所共知': 10.0088573539,
      '家电企业': 10.3743171274,
      '距离处': 11.9547675029,
      '风情万种': 10.8561552143,
      '外存': 12.5143832909,
      '外孙': 9.85762638414,
      '梅里威': 13.2075304714,
      '亚圣': 12.1089181827,
      '周至县': 11.5027823792,
      '采编部': 13.900677652,
      '怀特河': 13.2075304714,
      '外学': 11.7034530746,
      '马八儿': 12.2912397395,
      '圣路易斯': 10.2630914922,
      '合线期': 13.900677652,
      '凿井': 10.6818018271,
      '联贯性': 13.900677652,
      '冰室': 13.2075304714,
      '显身手': 12.5143832909,
      '后怕': 9.91169360541,
      '赏析': 12.1089181827,
      '瓦德希': 13.2075304714,
      '卢彦': 13.900677652,
      '切齿痛恨': 11.4157710022,
      '不惜一战': 13.900677652,
      '千百万': 10.0720362555,
      '战斗分队': 12.2912397395,
      '夜壶': 10.9562386728,
      '配': 8.11071748108,
      '古巴共和国': 13.2075304714,
      '缘薄': 13.900677652,
      '麦禾': 12.8020653633,
      '毋须': 11.5027823792,
      '测试者': 12.2912397395,
      '乌巢劫': 13.2075304714,
      '吃大户': 11.2616203224,
      '平城南': 13.900677652,
      '勠': 12.5143832909,
      '风风光光': 11.4157710022,
      '镇巴': 12.5143832909,
      '江三公子': 13.2075304714,
      '拨乱反正': 10.3171587135,
      '戒酒': 10.4349417492,
      '一千五百多名': 13.2075304714,
      '好胜': 11.5027823792,
      '多瘦': 13.2075304714,
      '最矮': 12.5143832909,
      '铺设': 8.68574189437,
      '最短': 9.28555713513,
      '标准粉': 13.2075304714,
      '折款': 13.900677652,
      '房脊': 11.598092559,
      '信奉者': 11.5027823792,
      '绝对数': 11.0674643079,
      '鸡冠花': 11.8212361103,
      '坏血酸': 13.900677652,
      '外嫁': 13.900677652,
      '萝北': 12.5143832909,
      '张泽咸': 12.2912397395,
      '空置率': 11.0674643079,
      '款洽': 13.900677652,
      '恩仇记': 13.2075304714,
      '拖上': 11.598092559,
      '拖下': 12.8020653633,
      '好脸': 13.2075304714,
      '投河自尽': 11.7034530746,
      '博蒙': 12.8020653633,
      '张高丽': 12.8020653633,
      '欢音': 12.8020653633,
      '方方正正': 10.8096351986,
      '私人教师': 11.7034530746,
      '医务部': 12.8020653633,
      '慢点': 10.6818018271,
      '马宅': 11.7034530746,
      '查哨': 11.8212361103,
      '零所': 13.2075304714,
      '钥': 10.3171587135,
      '海关检查': 12.5143832909,
      '弗雷泽': 11.598092559,
      '血糖仪': 12.2912397395,
      '民航机场': 11.598092559,
      '异端邪说': 11.8212361103,
      '既成': 11.0103058941,
      '吹风会': 11.0674643079,
      '霅': 13.900677652,
      '活字版': 11.9547675029,
      '阝': 11.9547675029,
      '黄风吹': 13.2075304714,
      '多石': 12.2912397395,
      '朴不花': 12.5143832909,
      '广南西': 11.5027823792,
      '叶祖': 11.1926274509,
      '姊妹花': 11.5027823792,
      '仉': 10.7226238216,
      '萝卜': 8.6803218269,
      '陇海路': 9.93038573842,
      '刁羊': 11.9547675029,
      '供办': 12.8020653633,
      '二千五百元': 13.900677652,
      '地图更新': 13.900677652,
      '天津市委': 10.9562386728,
      '三四百斤': 12.1089181827,
      '百忙之中': 10.9562386728,
      '没前途': 12.1089181827,
      '刑讯': 11.8212361103,
      '百级': 13.900677652,
      '镤': 12.5143832909,
      '高得幸': 13.2075304714,
      '受贿者': 12.2912397395,
      '普通住宅': 10.2117981979,
      '枪打出头鸟': 13.2075304714,
      '树皮画': 12.8020653633,
      '强弩之末': 10.1164880181,
      '铸造蜡': 13.900677652,
      '咽喉': 8.22392384971,
      '阮大人': 12.8020653633,
      '暴发性': 11.598092559,
      '保险制度': 10.7226238216,
      '另行通知': 12.2912397395,
      '韩世昌': 12.2912397395,
      '侈': 11.9547675029,
      '外套': 9.20932976975,
      '多着': 12.5143832909,
      '甏': 10.9049453784,
      '空穴': 10.1871055853,
      '扫黄办': 13.2075304714,
      '祖白圭': 12.8020653633,
      '公平交易': 9.69598503258,
      '牵过来': 11.8212361103,
      '刑警': 11.1280889297,
      '陈求发': 12.8020653633,
      '刡': 11.8212361103,
      '贾政问': 12.8020653633,
      '立体声': 10.642581114,
      '卢布': 9.62401153296,
      '智能网': 13.2075304714,
      '左臂': 9.31571017331,
      '娄室之': 13.2075304714,
      '卢帕': 13.2075304714,
      '杜若': 12.2912397395,
      '郭攸之': 12.5143832909,
      '兄友弟恭': 12.5143832909,
      '容星桥': 13.2075304714,
      '萨拉班': 12.8020653633,
      '下流无耻': 13.900677652,
      '桑德斯': 12.8020653633,
      '二人同心': 13.900677652,
      '文崔二': 12.5143832909,
      '自误': 11.8212361103,
      '多看': 9.75754292558,
      '宁王': 11.3357282945,
      '玉华王': 11.9547675029,
      '不饱和': 9.16447920358,
      '慢火': 11.598092559,
      '王秀兰': 12.8020653633,
      '书档': 13.2075304714,
      '耐压性': 13.900677652,
      '截瘫': 11.7034530746,
      '圥': 13.2075304714,
      '宁玛': 12.1089181827,
      '户主': 10.6818018271,
      '易舟浮': 13.2075304714,
      '穆然城': 13.2075304714,
      '对话会': 13.2075304714,
      '海蜇头': 13.900677652,
      '多眼': 11.1926274509,
      '轳': 13.900677652,
      '书案': 9.49395840471,
      '瓕': 11.7034530746,
      '握力': 13.2075304714,
      '书桌': 9.87532596124,
      '遮面': 13.2075304714,
      '内廷紫': 13.2075304714,
      '八节': 11.598092559,
      '袁姑爷': 10.4349417492,
      '零散': 9.33632946051,
      '编过': 12.5143832909,
      '国台办': 11.5027823792,
      '蓝孔雀': 13.2075304714,
      '库银': 13.900677652,
      '同翅目': 10.8096351986,
      '零数': 11.9547675029,
      '上海滩': 10.4666904475,
      '正表': 13.900677652,
      '黎国': 13.900677652,
      '电焊条': 12.8020653633,
      '二钱': 11.0674643079,
      '交通违章': 12.2912397395,
      '五卅运动': 10.0940151622,
      '贡二水': 12.8020653633,
      '傣': 9.55687223012,
      '蜜色': 13.900677652,
      '以远': 11.9547675029,
      '百科': 10.1630080337,
      '左舷': 12.1089181827,
      '新媳妇': 9.85762638414,
      '外差': 11.9547675029,
      '竞争性': 9.62401153296,
      '编述': 12.5143832909,
      '孤负': 12.5143832909,
      '百种': 9.61021821083,
      '杨炎官': 13.2075304714,
      '每下愈况': 13.900677652,
      '博莱': 12.2912397395,
      '少数整': 12.8020653633,
      '宗羲': 12.2912397395,
      '新疆省': 10.9049453784,
      '由近而远': 12.8020653633,
      '镇子': 9.28555713513,
      '丽丽': 9.87532596124,
      '靳祥': 12.8020653633,
      '类型学': 11.2616203224,
      '小象虫': 13.2075304714,
      '烈女传': 13.2075304714,
      '史志宏': 11.8212361103,
      '四十六次': 13.2075304714,
      '编辑': 6.28685896717,
      '黑白两道': 11.598092559,
      '交换条件': 11.0103058941,
      '立体式': 12.8020653633,
      '发射区': 11.8212361103,
      '广陵派': 13.2075304714,
      '卢姆': 12.1089181827,
      '国务院法制办': 11.1926274509,
      '租下来': 13.2075304714,
      '孪': 10.4994802703,
      '私生活': 10.533381822,
      '山竹子': 13.2075304714,
      '神使鬼差': 13.900677652,
      '卢世荣': 12.2912397395,
      '任姓挚': 13.2075304714,
      '试述': 13.900677652,
      '多点': 8.86372504956,
      '囷': 8.98802276624,
      '诱导酶': 13.900677652,
      '阿旃陀': 10.9049453784,
      '夏耘': 13.900677652,
      '王爵封': 13.2075304714,
      '哈飞公司': 13.2075304714,
      '院校': 8.81927328699,
      '养阴': 10.7226238216,
      '个性特点': 12.5143832909,
      '第十七个': 13.900677652,
      '第二十六章': 10.5684731418,
      '潘公凯': 13.900677652,
      '镇定': 8.37124856446,
      '争嘴': 13.900677652,
      '专题讲座': 12.2912397395,
      '女追男': 13.900677652,
      '镇宅': 11.4157710022,
      '感受一下': 11.3357282945,
      '零时': 9.14708746087,
      '资源税': 10.2117981979,
      '项怀诚': 12.8020653633,
      '谛': 9.98865464655,
      '王立武': 13.2075304714,
      '镇安': 10.4041700905,
      '镇守': 8.38724890581,
      '一筐': 10.7226238216,
      '够格': 12.5143832909,
      '昐': 11.3357282945,
      '脉动': 9.98865464655,
      '级别': 7.50541605386,
      '竟陵': 10.7226238216,
      '全国学联': 12.2912397395,
      '贺喜': 9.38981814546,
      '宝钗素': 12.2912397395,
      '多灾': 11.598092559,
      '萨克森': 9.45802639549,
      '杨国强': 13.2075304714,
      '几十艘': 13.900677652,
      '严防': 9.56994431169,
      '元老级': 11.8212361103,
      '票庄': 13.2075304714,
      '足球界': 11.8212361103,
      '洮南': 11.9547675029,
      '双力': 13.2075304714,
      '后景': 12.8020653633,
      '截然': 9.05649056552,
      '照耀': 8.67493097826,
      '来江州': 12.5143832909,
      '丽人': 11.1926274509,
      '用途林': 12.8020653633,
      '戒面': 13.900677652,
      '上海港': 10.2371160058,
      '昏昏欲睡': 10.6818018271,
      '八艘': 11.9547675029,
      '撸子': 12.8020653633,
      '开门见山': 9.59661255877,
      '觞': 11.8212361103,
      '卢奇': 12.1089181827,
      '慢着': 10.533381822,
      '欢送': 10.604840786,
      '不作美': 13.900677652,
      '斯海姆': 12.8020653633,
      '合作局': 13.2075304714,
      '良': 9.45802639549,
      '丽亚': 12.2912397395,
      '上海电影制片厂': 10.2630914922,
      '川东南': 11.598092559,
      '布特莱齐': 13.900677652,
      '拉栖第': 10.3743171274,
      '明铁盖': 12.2912397395,
      '主掌': 11.7034530746,
      '脱氧核糖核酸': 10.1164880181,
      '阿拉斯加': 9.13850371718,
      '乌孙王': 11.9547675029,
      '塑胶管': 12.8020653633,
      '落马洲': 13.2075304714,
      '历经沧桑': 12.5143832909,
      '羊背石': 11.4157710022,
      '姑父': 9.72629038208,
      '姑爹': 13.2075304714,
      '桂林人': 12.2912397395,
      '张廷玉': 11.0674643079,
      '二十余家': 12.5143832909,
      '玎珰': 13.900677652,
      '冰封': 9.77354326693,
      '四出戏': 13.900677652,
      '海蚀台': 13.2075304714,
      '群而不党': 13.900677652,
      '戚': 9.94943393339,
      '鲁比亚': 12.8020653633,
      '输送泵': 13.2075304714,
      '老街区': 13.2075304714,
      '千态万状': 13.900677652,
      '铭心镂骨': 12.5143832909,
      '查克': 12.2912397395,
      '陈女士': 10.4994802703,
      '达官显宦': 12.8020653633,
      '人才流': 13.900677652,
      '适量水': 13.2075304714,
      '黑娃': 8.0985592766,
      '光纤网': 13.900677652,
      '傲雪凌霜': 13.900677652,
      '潭头': 12.8020653633,
      '电抗器': 11.5027823792,
      '后果': 7.19748953873,
      '牛山湖': 12.8020653633,
      '警报系统': 11.9547675029,
      '为民除害': 10.765183436,
      '应明辨': 12.8020653633,
      '喝进去': 12.2912397395,
      '李老爷': 11.598092559,
      '寒冬腊月': 11.2616203224,
      '冰屑': 11.9547675029,
      '多媒体信息': 12.8020653633,
      '美国纽约大学': 11.1926274509,
      '非常容易': 10.0505300503,
      '解放军部队': 12.1089181827,
      '睌': 8.95903522937,
      '复旦大学': 8.79473217808,
      '冰层': 9.28555713513,
      '二间': 12.8020653633,
      '仪器仪表': 9.56994431169,
      '远亲近友': 13.2075304714,
      '变幻莫测': 10.4994802703,
      '劲风': 11.0103058941,
      '外岛': 12.2912397395,
      '厚脸皮': 13.900677652,
      '奥威尔': 12.8020653633,
      '信息处理': 9.43476953332,
      '冰山': 9.29550746599,
      '几十箱': 13.2075304714,
      '老少爷们儿': 13.2075304714,
      '贩贱卖贵': 13.900677652,
      '非她不可': 13.2075304714,
      '成仙成': 13.2075304714,
      '夏历': 9.71102290995,
      '最灵': 11.3357282945,
      '投资银行业': 12.8020653633,
      '四时之气': 13.900677652,
      '外层': 8.83808261895,
      '长春电影制片厂': 11.1926274509,
      '张维': 11.598092559,
      '李虞候': 11.7034530746,
      '上海大众': 9.34680076038,
      '冰岛': 9.12155415886,
      '过磷酸': 13.2075304714,
      '外屋': 10.642581114,
      '小角色': 12.1089181827,
      '默不作声': 10.0505300503,
      '服罪': 11.9547675029,
      '查出': 8.40350942668,
      '哑巴亏': 11.9547675029,
      '防雷击': 13.900677652,
      '雅鲁藏布江': 8.97342396682,
      '分清主次': 13.900677652,
      '混起': 13.900677652,
      '后有': 11.0674643079,
      '海瑞罢官': 11.0674643079,
      '中饱私囊': 11.4157710022,
      '尼科西亚': 12.1089181827,
      '朱三松': 12.5143832909,
      '后期': 6.18778669049,
      '瀹': 6.80478443088,
      '画眉鸟': 12.1089181827,
      '洞鉴': 12.2912397395,
      '刑赏': 11.8212361103,
      '宇文泰嗣': 12.8020653633,
      '和平解决': 9.32596667347,
      '中草药': 9.28555713513,
      '一站式': 10.0720362555,
      '不怕困难': 12.5143832909,
      '标准箱': 11.2616203224,
      '后来': 4.99211827683,
      '心细': 10.5684731418,
      '戒除': 10.9049453784,
      '八荒': 12.8020653633,
      '刑责': 12.5143832909,
      '电信业': 11.0103058941,
      '帅营': 13.900677652,
      '逗乐': 11.0103058941,
      '固溶体': 10.642581114,
      '玄稽沉': 13.2075304714,
      '情夫': 13.2075304714,
      '减色': 11.9547675029,
      '巴拉那': 11.7034530746,
      '明叔让': 12.5143832909,
      '冰峰': 12.2912397395,
      '最烦': 11.8212361103,
      '待命状态': 12.8020653633,
      '近红外': 11.0103058941,
      '李永芳': 12.2912397395,
      '闸阀': 11.9547675029,
      '快撤': 11.7034530746,
      '宗明昌': 12.8020653633,
      '最热': 8.73589167805,
      '森严壁垒': 13.900677652,
      '千岛群岛': 10.6818018271,
      '技艺': 8.0600359946,
      '激光管': 13.900677652,
      '相当规模': 9.82314020807,
      '极端愚蠢': 13.2075304714,
      '业务室': 13.2075304714,
      '诉讼案': 10.2897597393,
      '杨国平': 12.1089181827,
      '从乐亭': 13.900677652,
      '降霜': 13.900677652,
      '闸门': 9.28555713513,
      '静止': 7.98988100794,
      '几万倍': 12.2912397395,
      '悲喜': 11.2616203224,
      '氦氖激光器': 13.2075304714,
      '后撤': 9.40086798165,
      '既未': 11.5027823792,
      '帝斯': 13.900677652,
      '创立': 6.8787012289,
      '自投罗网': 10.3171587135,
      '二难': 11.4157710022,
      '统战部门': 13.900677652,
      '马小舍': 12.2912397395,
      '团服': 13.900677652,
      '内利斯': 11.598092559,
      '贾政道': 9.45802639549,
      '卢宅': 12.8020653633,
      '八股': 9.53122979951,
      '幻灯机': 12.5143832909,
      '背不住': 13.900677652,
      '中国人民解放军空军': 11.1926274509,
      '拔出去': 13.900677652,
      '王峰': 10.642581114,
      '外快': 10.7226238216,
      '四五千里': 13.2075304714,
      '既有': 7.11622058934,
      '宗社': 10.9049453784,
      '纻': 10.642581114,
      '百无一见': 13.900677652,
      '纯棉纱': 12.8020653633,
      '百篇': 10.9562386728,
      '从维熙': 12.8020653633,
      '斯宾诺': 13.900677652,
      '外径': 11.0674643079,
      '童大人': 11.0103058941,
      '市政建设': 10.3743171274,
      '猜谜': 11.1280889297,
      '当代人': 12.1089181827,
      '谄上欺下': 13.900677652,
      '宗祖': 12.8020653633,
      '神农本草经': 10.9049453784,
      '卡波济': 13.900677652,
      '骑马打仗': 11.3357282945,
      '梅斯基': 13.2075304714,
      '减至': 9.19114745066,
      '查到': 9.66657114738,
      '尼泊尔共产党': 13.2075304714,
      '卢寻': 13.2075304714,
      '另起炉灶': 11.2616203224,
      '不可理喻': 10.6818018271,
      '宗祠': 10.533381822,
      '零月': 13.2075304714,
      '未处理': 13.2075304714,
      '少尉': 9.85762638414,
      '情面': 10.2897597393,
      '政法干部': 12.5143832909,
      '高等学府': 9.37888907493,
      '懊悔无及': 12.8020653633,
      '马加比': 13.2075304714,
      '不安全感': 11.4157710022,
      '和启东': 13.2075304714,
      '米勒德': 12.8020653633,
      '民族乐器': 10.9049453784,
      '由合子': 13.2075304714,
      '查勤': 13.900677652,
      '中国篮协': 13.900677652,
      '慢用': 12.5143832909,
      '统战部长': 11.9547675029,
      '二阶': 10.2117981979,
      '韦奇伍': 13.900677652,
      '利润率': 7.2673592187,
      '岸线': 8.80692745117,
      '亿加元': 12.5143832909,
      '地广': 12.1089181827,
      '逆我者死': 13.900677652,
      '南泥湾': 11.1926274509,
      '缘自': 11.9547675029,
      '外形': 7.45178825783,
      '多数三项': 13.900677652,
      '汪若海': 11.4157710022,
      '中国人民解放军三军仪仗队': 12.2912397395,
      '特库蒂': 13.2075304714,
      '欢闹': 12.8020653633,
      '百等': 13.2075304714,
      '风信子': 12.5143832909,
      '查勘': 10.2897597393,
      '如法炮制': 11.0103058941,
      '二队': 10.642581114,
      '坛坛罐罐': 11.2616203224,
      '游览胜地': 8.83177344976,
      '博多湾': 13.900677652,
      '镇委': 12.2912397395,
      '日本东京证券交易所': 13.900677652,
      '从今以后': 9.4233408375,
      '我姐': 10.7226238216,
      '阿弥陀': 11.4157710022,
      '戊子': 13.2075304714,
      '金乌西坠': 12.8020653633,
      '埃努古': 13.900677652,
      '纯如': 13.900677652,
      '冰心': 10.4349417492,
      '姬宗周': 13.2075304714,
      '魏延领': 11.8212361103,
      '外引': 13.2075304714,
      '家电网': 12.1089181827,
      '待物': 13.900677652,
      '杭嘉和': 8.39534611604,
      '千百件': 13.900677652,
      '职蜂': 13.2075304714,
      '外弦': 13.2075304714,
      '悲啼': 11.0103058941,
      '耳边风': 12.5143832909,
      '旱芹': 13.900677652,
      '查办': 9.74179456862,
      '配在一起': 12.5143832909,
      '情韵': 11.598092559,
      '别难过': 11.2616203224,
      '外强': 11.7034530746,
      '文国庆': 11.3357282945,
      '大连市': 9.66657114738,
      '岸礁': 11.9547675029,
      '开发计划署': 13.900677652,
      '反省': 9.4233408375,
      '减肥': 8.30225569298,
      '向父皇': 12.8020653633,
      '宫太后': 10.0088573539,
      '工具书': 9.91169360541,
      '图尔卡纳湖': 12.8020653633,
      '后方': 7.57811241205,
      '血循环': 10.604840786,
      '提供方便': 10.5684731418,
      '百端': 11.598092559,
      '龙的传人': 13.900677652,
      '十五丈': 13.2075304714,
      '目标群体': 12.5143832909,
      '廊房头条': 13.2075304714,
      '多班': 13.2075304714,
      '莫泽尔': 13.900677652,
      '乳状物': 13.900677652,
      '凋残': 11.8212361103,
      '悲咽': 12.5143832909,
      '篾青': 13.900677652,
      '蜜腺': 10.533381822,
      '后文': 12.1089181827,
      '嫡子': 10.9049453784,
      '最爱': 8.77671367257,
      '外延': 8.87679713113,
      '嫡孙': 11.9547675029,
      '米字旗': 13.2075304714,
      '小团体': 11.2616203224,
      '最爽': 12.5143832909,
      '仡': 13.900677652,
      '正梳妆': 13.900677652,
      '指甲钳': 13.900677652,
      '借壳上市': 9.5062284973,
      '十大元帅': 13.900677652,
      '后日': 9.87532596124,
      '梦牵魂绕': 11.9547675029,
      '潭子': 12.5143832909,
      '拙': 10.2117981979,
      '带头羊': 13.900677652,
      '魏末': 11.5027823792,
      '鼎立': 10.0294766411,
      '书法': 7.8184587416,
      '掩其不备': 13.2075304714,
      '林网化': 11.598092559,
      '交流电路': 10.9049453784,
      '古定剑': 12.5143832909,
      '少私寡欲': 12.8020653633,
      '上课时数': 13.900677652,
      '具体化': 10.2897597393,
      '悲哭': 11.1926274509,
      '尖锐湿疣': 11.2616203224,
      '查字法': 13.900677652,
      '技能': 8.16733637508,
      '张勋遂': 12.8020653633,
      '冰库': 12.2912397395,
      '金丸珠': 13.900677652,
      '闯王': 5.73730633552,
      '孤身': 10.1630080337,
      '元代': 7.09274270828,
      '非线性': 8.55834340001,
      '甄夫人': 12.8020653633,
      '而立': 8.83177344976,
      '汇率': 6.76658393078,
      '袁锦': 13.900677652,
      '可预测性': 10.642581114,
      '电热水壶': 13.900677652,
      '后放': 12.1089181827,
      '官晋爵': 12.8020653633,
      '神经衰弱': 9.98865464655,
      '掘': 8.53003962385,
      '查号': 13.900677652,
      '挣到': 10.4041700905,
      '褟': 9.30555780184,
      '二十余处': 12.8020653633,
      '养锐': 12.5143832909,
      '战斗能力': 11.1280889297,
      '栽插': 12.5143832909,
      '李亚': 10.8561552143,
      '史张腊': 13.2075304714,
      '绝对性': 10.9562386728,
      '政法委': 9.98865464655,
      '日积月累': 10.4666904475,
      '秒杀': 8.57766767284,
      '言之士': 12.8020653633,
      '不死不活': 11.7034530746,
      '博耶': 12.5143832909,
      '山药蛋': 12.5143832909,
      '鳖精': 13.900677652,
      '有用之才': 11.8212361103,
      '李岩惊': 13.900677652,
      '外币': 8.70772080109,
      '马雅': 13.900677652,
      '消息面': 8.11685246965,
      '金融债权': 12.8020653633,
      '丘伦梅': 13.900677652,
      '马鲁穆': 13.900677652,
      '棊': 12.8020653633,
      '鹑': 10.1871055853,
      '猛吃': 11.1926274509,
      '广南路': 13.2075304714,
      '乡土观念': 11.8212361103,
      '浩然之气': 12.8020653633,
      '太冲': 9.23723855786,
      '唐复名': 12.5143832909,
      '雷阵雨': 10.9562386728,
      '自外而内': 13.900677652,
      '亿千瓦': 9.33632946051,
      '师道尊严': 12.2912397395,
      '单家独户': 12.5143832909,
      '口出怨言': 11.1926274509,
      '外带': 10.6818018271,
      '石渠阁': 11.7034530746,
      '达生': 13.900677652,
      '滕哈': 13.2075304714,
      '二万二千八百七十七卷': 13.900677652,
      '寒露风': 12.1089181827,
      '卢峰': 12.2912397395,
      '尿素氮': 10.642581114,
      ...},
     'median_idf': 11.9547675029}



#### 可以通过加载自定义词典和自定义IDF文件，提高关键词抽取有效性


```python
idf_freq = tfidf.idf_freq
median_idf = tfidf.median_idf
print(median_idf)
idf_freq  
```

    11.9547675029
    




    {'劳动防护': 13.900677652,
     '生化学': 13.900677652,
     '奥萨贝尔': 13.900677652,
     '考察队员': 13.900677652,
     '岗上': 11.5027823792,
     '倒车档': 12.2912397395,
     '编译': 9.21854642485,
     '蝶泳': 11.1926274509,
     '外委': 11.8212361103,
     '故作高深': 11.9547675029,
     '尉遂成': 13.2075304714,
     '心源性': 11.1926274509,
     '现役军人': 10.642581114,
     '杜勃留': 13.2075304714,
     '包天笑': 13.900677652,
     '贾政陪': 13.2075304714,
     '托尔湾': 13.900677652,
     '多瓦': 12.5143832909,
     '多瓣': 13.900677652,
     '巴斯特尔': 11.598092559,
     '刘皇帝': 12.8020653633,
     '亚历山德罗夫': 13.2075304714,
     '社会公众': 8.90346537821,
     '五百份': 12.8020653633,
     '两点阈': 12.5143832909,
     '多瓶': 13.900677652,
     '冰天': 12.2912397395,
     '库布齐': 11.598092559,
     '龙川县': 12.8020653633,
     '银燕': 11.9547675029,
     '历史风貌': 11.8212361103,
     '信仰主义': 13.2075304714,
     '頷': 10.2897597393,
     '好色': 10.0088573539,
     '款款而行': 12.5143832909,
     '凳子': 8.36728816325,
     '二部': 9.93038573842,
     '卢巴': 12.1089181827,
     '五百五': 13.2075304714,
     '鳓': 11.0103058941,
     '畅叙': 11.598092559,
     '吴栅子': 13.2075304714,
     '智力竞赛': 13.900677652,
     '库邦': 13.2075304714,
     '非正义': 11.3357282945,
     '编订': 10.2897597393,
     '悲号': 12.8020653633,
     '陈庄搭': 13.2075304714,
     '二郎': 9.62401153296,
     '电光石火': 11.8212361103,
     '抢球': 11.9547675029,
     '南澳大利亚': 10.9562386728,
     '失散多年': 12.5143832909,
     '有理有据': 10.9562386728,
     '盈利': 5.72260018813,
     '弗龙堡': 13.900677652,
     '悚然': 10.604840786,
     '查吓': 13.2075304714,
     '滕县': 10.9049453784,
     '毛瑟枪': 12.2912397395,
     '好花': 11.2616203224,
     '潮州人': 13.900677652,
     '头羊': 11.5027823792,
     '提足': 12.5143832909,
     '书款': 12.2912397395,
     '嗤之以鼻': 10.642581114,
     '代金券': 11.9547675029,
     '公共财产': 11.4157710022,
     '文化素质': 10.765183436,
     '口称': 10.0505300503,
     '聚异丁烯': 12.1089181827,
     '终南山': 10.4349417492,
     '东安动力': 10.2630914922,
     '集训营': 13.2075304714,
     '截留': 9.94943393339,
     '热烈欢迎': 9.91169360541,
     '岗亭': 11.598092559,
     '浑球': 13.900677652,
     '让座': 10.4349417492,
     '迁户': 13.2075304714,
     '布尔热': 12.5143832909,
     '绣花针儿': 11.598092559,
     '二通': 11.8212361103,
     '滑雪运动': 11.7034530746,
     '程颢': 10.3743171274,
     '五百万': 10.9049453784,
     '旱荒': 12.5143832909,
     '标准线': 13.900677652,
     '时后梁': 12.2912397395,
     '外备': 12.5143832909,
     '绝对权': 13.2075304714,
     '蕉麻': 11.5027823792,
     '痎': 12.5143832909,
     '黎刹': 12.2912397395,
     '二十余年': 10.0720362555,
     '好苦': 10.8096351986,
     '镇心': 11.598092559,
     '残茬': 11.598092559,
     '从界岭': 12.1089181827,
     '湟': 10.2117981979,
     '国际经济组织': 11.8212361103,
     '五百两': 9.94943393339,
     '后手': 11.3357282945,
     '广播公司': 10.0720362555,
     '诞生地': 10.533381822,
     '二遍': 10.8561552143,
     '縌': 12.8020653633,
     '遂溪': 12.1089181827,
     '五百个': 10.8096351986,
     '不知高下': 13.900677652,
     '盈动': 11.9547675029,
     '程颐': 9.89334446674,
     '外头': 7.76079309975,
     '二道': 9.43476953332,
     '外夷': 11.0103058941,
     '喷洒车': 13.2075304714,
     '过会芳': 13.2075304714,
     '含金量': 9.72629038208,
     '外壁': 10.7226238216,
     '运猪': 13.900677652,
     '伶俐': 9.5186510173,
     '滑来滑去': 13.2075304714,
     '四轮驱动': 10.9562386728,
     '多病': 9.75754292558,
     '时至今日': 8.81308131674,
     '上': 2.52604920291,
     '卖火柴': 12.1089181827,
     '后接': 12.5143832909,
     '发射器': 8.52078029844,
     '迭宕': 13.900677652,
     '索尼': 9.6811699468,
     '鹿角霜': 12.8020653633,
     '双日': 11.5027823792,
     '用之不竭': 10.8561552143,
     '诊病': 11.1280889297,
     '职能': 6.70924832194,
     '军民联欢': 13.900677652,
     '周迥': 13.2075304714,
     '策源地': 10.5684731418,
     '后掌': 12.8020653633,
     '奸夫淫妇': 12.5143832909,
     '北五祖': 11.8212361103,
     '分析仪器': 11.0103058941,
     '加州大学': 11.1926274509,
     '服用者': 12.2912397395,
     '付出代价': 10.0505300503,
     '枯': 9.02548032877,
     '小兴安岭': 9.5186510173,
     '暴涨暴跌': 9.89334446674,
     '额窦': 12.5143832909,
     '库里': 10.2117981979,
     '和良渚': 12.5143832909,
     '后排': 8.81927328699,
     '张羽': 11.1280889297,
     '落脚点': 10.4349417492,
     '多会儿': 11.9547675029,
     '地动仪': 11.9547675029,
     '外境': 12.2912397395,
     '进贤县': 13.2075304714,
     '冰塔': 12.8020653633,
     '乳腺': 9.25628675283,
     '漆绘': 12.2912397395,
     '尤尔弗': 13.900677652,
     '岗位': 7.86519621945,
     '诊疗': 9.15574552361,
     '万公斤': 11.2616203224,
     '救下来': 11.7034530746,
     '折梅': 12.8020653633,
     '壑': 9.63799777493,
     '虎口脱险': 11.9547675029,
     '蜜蜂': 8.78868986362,
     '长角牛': 12.1089181827,
     '平滑肌': 9.4233408375,
     '外墙': 10.3743171274,
     '斯坦贝克': 11.4157710022,
     '后援': 10.8096351986,
     '多疑': 9.25628675283,
     '大水沟': 13.2075304714,
     '光机所': 13.900677652,
     '王治朝': 13.2075304714,
     '孤行': 12.5143832909,
     '诉讼法': 9.37888907493,
     '奥运会': 8.16733637508,
     '会合点': 11.7034530746,
     '票子': 9.48183704418,
     '二重': 10.0505300503,
     '声全息图': 13.900677652,
     '胡正卿': 12.1089181827,
     '教学进度': 13.900677652,
     '人证物证': 11.5027823792,
     '算进来': 12.8020653633,
     '积雨云': 11.0674643079,
     '人微言轻': 11.3357282945,
     '开路先锋': 11.3357282945,
     '董琬': 12.8020653633,
     '梁父吟': 12.2912397395,
     '两百二十册': 13.2075304714,
     '傅大人': 11.2616203224,
     '张家辉': 13.900677652,
     '百米': 9.02548032877,
     '连遭败绩': 12.8020653633,
     '暴发户': 9.87532596124,
     '多留': 10.0088573539,
     '分宜': 12.2912397395,
     '汝可先': 12.2912397395,
     '宇文泰和': 12.5143832909,
     '五百余': 10.4666904475,
     '寒潮': 9.05649056552,
     '大水池': 12.5143832909,
     '陈循': 13.900677652,
     '多番': 11.9547675029,
     '旱船': 11.7034530746,
     '十一名': 11.9547675029,
     '慢条斯理': 9.91169360541,
     '卢尔': 13.2075304714,
     '高低杠': 11.5027823792,
     '海西州': 13.2075304714,
     '官腔': 10.3743171274,
     '求贤若渴': 11.9547675029,
     '日喀则市': 11.4157710022,
     '多种营养': 12.2912397395,
     '新老交替': 13.2075304714,
     '手牵着': 11.0674643079,
     '书橱': 11.2616203224,
     '情郎': 11.7034530746,
     '江陵县': 10.4349417492,
     '通布卡': 13.900677652,
     '医药卫生': 10.2117981979,
     '渭川千亩': 13.900677652,
     '莫恰洛': 12.5143832909,
     '房舱': 13.2075304714,
     '冰壁': 10.4349417492,
     '焦庄户': 12.8020653633,
     '既想': 11.7034530746,
     '就业结构': 11.9547675029,
     '人类学': 8.81308131674,
     '潭州': 10.4666904475,
     '训练班': 9.71102290995,
     '骚动': 8.61241062128,
     '鸿业': 11.5027823792,
     '今年底': 8.78868986362,
     '好菜': 11.1280889297,
     '小亚丁': 13.900677652,
     '店伙': 12.8020653633,
     '马鞭': 9.66657114738,
     '高负荷': 13.900677652,
     '房舍': 8.96620371885,
     '悲剧': 7.55855623325,
     '缅甸': 7.81390292506,
     '泌尿器官': 13.900677652,
     '免罚': 13.900677652,
     '总商会': 11.4157710022,
     '口喊着': 13.2075304714,
     '截球': 13.2075304714,
     '最省': 12.1089181827,
     '减薪': 10.642581114,
     '辛丑和约': 12.2912397395,
     '外寇': 13.2075304714,
     '躲藏着': 12.5143832909,
     '浮来': 13.2075304714,
     '莫尔耶': 13.900677652,
     '撒手不管': 10.4994802703,
     '卢循': 12.1089181827,
     '垬': 7.63537643924,
     '枯木朽株': 13.900677652,
     '卢德': 12.1089181827,
     '多盘': 12.2912397395,
     '幽期密约': 13.900677652,
     '花生饼': 12.8020653633,
     '斯堪尼亚': 13.2075304714,
     '易中天': 13.2075304714,
     '左膀': 13.900677652,
     '多目': 12.8020653633,
     '郎咸平': 11.0103058941,
     '赏月': 10.0505300503,
     '寒威': 12.5143832909,
     '贺兰': 10.7226238216,
     '邪风': 12.5143832909,
     '好者': 13.900677652,
     '蒋御史': 13.900677652,
     '多相': 10.2630914922,
     '古观象台': 11.7034530746,
     '好耍': 11.0103058941,
     '老谋深算': 10.4041700905,
     '后悔': 7.32142643997,
     '游嬉恰': 13.900677652,
     '伤心落泪': 10.9049453784,
     '韩非则': 13.2075304714,
     '服用药': 13.2075304714,
     '格林卡': 11.5027823792,
     '正话': 10.8561552143,
     '叶碧秋': 8.49350588052,
     '姜丝排': 12.5143832909,
     '贺卡': 12.1089181827,
     '拖住': 9.21854642485,
     '悲凄': 11.0674643079,
     '葛翠琳': 13.900677652,
     '吴景超': 12.1089181827,
     '银灯': 13.2075304714,
     '悲凉': 9.35738286971,
     '睃': 9.91169360541,
     '外客': 12.1089181827,
     '外宣': 10.9049453784,
     '情报搜集': 11.598092559,
     '狗仔队': 13.2075304714,
     '裁汰': 10.7226238216,
     '践': 10.8561552143,
     '位于下面': 13.2075304714,
     '子禄父': 12.1089181827,
     '埃弗里': 12.5143832909,
     '乌尔斯': 13.2075304714,
     '外宾': 10.5684731418,
     '外宿': 13.900677652,
     '咱村': 9.96885201925,
     '从宽处理': 11.9547675029,
     '赊贷': 11.3357282945,
     '免纳': 11.7034530746,
     '蜕壳激素': 13.900677652,
     '表意文字': 12.1089181827,
     '趁心如意': 13.900677652,
     '悲叹': 10.604840786,
     '人所共知': 10.0088573539,
     '家电企业': 10.3743171274,
     '距离处': 11.9547675029,
     '风情万种': 10.8561552143,
     '外存': 12.5143832909,
     '外孙': 9.85762638414,
     '梅里威': 13.2075304714,
     '亚圣': 12.1089181827,
     '周至县': 11.5027823792,
     '采编部': 13.900677652,
     '怀特河': 13.2075304714,
     '外学': 11.7034530746,
     '马八儿': 12.2912397395,
     '圣路易斯': 10.2630914922,
     '合线期': 13.900677652,
     '凿井': 10.6818018271,
     '联贯性': 13.900677652,
     '冰室': 13.2075304714,
     '显身手': 12.5143832909,
     '后怕': 9.91169360541,
     '赏析': 12.1089181827,
     '瓦德希': 13.2075304714,
     '卢彦': 13.900677652,
     '切齿痛恨': 11.4157710022,
     '不惜一战': 13.900677652,
     '千百万': 10.0720362555,
     '战斗分队': 12.2912397395,
     '夜壶': 10.9562386728,
     '配': 8.11071748108,
     '古巴共和国': 13.2075304714,
     '缘薄': 13.900677652,
     '麦禾': 12.8020653633,
     '毋须': 11.5027823792,
     '测试者': 12.2912397395,
     '乌巢劫': 13.2075304714,
     '吃大户': 11.2616203224,
     '平城南': 13.900677652,
     '勠': 12.5143832909,
     '风风光光': 11.4157710022,
     '镇巴': 12.5143832909,
     '江三公子': 13.2075304714,
     '拨乱反正': 10.3171587135,
     '戒酒': 10.4349417492,
     '一千五百多名': 13.2075304714,
     '好胜': 11.5027823792,
     '多瘦': 13.2075304714,
     '最矮': 12.5143832909,
     '铺设': 8.68574189437,
     '最短': 9.28555713513,
     '标准粉': 13.2075304714,
     '折款': 13.900677652,
     '房脊': 11.598092559,
     '信奉者': 11.5027823792,
     '绝对数': 11.0674643079,
     '鸡冠花': 11.8212361103,
     '坏血酸': 13.900677652,
     '外嫁': 13.900677652,
     '萝北': 12.5143832909,
     '张泽咸': 12.2912397395,
     '空置率': 11.0674643079,
     '款洽': 13.900677652,
     '恩仇记': 13.2075304714,
     '拖上': 11.598092559,
     '拖下': 12.8020653633,
     '好脸': 13.2075304714,
     '投河自尽': 11.7034530746,
     '博蒙': 12.8020653633,
     '张高丽': 12.8020653633,
     '欢音': 12.8020653633,
     '方方正正': 10.8096351986,
     '私人教师': 11.7034530746,
     '医务部': 12.8020653633,
     '慢点': 10.6818018271,
     '马宅': 11.7034530746,
     '查哨': 11.8212361103,
     '零所': 13.2075304714,
     '钥': 10.3171587135,
     '海关检查': 12.5143832909,
     '弗雷泽': 11.598092559,
     '血糖仪': 12.2912397395,
     '民航机场': 11.598092559,
     '异端邪说': 11.8212361103,
     '既成': 11.0103058941,
     '吹风会': 11.0674643079,
     '霅': 13.900677652,
     '活字版': 11.9547675029,
     '阝': 11.9547675029,
     '黄风吹': 13.2075304714,
     '多石': 12.2912397395,
     '朴不花': 12.5143832909,
     '广南西': 11.5027823792,
     '叶祖': 11.1926274509,
     '姊妹花': 11.5027823792,
     '仉': 10.7226238216,
     '萝卜': 8.6803218269,
     '陇海路': 9.93038573842,
     '刁羊': 11.9547675029,
     '供办': 12.8020653633,
     '二千五百元': 13.900677652,
     '地图更新': 13.900677652,
     '天津市委': 10.9562386728,
     '三四百斤': 12.1089181827,
     '百忙之中': 10.9562386728,
     '没前途': 12.1089181827,
     '刑讯': 11.8212361103,
     '百级': 13.900677652,
     '镤': 12.5143832909,
     '高得幸': 13.2075304714,
     '受贿者': 12.2912397395,
     '普通住宅': 10.2117981979,
     '枪打出头鸟': 13.2075304714,
     '树皮画': 12.8020653633,
     '强弩之末': 10.1164880181,
     '铸造蜡': 13.900677652,
     '咽喉': 8.22392384971,
     '阮大人': 12.8020653633,
     '暴发性': 11.598092559,
     '保险制度': 10.7226238216,
     '另行通知': 12.2912397395,
     '韩世昌': 12.2912397395,
     '侈': 11.9547675029,
     '外套': 9.20932976975,
     '多着': 12.5143832909,
     '甏': 10.9049453784,
     '空穴': 10.1871055853,
     '扫黄办': 13.2075304714,
     '祖白圭': 12.8020653633,
     '公平交易': 9.69598503258,
     '牵过来': 11.8212361103,
     '刑警': 11.1280889297,
     '陈求发': 12.8020653633,
     '刡': 11.8212361103,
     '贾政问': 12.8020653633,
     '立体声': 10.642581114,
     '卢布': 9.62401153296,
     '智能网': 13.2075304714,
     '左臂': 9.31571017331,
     '娄室之': 13.2075304714,
     '卢帕': 13.2075304714,
     '杜若': 12.2912397395,
     '郭攸之': 12.5143832909,
     '兄友弟恭': 12.5143832909,
     '容星桥': 13.2075304714,
     '萨拉班': 12.8020653633,
     '下流无耻': 13.900677652,
     '桑德斯': 12.8020653633,
     '二人同心': 13.900677652,
     '文崔二': 12.5143832909,
     '自误': 11.8212361103,
     '多看': 9.75754292558,
     '宁王': 11.3357282945,
     '玉华王': 11.9547675029,
     '不饱和': 9.16447920358,
     '慢火': 11.598092559,
     '王秀兰': 12.8020653633,
     '书档': 13.2075304714,
     '耐压性': 13.900677652,
     '截瘫': 11.7034530746,
     '圥': 13.2075304714,
     '宁玛': 12.1089181827,
     '户主': 10.6818018271,
     '易舟浮': 13.2075304714,
     '穆然城': 13.2075304714,
     '对话会': 13.2075304714,
     '海蜇头': 13.900677652,
     '多眼': 11.1926274509,
     '轳': 13.900677652,
     '书案': 9.49395840471,
     '瓕': 11.7034530746,
     '握力': 13.2075304714,
     '书桌': 9.87532596124,
     '遮面': 13.2075304714,
     '内廷紫': 13.2075304714,
     '八节': 11.598092559,
     '袁姑爷': 10.4349417492,
     '零散': 9.33632946051,
     '编过': 12.5143832909,
     '国台办': 11.5027823792,
     '蓝孔雀': 13.2075304714,
     '库银': 13.900677652,
     '同翅目': 10.8096351986,
     '零数': 11.9547675029,
     '上海滩': 10.4666904475,
     '正表': 13.900677652,
     '黎国': 13.900677652,
     '电焊条': 12.8020653633,
     '二钱': 11.0674643079,
     '交通违章': 12.2912397395,
     '五卅运动': 10.0940151622,
     '贡二水': 12.8020653633,
     '傣': 9.55687223012,
     '蜜色': 13.900677652,
     '以远': 11.9547675029,
     '百科': 10.1630080337,
     '左舷': 12.1089181827,
     '新媳妇': 9.85762638414,
     '外差': 11.9547675029,
     '竞争性': 9.62401153296,
     '编述': 12.5143832909,
     '孤负': 12.5143832909,
     '百种': 9.61021821083,
     '杨炎官': 13.2075304714,
     '每下愈况': 13.900677652,
     '博莱': 12.2912397395,
     '少数整': 12.8020653633,
     '宗羲': 12.2912397395,
     '新疆省': 10.9049453784,
     '由近而远': 12.8020653633,
     '镇子': 9.28555713513,
     '丽丽': 9.87532596124,
     '靳祥': 12.8020653633,
     '类型学': 11.2616203224,
     '小象虫': 13.2075304714,
     '烈女传': 13.2075304714,
     '史志宏': 11.8212361103,
     '四十六次': 13.2075304714,
     '编辑': 6.28685896717,
     '黑白两道': 11.598092559,
     '交换条件': 11.0103058941,
     '立体式': 12.8020653633,
     '发射区': 11.8212361103,
     '广陵派': 13.2075304714,
     '卢姆': 12.1089181827,
     '国务院法制办': 11.1926274509,
     '租下来': 13.2075304714,
     '孪': 10.4994802703,
     '私生活': 10.533381822,
     '山竹子': 13.2075304714,
     '神使鬼差': 13.900677652,
     '卢世荣': 12.2912397395,
     '任姓挚': 13.2075304714,
     '试述': 13.900677652,
     '多点': 8.86372504956,
     '囷': 8.98802276624,
     '诱导酶': 13.900677652,
     '阿旃陀': 10.9049453784,
     '夏耘': 13.900677652,
     '王爵封': 13.2075304714,
     '哈飞公司': 13.2075304714,
     '院校': 8.81927328699,
     '养阴': 10.7226238216,
     '个性特点': 12.5143832909,
     '第十七个': 13.900677652,
     '第二十六章': 10.5684731418,
     '潘公凯': 13.900677652,
     '镇定': 8.37124856446,
     '争嘴': 13.900677652,
     '专题讲座': 12.2912397395,
     '女追男': 13.900677652,
     '镇宅': 11.4157710022,
     '感受一下': 11.3357282945,
     '零时': 9.14708746087,
     '资源税': 10.2117981979,
     '项怀诚': 12.8020653633,
     '谛': 9.98865464655,
     '王立武': 13.2075304714,
     '镇安': 10.4041700905,
     '镇守': 8.38724890581,
     '一筐': 10.7226238216,
     '够格': 12.5143832909,
     '昐': 11.3357282945,
     '脉动': 9.98865464655,
     '级别': 7.50541605386,
     '竟陵': 10.7226238216,
     '全国学联': 12.2912397395,
     '贺喜': 9.38981814546,
     '宝钗素': 12.2912397395,
     '多灾': 11.598092559,
     '萨克森': 9.45802639549,
     '杨国强': 13.2075304714,
     '几十艘': 13.900677652,
     '严防': 9.56994431169,
     '元老级': 11.8212361103,
     '票庄': 13.2075304714,
     '足球界': 11.8212361103,
     '洮南': 11.9547675029,
     '双力': 13.2075304714,
     '后景': 12.8020653633,
     '截然': 9.05649056552,
     '照耀': 8.67493097826,
     '来江州': 12.5143832909,
     '丽人': 11.1926274509,
     '用途林': 12.8020653633,
     '戒面': 13.900677652,
     '上海港': 10.2371160058,
     '昏昏欲睡': 10.6818018271,
     '八艘': 11.9547675029,
     '撸子': 12.8020653633,
     '开门见山': 9.59661255877,
     '觞': 11.8212361103,
     '卢奇': 12.1089181827,
     '慢着': 10.533381822,
     '欢送': 10.604840786,
     '不作美': 13.900677652,
     '斯海姆': 12.8020653633,
     '合作局': 13.2075304714,
     '良': 9.45802639549,
     '丽亚': 12.2912397395,
     '上海电影制片厂': 10.2630914922,
     '川东南': 11.598092559,
     '布特莱齐': 13.900677652,
     '拉栖第': 10.3743171274,
     '明铁盖': 12.2912397395,
     '主掌': 11.7034530746,
     '脱氧核糖核酸': 10.1164880181,
     '阿拉斯加': 9.13850371718,
     '乌孙王': 11.9547675029,
     '塑胶管': 12.8020653633,
     '落马洲': 13.2075304714,
     '历经沧桑': 12.5143832909,
     '羊背石': 11.4157710022,
     '姑父': 9.72629038208,
     '姑爹': 13.2075304714,
     '桂林人': 12.2912397395,
     '张廷玉': 11.0674643079,
     '二十余家': 12.5143832909,
     '玎珰': 13.900677652,
     '冰封': 9.77354326693,
     '四出戏': 13.900677652,
     '海蚀台': 13.2075304714,
     '群而不党': 13.900677652,
     '戚': 9.94943393339,
     '鲁比亚': 12.8020653633,
     '输送泵': 13.2075304714,
     '老街区': 13.2075304714,
     '千态万状': 13.900677652,
     '铭心镂骨': 12.5143832909,
     '查克': 12.2912397395,
     '陈女士': 10.4994802703,
     '达官显宦': 12.8020653633,
     '人才流': 13.900677652,
     '适量水': 13.2075304714,
     '黑娃': 8.0985592766,
     '光纤网': 13.900677652,
     '傲雪凌霜': 13.900677652,
     '潭头': 12.8020653633,
     '电抗器': 11.5027823792,
     '后果': 7.19748953873,
     '牛山湖': 12.8020653633,
     '警报系统': 11.9547675029,
     '为民除害': 10.765183436,
     '应明辨': 12.8020653633,
     '喝进去': 12.2912397395,
     '李老爷': 11.598092559,
     '寒冬腊月': 11.2616203224,
     '冰屑': 11.9547675029,
     '多媒体信息': 12.8020653633,
     '美国纽约大学': 11.1926274509,
     '非常容易': 10.0505300503,
     '解放军部队': 12.1089181827,
     '睌': 8.95903522937,
     '复旦大学': 8.79473217808,
     '冰层': 9.28555713513,
     '二间': 12.8020653633,
     '仪器仪表': 9.56994431169,
     '远亲近友': 13.2075304714,
     '变幻莫测': 10.4994802703,
     '劲风': 11.0103058941,
     '外岛': 12.2912397395,
     '厚脸皮': 13.900677652,
     '奥威尔': 12.8020653633,
     '信息处理': 9.43476953332,
     '冰山': 9.29550746599,
     '几十箱': 13.2075304714,
     '老少爷们儿': 13.2075304714,
     '贩贱卖贵': 13.900677652,
     '非她不可': 13.2075304714,
     '成仙成': 13.2075304714,
     '夏历': 9.71102290995,
     '最灵': 11.3357282945,
     '投资银行业': 12.8020653633,
     '四时之气': 13.900677652,
     '外层': 8.83808261895,
     '长春电影制片厂': 11.1926274509,
     '张维': 11.598092559,
     '李虞候': 11.7034530746,
     '上海大众': 9.34680076038,
     '冰岛': 9.12155415886,
     '过磷酸': 13.2075304714,
     '外屋': 10.642581114,
     '小角色': 12.1089181827,
     '默不作声': 10.0505300503,
     '服罪': 11.9547675029,
     '查出': 8.40350942668,
     '哑巴亏': 11.9547675029,
     '防雷击': 13.900677652,
     '雅鲁藏布江': 8.97342396682,
     '分清主次': 13.900677652,
     '混起': 13.900677652,
     '后有': 11.0674643079,
     '海瑞罢官': 11.0674643079,
     '中饱私囊': 11.4157710022,
     '尼科西亚': 12.1089181827,
     '朱三松': 12.5143832909,
     '后期': 6.18778669049,
     '瀹': 6.80478443088,
     '画眉鸟': 12.1089181827,
     '洞鉴': 12.2912397395,
     '刑赏': 11.8212361103,
     '宇文泰嗣': 12.8020653633,
     '和平解决': 9.32596667347,
     '中草药': 9.28555713513,
     '一站式': 10.0720362555,
     '不怕困难': 12.5143832909,
     '标准箱': 11.2616203224,
     '后来': 4.99211827683,
     '心细': 10.5684731418,
     '戒除': 10.9049453784,
     '八荒': 12.8020653633,
     '刑责': 12.5143832909,
     '电信业': 11.0103058941,
     '帅营': 13.900677652,
     '逗乐': 11.0103058941,
     '固溶体': 10.642581114,
     '玄稽沉': 13.2075304714,
     '情夫': 13.2075304714,
     '减色': 11.9547675029,
     '巴拉那': 11.7034530746,
     '明叔让': 12.5143832909,
     '冰峰': 12.2912397395,
     '最烦': 11.8212361103,
     '待命状态': 12.8020653633,
     '近红外': 11.0103058941,
     '李永芳': 12.2912397395,
     '闸阀': 11.9547675029,
     '快撤': 11.7034530746,
     '宗明昌': 12.8020653633,
     '最热': 8.73589167805,
     '森严壁垒': 13.900677652,
     '千岛群岛': 10.6818018271,
     '技艺': 8.0600359946,
     '激光管': 13.900677652,
     '相当规模': 9.82314020807,
     '极端愚蠢': 13.2075304714,
     '业务室': 13.2075304714,
     '诉讼案': 10.2897597393,
     '杨国平': 12.1089181827,
     '从乐亭': 13.900677652,
     '降霜': 13.900677652,
     '闸门': 9.28555713513,
     '静止': 7.98988100794,
     '几万倍': 12.2912397395,
     '悲喜': 11.2616203224,
     '氦氖激光器': 13.2075304714,
     '后撤': 9.40086798165,
     '既未': 11.5027823792,
     '帝斯': 13.900677652,
     '创立': 6.8787012289,
     '自投罗网': 10.3171587135,
     '二难': 11.4157710022,
     '统战部门': 13.900677652,
     '马小舍': 12.2912397395,
     '团服': 13.900677652,
     '内利斯': 11.598092559,
     '贾政道': 9.45802639549,
     '卢宅': 12.8020653633,
     '八股': 9.53122979951,
     '幻灯机': 12.5143832909,
     '背不住': 13.900677652,
     '中国人民解放军空军': 11.1926274509,
     '拔出去': 13.900677652,
     '王峰': 10.642581114,
     '外快': 10.7226238216,
     '四五千里': 13.2075304714,
     '既有': 7.11622058934,
     '宗社': 10.9049453784,
     '纻': 10.642581114,
     '百无一见': 13.900677652,
     '纯棉纱': 12.8020653633,
     '百篇': 10.9562386728,
     '从维熙': 12.8020653633,
     '斯宾诺': 13.900677652,
     '外径': 11.0674643079,
     '童大人': 11.0103058941,
     '市政建设': 10.3743171274,
     '猜谜': 11.1280889297,
     '当代人': 12.1089181827,
     '谄上欺下': 13.900677652,
     '宗祖': 12.8020653633,
     '神农本草经': 10.9049453784,
     '卡波济': 13.900677652,
     '骑马打仗': 11.3357282945,
     '梅斯基': 13.2075304714,
     '减至': 9.19114745066,
     '查到': 9.66657114738,
     '尼泊尔共产党': 13.2075304714,
     '卢寻': 13.2075304714,
     '另起炉灶': 11.2616203224,
     '不可理喻': 10.6818018271,
     '宗祠': 10.533381822,
     '零月': 13.2075304714,
     '未处理': 13.2075304714,
     '少尉': 9.85762638414,
     '情面': 10.2897597393,
     '政法干部': 12.5143832909,
     '高等学府': 9.37888907493,
     '懊悔无及': 12.8020653633,
     '马加比': 13.2075304714,
     '不安全感': 11.4157710022,
     '和启东': 13.2075304714,
     '米勒德': 12.8020653633,
     '民族乐器': 10.9049453784,
     '由合子': 13.2075304714,
     '查勤': 13.900677652,
     '中国篮协': 13.900677652,
     '慢用': 12.5143832909,
     '统战部长': 11.9547675029,
     '二阶': 10.2117981979,
     '韦奇伍': 13.900677652,
     '利润率': 7.2673592187,
     '岸线': 8.80692745117,
     '亿加元': 12.5143832909,
     '地广': 12.1089181827,
     '逆我者死': 13.900677652,
     '南泥湾': 11.1926274509,
     '缘自': 11.9547675029,
     '外形': 7.45178825783,
     '多数三项': 13.900677652,
     '汪若海': 11.4157710022,
     '中国人民解放军三军仪仗队': 12.2912397395,
     '特库蒂': 13.2075304714,
     '欢闹': 12.8020653633,
     '百等': 13.2075304714,
     '风信子': 12.5143832909,
     '查勘': 10.2897597393,
     '如法炮制': 11.0103058941,
     '二队': 10.642581114,
     '坛坛罐罐': 11.2616203224,
     '游览胜地': 8.83177344976,
     '博多湾': 13.900677652,
     '镇委': 12.2912397395,
     '日本东京证券交易所': 13.900677652,
     '从今以后': 9.4233408375,
     '我姐': 10.7226238216,
     '阿弥陀': 11.4157710022,
     '戊子': 13.2075304714,
     '金乌西坠': 12.8020653633,
     '埃努古': 13.900677652,
     '纯如': 13.900677652,
     '冰心': 10.4349417492,
     '姬宗周': 13.2075304714,
     '魏延领': 11.8212361103,
     '外引': 13.2075304714,
     '家电网': 12.1089181827,
     '待物': 13.900677652,
     '杭嘉和': 8.39534611604,
     '千百件': 13.900677652,
     '职蜂': 13.2075304714,
     '外弦': 13.2075304714,
     '悲啼': 11.0103058941,
     '耳边风': 12.5143832909,
     '旱芹': 13.900677652,
     '查办': 9.74179456862,
     '配在一起': 12.5143832909,
     '情韵': 11.598092559,
     '别难过': 11.2616203224,
     '外强': 11.7034530746,
     '文国庆': 11.3357282945,
     '大连市': 9.66657114738,
     '岸礁': 11.9547675029,
     '开发计划署': 13.900677652,
     '反省': 9.4233408375,
     '减肥': 8.30225569298,
     '向父皇': 12.8020653633,
     '宫太后': 10.0088573539,
     '工具书': 9.91169360541,
     '图尔卡纳湖': 12.8020653633,
     '后方': 7.57811241205,
     '血循环': 10.604840786,
     '提供方便': 10.5684731418,
     '百端': 11.598092559,
     '龙的传人': 13.900677652,
     '十五丈': 13.2075304714,
     '目标群体': 12.5143832909,
     '廊房头条': 13.2075304714,
     '多班': 13.2075304714,
     '莫泽尔': 13.900677652,
     '乳状物': 13.900677652,
     '凋残': 11.8212361103,
     '悲咽': 12.5143832909,
     '篾青': 13.900677652,
     '蜜腺': 10.533381822,
     '后文': 12.1089181827,
     '嫡子': 10.9049453784,
     '最爱': 8.77671367257,
     '外延': 8.87679713113,
     '嫡孙': 11.9547675029,
     '米字旗': 13.2075304714,
     '小团体': 11.2616203224,
     '最爽': 12.5143832909,
     '仡': 13.900677652,
     '正梳妆': 13.900677652,
     '指甲钳': 13.900677652,
     '借壳上市': 9.5062284973,
     '十大元帅': 13.900677652,
     '后日': 9.87532596124,
     '梦牵魂绕': 11.9547675029,
     '潭子': 12.5143832909,
     '拙': 10.2117981979,
     '带头羊': 13.900677652,
     '魏末': 11.5027823792,
     '鼎立': 10.0294766411,
     '书法': 7.8184587416,
     '掩其不备': 13.2075304714,
     '林网化': 11.598092559,
     '交流电路': 10.9049453784,
     '古定剑': 12.5143832909,
     '少私寡欲': 12.8020653633,
     '上课时数': 13.900677652,
     '具体化': 10.2897597393,
     '悲哭': 11.1926274509,
     '尖锐湿疣': 11.2616203224,
     '查字法': 13.900677652,
     '技能': 8.16733637508,
     '张勋遂': 12.8020653633,
     '冰库': 12.2912397395,
     '金丸珠': 13.900677652,
     '闯王': 5.73730633552,
     '孤身': 10.1630080337,
     '元代': 7.09274270828,
     '非线性': 8.55834340001,
     '甄夫人': 12.8020653633,
     '而立': 8.83177344976,
     '汇率': 6.76658393078,
     '袁锦': 13.900677652,
     '可预测性': 10.642581114,
     '电热水壶': 13.900677652,
     '后放': 12.1089181827,
     '官晋爵': 12.8020653633,
     '神经衰弱': 9.98865464655,
     '掘': 8.53003962385,
     '查号': 13.900677652,
     '挣到': 10.4041700905,
     '褟': 9.30555780184,
     '二十余处': 12.8020653633,
     '养锐': 12.5143832909,
     '战斗能力': 11.1280889297,
     '栽插': 12.5143832909,
     '李亚': 10.8561552143,
     '史张腊': 13.2075304714,
     '绝对性': 10.9562386728,
     '政法委': 9.98865464655,
     '日积月累': 10.4666904475,
     '秒杀': 8.57766767284,
     '言之士': 12.8020653633,
     '不死不活': 11.7034530746,
     '博耶': 12.5143832909,
     '山药蛋': 12.5143832909,
     '鳖精': 13.900677652,
     '有用之才': 11.8212361103,
     '李岩惊': 13.900677652,
     '外币': 8.70772080109,
     '马雅': 13.900677652,
     '消息面': 8.11685246965,
     '金融债权': 12.8020653633,
     '丘伦梅': 13.900677652,
     '马鲁穆': 13.900677652,
     '棊': 12.8020653633,
     '鹑': 10.1871055853,
     '猛吃': 11.1926274509,
     '广南路': 13.2075304714,
     '乡土观念': 11.8212361103,
     '浩然之气': 12.8020653633,
     '太冲': 9.23723855786,
     '唐复名': 12.5143832909,
     '雷阵雨': 10.9562386728,
     '自外而内': 13.900677652,
     '亿千瓦': 9.33632946051,
     '师道尊严': 12.2912397395,
     '单家独户': 12.5143832909,
     '口出怨言': 11.1926274509,
     '外带': 10.6818018271,
     '石渠阁': 11.7034530746,
     '达生': 13.900677652,
     '滕哈': 13.2075304714,
     '二万二千八百七十七卷': 13.900677652,
     '寒露风': 12.1089181827,
     '卢峰': 12.2912397395,
     '尿素氮': 10.642581114,
     ...}




```python
sentence = '中央空调系统包括制冷站，末端'
tfidf.extract_tags(sentence,withWeight=True)
```




    [('中央空调系统', 2.988691875725),
     ('制冷', 2.336700190095),
     ('末端', 2.0194079391225),
     ('包括', 1.0559129123075)]



### 2.2.2 基于Textrank提取关键词 ：jieba.analyse.textrank

#### 原理介绍见：
https://blog.csdn.net/qq_41664845/article/details/82869596

https://blog.csdn.net/qq_33373858/article/details/90810066

TextRank算法是由 Google 搜索的核心网页排序算法 PageRank 改编而来，利用图模型来提取文章中的关键词，首先介绍一下 PageRank 排序算法

### 一、PageRank 算法
![jupyter](https://img-blog.csdnimg.cn/20190604193542365.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMzczODU4,size_16,color_FFFFFF,t_70)

#### PageRank 算法是一种网页排名算法，其基本思想有两条：

    链接数量：一个网页被越多的其他网页链接，说明这个网页越重要。
    链接质量：一个网页被一个越高权值的网页链接，也能表明这个网页越重要。

![jupyter](https://img-blog.csdnimg.cn/20190530204915270.png)

* 其中V表示网页，S表示每个网页的score，S越大表示网页的重要程度越高。d是阻尼系数，一般取0.85

* In(V) 表示存在指向网页 i 的链接的网页集合。Out(V)表示网页 j 中的链接指向的网页的集合；|Out(V)| 是集合中元素的个数

* #### 在评价网页的重要性时，根据所有指向该网页 i 的网页 j 的重要性以及网页 j 中的链接指向的网页的数目。比如：一篇文章被许多权重高的网页指向，而且指向它的网页本身指出去的链接并不多，那这篇文章就十分重要，其得分就很高。（换句话来说，这篇文章被很多人借鉴，并且是唯一被引用的）

* 初始时，可以设置每个网页的重要性为 1，进行迭代。当S（V）的变化量小于阈值（0.0001）时停止迭代。

### 2、TextRank 算法

TextRank在构建图的时候将节点由网页改成了句子，并为节点之间的边引入了权值，其中权值表示两个句子的相似程度，本质上构建的是一个带权无向图，其计算公式如下：
![jupyter](https://img-blog.csdnimg.cn/20190604193622308.png)
![jupyter](https://img-blog.csdnimg.cn/20190604193604339.png)
在 TextRank 构建的图中，默认节点就是句子，权重 w_{ij} 为两个句子 S_{i} 和 S_{j} 的相似度分数，公式如下：
![jupyter](https://img-blog.csdnimg.cn/20190604193659990.png)

使用TextRank提取关键词,和网页中选哪个网页比较重要其实是异曲同工的，so，我们只需要想办法把图构建出来就好了。

图的结点其实比较好定义，就是单词喽，把文章拆成句子，每个句子再拆成单词，以单词为结点。

那么边如何定义呢？这里就可以利用n-gram的思路，简单来说，某个单词，只与它附近的n个单词有关，即与它附近的n个词对应的结点连一条无向边（两个有向边）。

另外，还可以做一些操作，比如把某类词性的词删掉，一些自定义词删掉，只保留一部分单词，只有这些词之间能够连边。

下面是论文中给出的例子：
![jupyter](https://img-blog.csdnimg.cn/20181104103703911.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FpYW45OQ==,size_16,color_FFFFFF,t_70)

##### 例如要从下面的文本中提取关键词：
![jupyter](https://img-blog.csdnimg.cn/20190604193726678.png)
1）对这句话分词，去掉里面的停用词
![jupyter](https://img-blog.csdnimg.cn/20190604193735347.png)
2）现在建立一个大小为 9 的窗口，即相当于每个单词要将票投给它身前身后距离 5 以内的单词：
![jupyter](https://img-blog.csdnimg.cn/20190604193744939.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMzczODU4,size_16,color_FFFFFF,t_70)
然后开始迭代投票，直至收敛：
![jupyter](https://img-blog.csdnimg.cn/20190604193753354.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMzMzczODU4,size_16,color_FFFFFF,t_70)
可以看到“程序员”的得票数最多，因而它是整段文本最重要的单词，我们将文本中得票数多的若干单词作为该段文本的关键词。

#### Jieba分词TextRank：
https://blog.csdn.net/qq_41664845/article/details/82869596

* 对每个句子进行分词和词性标注处理
* 过滤掉除指定词性外的其他单词，过滤掉出现在停用词表的单词，过滤掉长度小于2的单词
* 将剩下的单词中循环选择一个单词，将其与其后面4个单词分别组合成4条边。

例如：

['有','媒体', '曝光','高圆圆', '和', '赵又廷','现身', '台北', '桃园','机场','的', '照片']

对于‘媒体‘这个单词，就有（'媒体', '曝光'）、（'媒体', '高圆圆'）、（'媒体', '和'）、（'媒体', '赵又廷'）4条边，且每条边权值为1，当这条边在之后再次出现时，权值再在基础上加1.

有了这些数据后，我们就可以构建出候选关键词图，把2个单词组成的边，和其权值记录了下来。

这样我们就可以套用TextRank的公式，迭代传播各节点的权值，直至收敛。

对结果中的Rank值进行倒序排序，筛选出前面的几个单词，就是我们需要的关键词了。

    def textrank(self, sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'), withFlag=False):
 
        self.pos_filt = frozenset(allowPOS)
        # 定义无向有权图
        g = UndirectWeightedGraph()
        # 定义共现词典
        cm = defaultdict(int)
        # 分词
        words = tuple(self.tokenizer.cut(sentence))
        # 依次遍历每个词
        for i, wp in enumerate(words):
            # 词i 满足过滤条件
            if self.pairfilter(wp):
                # 依次遍历词i 之后窗口范围内的词
                for j in xrange(i + 1, i + self.span):
                    # 词j 不能超出整个句子
                    if j >= len(words):
                        break
                    # 词j不满足过滤条件，则跳过
                    if not self.pairfilter(words[j]):
                        continue
                    # 将词i和词j作为key，出现的次数作为value，添加到共现词典中
                    if allowPOS and withFlag:
                        cm[(wp, words[j])] += 1
                    else:
                        cm[(wp.word, words[j].word)] += 1
        # 依次遍历共现词典的每个元素，将词i，词j作为一条边起始点和终止点，共现的次数作为边的权重
        for terms, w in cm.items():
            g.addEdge(terms[0], terms[1], w)

        # 运行textrank算法
        nodes_rank = g.rank()

        # 根据指标值进行排序
        if withWeight:
            tags = sorted(nodes_rank.items(), key=itemgetter(1), reverse=True)
        else:
            tags = sorted(nodes_rank, key=nodes_rank.__getitem__, reverse=True)

        # 输出topK个词作为关键词
        if topK:
            return tags[:topK]
        else:
            return tags

#### 关于有向图的数据结构：
    def addEdge(self, start, end, weight):
        # use a tuple (start, end, weight) instead of a Edge object
        self.graph[start].append((start, end, weight))
        self.graph[end].append((end, start, weight))

#### rank实现：
      def rank(self):
        #yan:暴露ws出来
        self.ws = defaultdict(float)
        outSum = defaultdict(float)

        wsdef = 1.0 / (len(self.graph) or 1.0)
        for n, out in self.graph.items():
            self.ws[n] = wsdef
            outSum[n] = sum((e[2] for e in out), 0.0)

        # this line for build stable iteration
        sorted_keys = sorted(self.graph.keys())
        for x in xrange(10):  # 10 iters
            #yan:
            print('迭代轮次:',x)
            for n in sorted_keys:
                s = 0
                #graph:
                #{'了解': [('了解', '时候', 1)],
                #    '时候': [('时候', '了解', 1), ('时候', '参考', 1)],
![jupyter](https://img-blog.csdnimg.cn/20190604193622308.png)
“在评价网页的重要性时，根据所有指向该网页 i 的网页 j 的重要性以及网页 j 中的链接指向的网页的数目。比如：一篇文章被许多权重高的网页指向，而且指向它的网页本身指出去的链接并不多，那这篇文章就十分重要，其得分就很高。（换句话来说，这篇文章被很多人借鉴，并且是唯一被引用的）”

                for e in self.graph[n]:
                    s += e[2] / outSum[e[1]] * self.ws[e[1]]
                self.ws[n] = (1 - self.d) + self.d * s
                #yan：
                print("(n, self.ws[n]):",n,self.ws[n])

        (min_rank, max_rank) = (sys.float_info[0], sys.float_info[3])

        # 获取权值的最大值和最小值
        for w in itervalues(ws):
            if w < min_rank:
                min_rank = w
            if w > max_rank:
                max_rank = w

        # 对权值进行归一化
        for n, w in ws.items():
            # to unify the weights, don't *100.
            ws[n] = (w - min_rank / 10.0) / (max_rank - min_rank / 10.0)

        return ws


```python
from jieba.analyse.textrank import UndirectWeightedGraph,TextRank
```


```python
undirectWeightedGraph = UndirectWeightedGraph()
undirectWeightedGraph.__dict__
```




    {'graph': defaultdict(list, {})}




```python
sentence=' 上山打猎，下河摸鱼，打猎山上，摸鱼下河，这就是野外生存节目一贯套路。'
```


```python
textrank = TextRank()
textrank.__dict__
```




    {'tokenizer': <POSTokenizer tokenizer=<Tokenizer dictionary=None>>,
     'postokenizer': <POSTokenizer tokenizer=<Tokenizer dictionary=None>>,
     'stop_words': {'all',
      'an',
      'and',
      'are',
      'as',
      'at',
      'be',
      'by',
      'can',
      'for',
      'from',
      'has',
      'have',
      'if',
      'in',
      'is',
      'it',
      'not',
      'of',
      'on',
      'one',
      'or',
      'that',
      'the',
      'then',
      'this',
      'to',
      'we',
      'which',
      'with',
      'you'},
     'pos_filt': frozenset({'n', 'ns', 'v', 'vn'}),
     'span': 5}




```python
textrank.textrank(sentence, withWeight=True)
```

    迭代轮次: 0
    (n, self.ws[n]): 上山 0.2078231292517007
    (n, self.ws[n]): 下河 0.30140022675736966
    (n, self.ws[n]): 套路 0.27142857142857146
    (n, self.ws[n]): 打猎 0.39769260204081636
    (n, self.ws[n]): 摸鱼 0.43915368446981967
    (n, self.ws[n]): 生存 0.32607142857142857
    (n, self.ws[n]): 节目 0.4039375
    迭代轮次: 1
    (n, self.ws[n]): 上山 0.30320304862404623
    (n, self.ws[n]): 下河 0.5052081413105116
    (n, self.ws[n]): 套路 0.4602537946428572
    (n, self.ws[n]): 打猎 0.6372613064001207
    (n, self.ws[n]): 摸鱼 0.6111950273367401
    (n, self.ws[n]): 生存 0.5172813002232143
    (n, self.ws[n]): 节目 0.5654524153180804
    迭代轮次: 2
    (n, self.ws[n]): 上山 0.3855388456212325
    (n, self.ws[n]): 下河 0.6645531208600409
    (n, self.ws[n]): 套路 0.6101618291050503
    (n, self.ws[n]): 打猎 0.8014289692429811
    (n, self.ws[n]): 摸鱼 0.7394751816796372
    (n, self.ws[n]): 生存 0.6496360538798306
    (n, self.ws[n]): 节目 0.6854141002685744
    迭代轮次: 3
    (n, self.ws[n]): 上山 0.44622038436310213
    (n, self.ws[n]): 下河 0.7778962015553859
    (n, self.ws[n]): 套路 0.7173963155130721
    (n, self.ws[n]): 打猎 0.9213119467777637
    (n, self.ws[n]): 摸鱼 0.8324538132888046
    (n, self.ws[n]): 生存 0.7461944267071998
    (n, self.ws[n]): 节目 0.7720260654436155
    迭代轮次: 4
    (n, self.ws[n]): 上山 0.4900065123068935
    (n, self.ws[n]): 下河 0.8603178728640142
    (n, self.ws[n]): 套路 0.7952437091640965
    (n, self.ws[n]): 打猎 1.008263145101901
    (n, self.ws[n]): 摸鱼 0.8998877691331639
    (n, self.ws[n]): 生存 0.8160896542082776
    (n, self.ws[n]): 节目 0.834816679433259
    迭代轮次: 5
    (n, self.ws[n]): 上山 0.5217944192834025
    (n, self.ws[n]): 下河 0.9201058133861005
    (n, self.ws[n]): 套路 0.851635191797653
    (n, self.ws[n]): 打猎 1.0713390247009849
    (n, self.ws[n]): 摸鱼 0.9488119011117178
    (n, self.ws[n]): 生存 0.8667420452731376
    (n, self.ws[n]): 节目 0.880310325755086
    迭代轮次: 6
    (n, self.ws[n]): 上山 0.5448545101723106
    (n, self.ws[n]): 下河 0.9634789850525
    (n, self.ws[n]): 套路 0.8924972576869951
    (n, self.ws[n]): 打猎 1.117099071168614
    (n, self.ws[n]): 摸鱼 0.9843043900489296
    (n, self.ws[n]): 生存 0.9034432229628845
    (n, self.ws[n]): 节目 0.9132747042761988
    迭代轮次: 7
    (n, self.ws[n]): 上山 0.561583722495558
    (n, self.ws[n]): 下河 0.9949448649561714
    (n, self.ws[n]): 套路 0.9221051190766104
    (n, self.ws[n]): 打猎 1.150296321417576
    (n, self.ws[n]): 摸鱼 1.0100529501991544
    (n, self.ws[n]): 生存 0.9300364249249439
    (n, self.ws[n]): 节目 0.9371601562006606
    迭代轮次: 8
    (n, self.ws[n]): 上山 0.5737201961762816
    (n, self.ws[n]): 下河 1.0177722418942048
    (n, self.ws[n]): 套路 0.9435585469783818
    (n, self.ws[n]): 打猎 1.1743797622229573
    (n, self.ws[n]): 摸鱼 1.0287326279773816
    (n, self.ws[n]): 生存 0.949305448851093
    (n, self.ws[n]): 节目 0.9544671982275268
    迭代轮次: 9
    (n, self.ws[n]): 上山 0.5825247800731672
    (n, self.ws[n]): 下河 1.034332702805066
    (n, self.ws[n]): 套路 0.9591033750084135
    (n, self.ws[n]): 打猎 1.1918514532699378
    (n, self.ws[n]): 摸鱼 1.0422840781257388
    (n, self.ws[n]): 生存 0.9632674936252746
    (n, self.ws[n]): 节目 0.9670076191693174
    




    [('打猎', 1.0),
     ('摸鱼', 0.8680597121133171),
     ('下河', 0.8610454367882793),
     ('节目', 0.8016548717781519),
     ('生存', 0.7983555343354938),
     ('套路', 0.7946821730254269),
     ('上山', 0.46248480592035845)]



改造TextRank中的textrank方法，将g= UndirectWeightedGraph()暴露出来,

改造UndirectWeightedGraph.rank中的ws，将其暴露出来


```python
textrank.g
```




    <jieba.analyse.textrank.UndirectWeightedGraph at 0x1c1c0291308>




```python
textrank.g.graph
```




    defaultdict(list,
                {'上山': [('上山', '打猎', 1), ('上山', '下河', 1), ('上山', '摸鱼', 1)],
                 '打猎': [('打猎', '上山', 1),
                  ('打猎', '下河', 2),
                  ('打猎', '摸鱼', 2),
                  ('打猎', '下河', 1),
                  ('打猎', '摸鱼', 1)],
                 '下河': [('下河', '上山', 1),
                  ('下河', '打猎', 2),
                  ('下河', '摸鱼', 1),
                  ('下河', '打猎', 1),
                  ('下河', '摸鱼', 1)],
                 '摸鱼': [('摸鱼', '上山', 1),
                  ('摸鱼', '打猎', 2),
                  ('摸鱼', '下河', 1),
                  ('摸鱼', '打猎', 1),
                  ('摸鱼', '下河', 1)],
                 '生存': [('生存', '节目', 1), ('生存', '套路', 1)],
                 '节目': [('节目', '生存', 1), ('节目', '套路', 1)],
                 '套路': [('套路', '生存', 1), ('套路', '节目', 1)]})




```python
textrank.cm
```




    defaultdict(int,
                {('上山', '打猎'): 1,
                 ('上山', '下河'): 1,
                 ('上山', '摸鱼'): 1,
                 ('打猎', '下河'): 2,
                 ('打猎', '摸鱼'): 2,
                 ('下河', '摸鱼'): 1,
                 ('下河', '打猎'): 1,
                 ('摸鱼', '打猎'): 1,
                 ('摸鱼', '下河'): 1,
                 ('生存', '节目'): 1,
                 ('生存', '套路'): 1,
                 ('节目', '套路'): 1})




```python
textrank.g.ws
```




    defaultdict(float,
                {'上山': 0.46248480592035845,
                 '打猎': 1.0,
                 '下河': 0.8610454367882793,
                 '摸鱼': 0.8680597121133171,
                 '生存': 0.7983555343354938,
                 '节目': 0.8016548717781519,
                 '套路': 0.7946821730254269})


