# KP用リポジトリ
## 環境構築

### 開発環境

__1. 仮想環境を立てる (なんでもいい)__

```shell
python -m venv dev
```

__2. 仮想環境に入る__

```shell
source dev/bin/activate
```

__3. pyinstallerをインストールする__

```shell
pip install pyinstall
```

### 実行環境

__特に必要なし__

ただし、実行時に `shopping_list.csv` を読み込むので、該当ファイルが存在しないとエラーが吐かれる。

## バイナリのビルド方法

以下の記事が参考になる

https://qiita.com/nal_dal_dere/items/95e173068af399e61981


コマンド一発でいける

```shell
pyinstaller shop.py --onefile
```

成果物として、`dist/shop` が得られるので、これを以下のように使う

```shell
dist/shop
```

## 使い方

### 概要
`shop.py` と `dist/shop` は同様の方法で使用できるので、 `shop.py` を例に挙げて使い方を説明する。カレントディレクトリに `shopping.csv` がある状態で、以下のようにpythonファイルを実行する。

```shell
python shop.py
```

買い物の結果が `results.csv` に出力される。

### shopping.csv の形式

以下の形式で買う個数を記述する。

```csv
Aを買う個数,Bを買う個数,Cを買う個数,Dを買う個数,Eを買う個数,Fを買う個数
```

さらに、複数行にわたって記述することで、それらすべての計算結果が `results.csv` に出力される。

### results.csv の形式

以下の形式で当たり判定結果が出力される。

```csv
合計,購入,当たり
購入に使った金額+当たった商品の金額,購入に使った金額,当たった商品の金額の合計
```