hetzer
==

Javaのプログラムに対して，メソッド名の動詞の逆難読化をするプログラム

## Description
機械学習（ランダムフォレスト）を用いて，名前難読化されたJavaプログラムに対して，メソッド名の動詞を逆難読化（復元）するプログラムです．
メソッドの情報を取り出すために，[sufbo](https://github.com/tamada/sufbo)が必要となります．

## Requirement
* [sufbo](https://github.com/tamada/sufbo)
* WordNet
* Python 2.7
* Gradle
* pip

## Usage
1. sufboの準備
    1. [sufbo](https://github.com/tamada/sufbo)をClone，Buileする．
    1. 出来た`sufbo.jar`をlibsにおく．
1. hetzerのBuild
    1. 以下コマンドでBuildする．
    ```
    $ gradle build
    ````
1. 逆難読化モデルの作成
    1. sufboを用いて，学習データに使うjarファイルを成型，書き出す（詳しくは[sufbo](https://github.com/tamada/sufbo)）．
    1. 書き出したファイルを以下コマンドで機械学習し，モデルを作成する（詳しくは`-h`で参照のこと）．
    ```
    $ python src/model_maker/python/main.py LEARNING_DATA
    ```
1. 逆難読化
    1. 3.で作成したモデルを用いて，以下コマンドで逆難読化する（詳しくは`-h`で参照のこと）．
    ```
    $  python src/main/python/main.py MODEL TARGET
    ```
