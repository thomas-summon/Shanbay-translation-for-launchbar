# Shanbay-translation-for-launchbar

## 介绍
Shanbay Tranlation 是一个基于扇贝api的Launchbar快速查词Action。通过它，你可以在Launchbar的交互界面快速查询英文单词的中文翻译并直接将结果显示在界面上。

## 依赖
Shanbay Tranlation 的脚本文件是由Python3编写的，并使用了requests这个Python模块。所以，要正常使用 Shanbay Tranlation, 请先下载这两个依赖。

### Python3

#### 使用homebrew下载（推荐）
* 打开终端，输入以下指令下载homebrew
`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
* homebrew下载完成后，输入下面的指令下载Python3
`brew install python3`

#### 官网下载
当然，你也可以直接从官网下载安装包安装。
下载地址：https://www.python.org/downloads/

### requests模块
下载完Python3后，你同时也下载了Python3自带的包管理软件pip3，通过它下载requests模块。
打开终端，输入以下指令下载`pip3 install requests`

## 安装
* 点击[这里](https://github.com/Thomas4949/Shanbay-translation-for-launchbar/raw/master/Shanbay_Translation.lbaction.zip)下载 Shanbay Tranlation 的压缩文件。
* 解压缩
* 双击解压文件，Launchbar会自动识别并安装。

## 可能出现的问题
下载完成后，当你在使用 Shanbay Tranlation 时，可能会出现类似于这样的错误界面
![错误界面](https://github.com/Thomas4949/Shanbay-translation-for-launchbar/raw/master/screen.png)
这很可能是因为一个与Shebang有关的错误。
为了尽可能适应各种情况，脚本Shebang部分使用的是`#!/usr/bin/env/python3`，但有的时候，这会出现问题，
具体参见[这里](https://stackoverflow.com/questions/10623833/usr-bin-env-python2-6-no-such-file-or-directory-error)
和[这里](https://stackoverflow.com/questions/11390206/usr-bin-env-python2-no-such-file-or-directory)。
### 一个解决办法
将`#!/usr/bin/env/python3`改为`#!你的Python3解释器的绝对路径`，如果你的Python3是使用homebrew下载的，那这个路径就是`/usr/local/bin/python3`。
