'''
@Description: 
@Version: 1.0
@Autor: Troy Wu
@Date: 2020-06-24 17:18:07
@LastEditors: Troy Wu
@LastEditTime: 2020-06-24 18:06:35
'''
# 逆向最大匹配
class IMM:
    def __init__(self, dic_path):
        self.dictionary = set()
        self.maximum = 0
        # 读取词典
        with open(dic_path, 'r', encoding = 'utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                self.dictionary.add(line)
                if len(line) > self.maximum:
                    self.maximum = len(line)
    
    def cut(self, text):
        result = []
        index = len(text)
        while index > 0:
            word = None
            for size in range(self.maximum, 0, -1):
                if index - size < 0:
                    continue
                piece = text[(index - size): index]
                if piece in self.dictionary:
                    word = piece
                    result.append(word)
                    index -= size
                    break
            if word is None:
                index -= 1
        return result[::-1]

if __name__ == '__main__':
    text = '南京市长江大桥'
    tokenizer = IMM('./data/imm_dic.utf8')
    print(tokenizer.cut(text))