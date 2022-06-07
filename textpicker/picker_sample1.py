import pandas as pd
import os
import re



### 폴더 sample1 내의 텍스트 파일을 읽어 1 string storyText 행 추출.

### 폴더명 수정
folder = "sample1"
### 추출하고자 하는 문자열
string = " 1 string storyText = "
text = pd.read_csv('text.csv')
for filename in os.listdir(folder):
    if filename == '.DS_Store':
        continue
    with open(os.path.join(folder, filename), 'r') as f:
        for i in f:
            if i.startswith(string):
                text = text.append({'file':filename, 'text':re.findall(r'"(.*?)"', i)[0]}, ignore_index=True)
text.sort_values(by=['file'], inplace=True)
text.to_csv('text_sample1.csv', index=False, encoding='utf-8') ### 추출해서 저장할 csv 파일