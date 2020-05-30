#encoding=utf-8
from __future__ import print_function, unicode_literals
#==============================================================================
# import nltk  严
# sentence = """At eight o'clock on Thursday morning  Arthur didn't feel very good."""
# tokens = nltk.word_tokenize(sentence)
# tagged = nltk.pos_tag(tokens)
# nltk.ne_chunk(tagged)
#==============================================================================

import sys
sys.path.append("../")
import jieba
jieba.load_userdict("userdict.txt")
import jieba.posseg as pseg

jieba.add_word('石墨烯')
jieba.add_word('凱特琳')
jieba.del_word('自定义词')

test_sent = (
"李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
"例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
"「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。"
)
words = jieba.cut(test_sent)
print('/'.join(words))

print("="*40)

result = pseg.cut(test_sent)

for w in result:
    print(w.word, "/", w.flag, ", ", end=' ') #和nltk中类似？

print("\n" + "="*40)

terms = jieba.cut('easy_install is great')
print('/'.join(terms))
terms = jieba.cut('python 的正则表达式是好用的')
print('/'.join(terms))

print("="*40)
# test frequency tune
testlist = [
('今天天气不错', ('今天', '天气')),
('如果放到post中将出错。', ('中', '将')),  #
('我们中出了一个叛徒', ('中', '出')),
]

for sent, seg in testlist:
    print('/'.join(jieba.cut(sent, HMM=False)))
    word = ''.join(seg)
    print('%s Before: %s, After: %s' % (word, jieba.get_FREQ(word), jieba.suggest_freq(seg, True)))
    print('/'.join(jieba.cut(sent, HMM=False)))
    print("-"*40)

'''
调整词典
使用 add_word(word, freq=None, tag=None) 和 del_word(word) 可在程序中动态修改词典。

使用 suggest_freq(segment, tune=True) 可调节单个词语的词频，使其能（或不能）被分出来。 ?这是自动的吗？？
tune : If True, tune the word frequency.

注意：自动计算的词频在使用 HMM 新词发现功能时可能无效。

>>> print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
如果/放到/post/中将/出错/。
>>> jieba.suggest_freq(('中', '将'), True)
494
>>> print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
如果/放到/post/中/将/出错/。
>>> print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))
「/台/中/」/正确/应该/不会/被/切开
>>> jieba.suggest_freq('台中', True)
69
>>> print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))
「/台中/」/正确/应该/不会/被/切开
'''
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))

jieba.suggest_freq(('台','中'), True)   #68  #通过调整使其分开
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False))) #通过调整使其分开

jieba.suggest_freq('台中', True)                                   #通过调整使其分开，使其合并！！！
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))

