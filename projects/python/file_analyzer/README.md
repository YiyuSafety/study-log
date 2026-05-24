# Python 文件统计小工具

## 项目简介

这是一个使用 Python 编写的文本文件统计工具。

它可以统计一个文本文件的：

- 字符数
- 行数
- 单词数

## 用到的知识点

- pathlib
- 文件读取
- 条件判断
- 函数封装
- 字符串统计
- split()

## 文件结构

```txt
file_analyzer/
├── file_analyzer.py
├── test.txt
└── README.md
## 扩展练习：统计当前目录下的 txt 文件

新增 `txt_counter.py`，用于统计当前脚本所在文件夹中的 `.txt` 文件数量。

### 新增知识点

- Path(__file__)
- .parent
- .iterdir()
- .suffix
- is_file()

### 关键理解

- `Path(".")` 表示当前终端所在目录
- `Path(__file__)` 表示当前正在运行的 Python 文件
- `Path(__file__).parent` 表示当前 Python 文件所在的文件夹
- `.iterdir()` 可以遍历文件夹第一层内容
- `.suffix` 可以获取文件后缀名
