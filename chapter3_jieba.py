'''
@Description: 
@Version: 1.0
@Autor: Troy Wu
@Date: 2020-06-27 22:27:55
@LastEditors: Troy Wu
@LastEditTime: 2020-06-28 17:43:28
'''
import jieba
import glob
import random
import jieba.posseg as psg
import re
from datetime import datetime, timedelta
from dateutil.parser import parse

# 分词
sent = '中文分词是文本处理不可或缺的一步！'
seg_list = jieba.cut(sent, cut_all = True)
print('全模式：', '/'.join(seg_list))
seg_list = jieba.cut(sent, cut_all = False)#也是默认模式
print('精确模型：', '/'.join(seg_list))
seg_list = jieba.cut_for_search(sent)
print('搜索引擎模式：', '/'.join(seg_list))

# 高频词提取和去除常见停用词
def get_content(path):
    with open(path, 'r', encoding = 'gbk', errors = 'ignore') as f:
        content = ''
        for l in f:
            l = l.strip()
            content += l
        return content

def get_TF(words, topK = 10):
    tf_dic = {}
    for w in words:
        tf_dic[w] = tf_dic.get(w, 0) + 1
    return sorted(tf_dic.items(), key = lambda x: x[1], reverse = True)[: topK]

def stop_words(path):
    with open(path, encoding = 'utf8') as f:
        return [l.strip() for l in f]

files = glob.glob('D:/troywu666/personal_stuff/learning-nlp-master/chapter-3/data/news/C000013/*.txt')
corpus = [get_content(x) for x in files]
sample_inx = random.randint(0, len(corpus))
split_words = [x for x in jieba.cut(corpus[sample_inx]) if x not in stop_words(r'D:/troywu666/personal_stuff/learning-nlp-master/chapter-3/data\stop_words.utf8')]
print('样本之一：', corpus[sample_inx])
print('样本分词效果：', '/'.join(split_words))
print('样本的topK（10）词：', get_TF(split_words))

# 词性标注
sent = '中文分词是文本处理不可或缺的一步！'
seg_list = psg.cut(sent)
print(' '.join([r'{0}\{1}'.format(w, t) for w, t in seg_list]))

# 命名实体识别
## 日期识别


def time_extract(text):
    time_res = []
    word = ''
    keyDate = {'今天': 0, '明天': 1, '后天': 2}
    for k, v in psg.cut(text):
        if word != '':
            time_res.append(word)
            word = (datetime.today() + timedelta(days = keyDate.get(k, 0))).strftime('%Y年%m月%d日')
        elif word != '':
            if v in ['m', 't']:
                word = word + k
            else:
                time_res.append(word)
                word = ''
        elif v in ['m', 't']:
            word = k
    if word != '':
        time_res.append(word)
    result = list(filter(lambda x: x is not None, [check_time_valid(w) for w in time_res]))
    final_res = [parse_datetime(w) for w in result]

    return [x for x in final_res if x is not None]
