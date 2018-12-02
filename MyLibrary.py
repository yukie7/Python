# coding: utf-8

import sys

# 入力（改行アリ）を終わりまで（EOF）まで読み込み
# a b c d ...
a = []
for line in sys.stdin:
    line = line.replace('\n','') #改行文字を除去（空文字に置き換え）
    a.append(line)

# 配列aの1文字目を除去
del a[0]

# 小文字→大文字
# a = "abc" → a = "ABC"
a.upper()

# 大文字→小文字
# a = "ABC" → a = "abc"
a.lower()

# split
# a = "1 10" → tmp = [1, 10]
tmp = a.split(' ')

# 文字列指定部分取り出し
# a = "123" → "23"
a = a[1:]
# a = "123" → "12"
a = a[:-1]

''' 偶数桁，奇数桁'''
word = "パタトクカシーー"

# 奇数番目の文字を抽出
extract1 = word[::2]
print(extract1)

# 偶数番目の文字を抽出
extract2 = word[1::2]
print(extract2)
''' 偶数桁，奇数桁'''

# 文字列変換（translate） leet文字列
# input : PAIZA → result : P4124
# input : ALANTURING → result : 4L4NTUR1N6
table = str.maketrans({
    'A': '4',
    'E': '3',
    'G': '6',
    'I': '1',
    'O': '0',
    'S': '5',
    'Z': '2',
})
input_lines = input()
result =input_lines.translate(table)


