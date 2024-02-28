import streamlit as st
import time

st.title("Streamlit　超入門")

st.write("プログレスバーの表示")
"Staryt!!"

larest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    larest_interation.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"DONE!!"






left_column, right_column = st.columns(2)
button = left_column.button("右カラムの文字を表示")

if button:
    right_column.write("ここは右カラム")

expander1 = st.expander("問い合わせ１")
expander1.write("問い合わせ１内容を書く")
expander2 = st.expander("問い合わせ２")
expander2.write("問い合わせ2内容を書く")
expander3 = st.expander("問い合わせ３")
expander3.write("問い合わせ３内容を書く")
# text = st.text_input("あなたの趣味を教えてください")


# condition = st.slider("あなたの飯間の調子は",0,100,50)

# "あなたの好きな趣味は",text,"です"
# "コンディション", condition
# if st.checkbox("Show Image"):
#     img = Image.open("onepiece01_luffy.png")
#     st.image(img, caption="ルフィ",use_column_width=True)
# df = pd.DataFrame(
#     np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
#     columns=["lat", "lon"]
# )

# st.map(df)

# st.dataframe(df, width=100, height=100)
# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```


# """