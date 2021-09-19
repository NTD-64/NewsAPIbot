import pandas as pd
import os
from os import listdir

key_word = 'Mizuho' #指定キーワード
main_path='C:/Users/mxr78/PycharmProjects/pythonProject0809' #pythonの実装パス
path_csv = main_path + '/' + key_word #csvを格納したフォルダパス

#csvフォルダにある全csvファイルをリストで取得
files_csv = [csvname for csvname in listdir(path_csv) if not csvname.startswith('.')]

#csvフォルダに移動
os.chdir(path_csv)

dflist = []
#1つずつcsvを読み込んでappendでくっつける
for file in files_csv:
    dftemp = pd.read_csv(file)
    dflist.append(dftemp)

#データフレームとして格納して、日付順に並び替え
df = pd.concat(dflist, axis = 0)
df = df.drop(columns = ['Unnamed: 0'])
df['publishedAt'] = pd.to_datetime(df['publishedAt'])
df_sort = df.sort_values(['publishedAt'])

#メインフォルダに移動
os.chdir(main_path)
csvname = key_word + '.csv'
df_sort.to_csv(csvname, index = False)