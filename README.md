# mypkg
 * ロボットシステム学のROS2のパッケージです。また、ROS2を実際に授業で理解するために使ってみるためのものです。

![test](https://github.com/kamemattari/mypkg/actions/workflows/test.yml/badge.svg)

# 説明
talker(パブリッシャ)が数字をカウントしてInt16ビット型のメッセージをトピック(countup)でとばし、そのcountupでメッセージをlistener(サブスクライバー)が受け取って出力しています。

 * 使い方
```
$ ros2 launch mypkg talk_listen.launch.py
```
上記の通りに実行する。

# 必要なソフトウェア
 * ROS2(Humble テスト済み)
 * Python 3.10

# テスト環境
 * Ubuntu 22.04

# LICENSE
 * このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます
 * © 2022 Aika Katsuki
