# TDD 練習用 (Python)
## doctest サンプル
[tax.py](./tax.py) を見てね。詳しい使い方は[リファレンス](https://docs.python.jp/3/library/doctest.html)を。


## unittest サンプル
[test_tax.py](./test_tax.py) を見てね。"詳しい使い方は[リファレンス](https://docs.python.jp/3/library/doctest.html)を。


## TDD 体験
| 分類 | 金額
| ---- | ----
| 通常 | 二泊まで 200 円、それ以降は一泊 200 円
| 新作 | 一泊 300 円
| 子供向け | 三泊まで 150 円、それ以降は一泊 150 円


1. 一番簡単に書けそうなテストコードをひとつだけ書く
2. 失敗を確認
3. それを通すための最低限のコードを書く
4. 成功するまで 3 をがんばる
5. 1 からもう一度

境界値テストとかは意外と面倒なので程々でやめて、次に行く。


### リファクタリング体験
TDD による開発では必要十分なテストコードが生まれるので、リファクタリングがとても簡単。リファクタリングをすることで、境界値テストがやりやすくなり、テストの質が上がることを体験する。
