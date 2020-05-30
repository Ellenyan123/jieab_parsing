import sys
sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser

USAGE = "usage:    python extract_tags.py [file name] -k [top k]"

parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
opt, args = parser.parse_args()


if len(args) < 1:
    print(USAGE)
    sys.exit(1)

file_name = args[0]

if opt.topK is None:
    topK = 10
else:
    topK = int(opt.topK)

content = open(file_name, 'rb').read()
#%%严 https://github.com/fxsjy/jieba
#基于TF-IDF提取关键词
sent = '基于前缀词典实现高效的词图扫描，生成句子中汉字所有可能成词情况所构成的有向无环图'
sent = sent.encode(encoding='utf-8')
tags = jieba.analyse.extract_tags(sent, topK=10, withWeight=True)

print(",".join(tags))

#关键词提取所使用逆向文件频率（IDF）文本语料库可以切换成自定义语料库的路径
jieba.analyse.set_idf_path("../extra_dict/idf.txt.big");
tags = jieba.analyse.extract_tags(sent, topK=10, withWeight=True)
print(tags)

#关键词提取所使用停止词（Stop Words）文本语料库可以切换成自定义语料库的路径
jieba.analyse.set_stop_words("../extra_dict/stop_words.txt")
jieba.analyse.set_idf_path("../extra_dict/idf.txt.big");
tags = jieba.analyse.extract_tags(sent, topK=10, withWeight=True)
print(tags)
#%%基于 TextRank 算法的关键词抽取  ！！！
jieba.analyse.textrank(sent,topK=10, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))

sent = '这是为什么，一切都不如意'
words = '/'.join(jieba.cut(sent))
words
import jieba.posseg as pseg
for s in pseg.cut(sent):
    print(s.word, s.flag)

sent = '如果打中将可以完成任务'
words = '/'.join(jieba.cut(sent))
words
jieba.suggest_freq('中将 ', True)
words = '/'.join(jieba.cut(sent))












