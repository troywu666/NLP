'''
@Description: 
@Version: 1.0
@Autor: Troy Wu
@Date: 2020-06-27 22:27:55
@LastEditors: Troy Wu
@LastEditTime: 2020-06-27 22:37:03
'''
import jieba

# 分词
sent = '中文分词是文本处理不可或缺的一步！'
seg_list = jieba.cut(sent, cut_all = True)
print('全模式：', '/'.join(seg_list))
seg_list = jieba.cut(sent, cut_all = False)#也是默认模式
print('精确模型：', '/'.join(seg_list))
seg_list = jieba.cut_for_search(sent)
print('搜索引擎模式：', '/'.join(seg_list))