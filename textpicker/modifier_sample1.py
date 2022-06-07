import pandas as pd
import os
import re


### text_sample1.csv 파일을 읽어 해당 텍스트로 치환
### 폴더명 수정
folder = "sample1"
### 추출하고자 하는 문자열
string = " 1 string storyText = "


text_sample1 = pd.read_csv('text_sample1.csv', encoding='utf-8') 

for i in text_sample1['file']:

    f1 = open(os.path.join(folder, i), 'r')
    f2 = open(os.path.join(folder + "_modified", i), 'w')
    while True:
        line = f1.readline()
        if line.startswith(" 1 string storyText = "):
            str = text_sample1['text'].loc[text_sample1['file'] == i].values[0]
            f2.write(string + "\"{}\"\n".format(str))
        else:
            f2.write(line)

        if not line:
            break
    f2.close()
    f1.close()
  
  

    
