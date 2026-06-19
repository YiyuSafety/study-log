# 01-文件与权限

## 一、今天学习目标

今天主要学习 Linux 中最基础的文件操作和权限查看：

1. 会创建目录和文件
2. 会向文件写入内容并查看内容
3. 会修改文件权限
4. 会看懂 `ls -l` 显示的权限信息

---

## 二、常用命令速记

| 命令 | 作用 |
|---|---|
| `mkdir 目录名` | 创建目录 |
| `cd 目录名` | 进入目录 |
| `touch 文件名` | 创建一个空文件；如果文件已存在，会更新文件时间 |
| `echo "内容" > 文件名` | 把内容写入文件，会覆盖原内容 |
| `cat 文件名` | 查看文件内容 |
| `chmod 权限 文件名` | 修改文件权限 |
| `ls -l 文件名` | 查看文件的详细信息，包括权限、所有者、大小、时间等 |

---

## 三、今天敲过的命令

```bash
mkdir cyber-study
cd cyber-study
mkdir linux python git
touch linux/test.txt
echo "hello linux" > linux/test.txt
cat linux/test.txt
chmod 600 linux/test.txt
ls -l linux/test.txt
