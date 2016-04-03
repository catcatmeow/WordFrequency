#encoding=utf-8
from __future__ import print_function, unicode_literals
import sys
sys.path.append("../")
import jieba
jieba.load_userdict("userdict.txt")


def getText(path):
    filename=open(path)
    txt=filename.readlines()
    return txt

def cutWordss(txt):
    wordlist=[]
    for line in txt:
        test_sent = (line)
        words = jieba.lcut(test_sent)
#         print(words)        
        wordlist=wordlist+words
            
    return wordlist
              
def countWords(wordlist):
    a = {}                         #定义空字典
    for i in wordlist:
        if wordlist.count(i)>1:
            a[i] = wordlist.count(i)     #字典a，，key是list1内的项，value是统计此项出现的次数
    print("去重后共有%s 个单词：" % len(a))
    return a


####按照词频数排序  

def sortFrequency(statistic):
    statistic_sort= sorted(statistic.iteritems(), key=lambda d:d[1], reverse = True)
    for i in range(0,len(statistic_sort)):
        print(statistic_sort[i][0],statistic_sort[i][1])
        
    
              
              
dicPATH='./emuchdict.txt'
filePATH='./testFile.txt'
fechedtxt=getText(filePATH)
jieba.add_word('讨论咨询')
####开始将输入的文件字符串进行分词，结果存放于fechedwords列表里
fechedwords=cutWordss(fechedtxt)
print("本次共切分 %s 个单词" % len(fechedwords))

print("\n" + "="*40)

####将切好的分词进行词频统计，以 单词：次数 的键值对存放于statistic词典中。     
statistic=countWords(fechedwords)
###打印统计好的词频
# statistic_keys=statistic.keys()
# for x in statistic_keys:
#     print(x,statistic.get(x))
#####排序并打印
sortFrequency(statistic)

    


 






