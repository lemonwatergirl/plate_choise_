import numbers
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# サイドバーの幅を調節
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 400px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 500px;
        margin-left: -500px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("器選択支援システム(仮)")
"""本システムは，あなたが選択した料理に適した器をランキングで教えてくれます！"""
st.title("")
# num="ステーキ食べたいかも"
# st.title(num)

# 画像の読み込み
pasta_image = Image.open('pasta.jpeg')
nimono_image = Image.open('nimono.jpeg')
stew_image = Image.open('stew.jpeg')
pasta_plate_image1=Image.open('pasta_plate.jpg')
pasta_plate_image2=Image.open('pasta_plate2.jpg')
nimono_plate_image=Image.open('nimono_plate.jpg')
stew_plate_image=Image.open('stew_plate.jpg')
anmitsu_soup_image=Image.open('anmitsu_soup.png')
curry_pasta_image=Image.open('curry_pasta.png')

# ランキング化するには，以下のリストの画像呼び出しの順番を変えることで可能
# 表示させる器画像を格納したリスト
pasta_plate_list=[pasta_plate_image1,pasta_plate_image2]
nimono_plate_list=[pasta_plate_image1,pasta_plate_image2]
stew_plate_list=[pasta_plate_image1,pasta_plate_image2]

# ランキングの番号のリスト
number_list=[1,2,3,4,5,6,7,8,9]

# 合致度のリスト
match_degree_list=[0.987,0.856]

# サイドバーで形体情報を調節可能
# 合致度が結果によっては低くなる可能性もある
with st.sidebar:
  st.title("詳細設定")
  """結果によっては合致度が低い器が出る場合もあります"""

  st.subheader("＊サイズ")
  values1 = st.slider(
    '長辺を選択してください',
    0.0, 35.0, (0.0, 35.0))
  values2 = st.slider(
    '短辺を選択してください',
    0.0, 35.0, (0.0, 35.0))
  values3 = st.slider(
    '高さを選択してください',
    0.0, 10.0, (0.0, 10.0))
  st.title("")

  # 形状の選択
  st.subheader("＊形状")
  # チェックボックスの場合
  all_material=st.checkbox('全ての形状')
  touki = st.checkbox('丸')
  jiki =st.checkbox('角')
  grass =st.checkbox('花')
  # ラジオボタンの場合
  # genre = st.radio(
  #     "形状を選択してください",
  #     ('全て','丸', '角', '花'))
  st.title("")

  # 材質の選択
  st.subheader("＊材質")
  # チェックボックスの場合
  all_material=st.checkbox('全ての材質')
  touki = st.checkbox('陶器')
  jiki =st.checkbox('磁器')
  grass =st.checkbox('ガラス')

# if agree & aaa:
#   st.write('Great!')
# elif agree:
#   st.write("agree")
# elif aaa:
#   st.write("aaa")

  # ラジオボタンの場合
  # genre = st.radio(
  #     "材質を選択してください",
  #     ('全て','陶器', '磁器', 'ガラス'))
  st.title("")

  # 色の選択
  # 将来的にカラーコード（またはRGB）と画像の色を対応づけする
  st.subheader("＊色")
  color = st.color_picker('クリックして色を選択してください', '#00f900')
  # st.write('The current color is', color)
  st.title("")

  # 印象の選択
  # どのような画面で印象をユーザに選択させるかは未定
  st.subheader("＊印象")
  options = st.multiselect(
     '印象を選択してください',
     ['おしゃれ', 'カフェ風', '和モダン', '和風'])
    

  start_color, end_color = st.select_slider(
     '',
     options=['フォーマル', '少しフォーマル', '両者の間', '少しカジュアル', 'カジュアル'],
     value=('少しフォーマル', '少しカジュアル'))

  color = st.select_slider(
     'おしゃれ',
     options=['1', '2', '3', '4', '5'])
  st.title("")
  st.title("")
  st.title("")

# 料理名が押された時の画像の表示
def click_foodname(foodname,plate_list,):
  if st.button(foodname):
    #  st.write('Why hello there')
    for plate,number,match in zip(plate_list,number_list,match_degree_list):
      st.write(number)
      st.caption(match)
      st.image(plate, use_column_width=True)

  # if st.button("aaa"):
  #      st.write('Why hello there')
  # else:
  #      st.write('Goodbye')

