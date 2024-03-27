import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門')
st.write('DataFrame')

df = pd.DataFrame({
'1列目' : [1,2,3,4],
'2列目' : [10,20,30,40]
}
)
st.write(df)
 
st.dataframe(df.style.highlight_max(axis=0), width=200,height=200)
 
st.table(df.style.highlight_max(axis=0))

#ダブルクォーテーション3つでマークダウンが使える
 
"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""
 

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] +[35.69,139.70],
    columns=['lat','lon']
 )


st.map(df)

img = Image.open('sample.png')
st.image(img,caption='fukuishiho',use_column_width=
'true')


st.title('Streamlit 門')
 
st.write('Display Image')
 
# -----------------------------------
if st.checkbox('show image'):
 
    img = Image.open('C:/Users/hukui/Documents/streamlit/sample.PNG')
    #ブラウザの横幅に合わせるuse_column_width
    st.image(img, caption='aiueo',use_column_width='true')
 
# -----------------------------------
option = st.selectbox(
    'あなたが好きな数字を教えて下さい。',
    list(range(1,11))
)
'あなたの好きな数字は、', option, 'です。'
 
# -----------------------------------
st.write('Interactive Widgets')
#text_areaは複数行入力
option = st.text_input('あなたの趣味を教えてい下さい。')
'あなたの趣味は', option, 'です。'
 
left_column, right_colunm = st.columns(2)

left_column.button('右から有無に文字を表示')

text = st.text_input('あなたの趣味を教えて下さい。：')
'あなたの趣味は', text, 'です。'

condition = st.sidebar.slider('あなたの今の調整は？',0,100,50)
'コンディション',condition


#2カラムレイアウト


st.title ('Streamlit 超入門')
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    print(i)
    time.sleep(0.1)