# 料理の選択
# st.header("料理から選ぶ")
st.subheader("▶︎ 料理名を選ぶ")
col1, col2, col3 = st.columns(3)
with col1:
    # st.header("パスタ")
    def pasta_plate_display():
      click_foodname("pasta",pasta_plate_list)
    st.image(pasta_image, use_column_width=True)
with col2:
    # st.header("煮物")
    def nimono_plate_display():
      click_foodname("nimono",nimono_plate_list)
    st.image(nimono_image, use_column_width=True)
with col3:
    # st.header("シチュー")
    def stew_plate_display():
      click_foodname("stew",stew_plate_list)
    st.image(stew_image, use_column_width=True)

# 器の画像の表示
col1, col2, col3 = st.columns(3)
with col1:
  pasta_plate_display()
with col2:
  nimono_plate_display()
with col3:
  stew_plate_display()

st.title("")

# 料理カテゴリが選択された際の分岐
# def 

# 料理の選択
# st.header("料理から選ぶ")
st.subheader("▶︎ あなたがよく作る料理から選ぶ")

options = st.multiselect(
    '料理カテゴリを選択してください',
    ['パスタ', 'カレー','コーンスープ','あんみつ'])

if st.button("選ぶ"):
  col1, col2 = st.columns(2)
  with col1:
    """パスタ，カレー"""
    st.image(curry_pasta_image, use_column_width=True)
  with col2:
    """コーンスープ，あんみつ"""
    st.image(anmitsu_soup_image, use_column_width=True)


st.title("")












#############################
# memo

# agree = st.checkbox('I agree')
# aaa=st.checkbox('aaa')

# if agree & aaa:
#   st.write('Great!')
# elif agree:
#   st.write("agree")
# elif aaa:
#   st.write("aaa")
  

# st.subheader("＊サイズ")
#   col1, col2, col3 = st.columns(3)
#   with col1:
#     values1 = st.slider(
#       '長辺を選択してください',
#       0.0, 35.0, (5.0, 30.0))
#   with col2:
#     values2 = st.slider(
#       '短辺を選択してください',
#       0.0, 35.0, (5.0, 30.0))
#   with col3:
#     values3 = st.slider(
#       '高さを選択してください',
#       0.0, 10.0, (2.0, 8.0))

#   st.title("")

#   col1, col2, col3 = st.columns(3)
#   # 形状の選択
#   with col1:
#     st.subheader("＊形状")
#     genre = st.radio(
#         "形状を選択してください",
#         ('丸', '角', '花'))
#   # 材質の選択
#   with col2:
#     st.subheader("＊材質")
#     genre = st.radio(
#         "材質を選択してください",
#         ('陶器', '磁器', 'ガラス'))
#   # 色の選択
#   # 将来的にカラーコード（またはRGB）と画像の色を対応づけする
#   with col3:
#     st.subheader("＊色")
#     color = st.color_picker('クリックして色を選択してください', '#00f900')
#     # st.write('The current color is', color)
#   st.title("")


# st.header("器から選ぶ")
# st.subheader("＊サイズ")
# col1, col2, col3 = st.columns(3)
# with col1:
#   platesel_long = st.slider(
#      '長辺を選択してください',
#      0.0, 35.0, (6.0, 29.0))
# with col2:
#   platesel_short = st.slider(
#      '短辺を選択してください',
#      0.0, 35.0, (6.0, 29.0))
# with col3:
#   platesel_height = st.slider(
#      '高さを選択してください',
#      0.0, 10.0, (3.0, 7.0))

# col1, col2, col3 = st.columns(3)
# # 形状の選択
# with col1:
#   st.subheader("＊形状")
#   genre = st.radio(
#       "形状を選択してください",
#       ('丸', '角', '花'))
# # 材質の選択
# with col2:
#   st.subheader("＊材質")
#   genre = st.radio(
#       "材質を選択してください",
#       ('陶器', '磁器', 'ガラス'))
# # 色の選択
# # 将来的にカラーコード（またはRGB）と画像の色を対応づけする
# with col3:
#   st.subheader("＊色")
#   color = st.color_picker('クリックして色を選択してください', '#00f900')
#   # st.write('The current color is', color)
# st.title("")