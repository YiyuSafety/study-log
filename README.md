# study-log

这是我的个人学习记录仓库，主要用于记录计算机基础、Python、Linux、Git、Web 安全与网络安全方向的学习过程。

当前目标不是“堆资料”或“只看视频”，而是通过 **笔记 + 实操 + 截图证据 + 小项目产出** 的方式，逐步建立真实的技术能力。

---

## 当前学习方向

目前主线：

* Python 基础与脚本开发
* Linux 基础命令与系统操作
* Git / GitHub 使用
* Web 基础与 HTTP 请求分析
* Burp Suite 抓包与 Repeater 练习
* Web 日志分析与安全特征识别
* Web 安全基础入门

后续计划：

* HTTP / Cookie / Session / Token
* 常见 Web 漏洞原理
* XSS / SQL 注入 / 文件上传 / 越权等漏洞复盘
* Python 安全小工具
* 代码审计与业务安全基础

---

## 仓库目录结构

```text
study-log/
├── daily/              # 每日学习记录
├── notes/              # 专题学习笔记
│   ├── linux_notes/    # Linux 学习笔记
│   ├── python_notes/   # Python 学习笔记
│   ├── web_security/   # Web 安全与抓包分析笔记
│   └── github-basic.md # Git / GitHub 基础笔记
├── projects/           # 学习过程中的小项目和脚本
├── screenshots/        # 学习截图、实验截图、运行结果截图
└── README.md           # 仓库说明
```

---

## 最近学习记录

### Web 安全基础

* 使用 Burp Suite 抓取本地站点 HTTP 请求
* 分析 GET / POST 请求区别
* 使用 Repeater 修改请求参数并重复发送
* 观察删除 `email` 参数后请求与响应的变化
* 理解“前端限制不等于后端限制”

相关笔记：

* `notes/web_security/burp-local-repeater.md`

### Python 项目练习

* 文件读取与统计
* 文本内容处理
* 目录遍历
* Markdown 报告生成

相关目录：

* `projects/python/`

### Web 日志分析

已完成一个基础 Web 日志分析项目，用于解析访问日志并生成安全分析报告。

涉及能力：

* Python 文件处理
* 正则表达式解析日志
* IP / URL / 状态码统计
* 异常访问特征识别
* Markdown 报告生成

相关项目：

* [SecLog-Analyzer](https://github.com/YiyuSafety/SecLog-Analyzer)

---

## 当前阶段目标

短期目标：

* 熟练使用 Burp Suite 抓包、重放请求、观察响应
* 理解 HTTP 请求与响应结构
* 能够看懂常见请求头、响应头、请求参数
* 能够用 Python 编写简单安全辅助脚本
* 持续整理学习笔记和实验截图

中期目标：

* 完成常见 Web 漏洞基础复盘
* 形成一批可以展示的漏洞学习笔记
* 迭代 Web 日志分析工具
* 建立清晰的 GitHub 作品集结构

长期目标：

* 走 Web 安全 / 应用安全 / 业务安全方向
* 通过持续产出证明学习过程和实际能力
* 为后续安全实习或技术岗位做准备

---

## 学习原则

1. 不只看视频，必须有实操。
2. 不只模仿步骤，必须写出自己的理解。
3. 不只学工具，必须理解请求、代码和业务逻辑。
4. 不在未授权环境中测试，只在本地环境、靶场或授权范围内练习。
5. 每次学习尽量留下可检查的产出，例如笔记、脚本、截图或项目提交。

---

## 当前技术栈

正在学习和使用：

* Python
* Linux
* Git / GitHub
* Burp Suite
* HTTP / Web 基础
* PHPStudy 本地 Web 环境
* Markdown 文档整理

---

## 仓库定位

这个仓库不是最终作品集，而是我的学习过程记录。

它的作用是：

* 记录每天学了什么
* 保存实操过程和截图证据
* 整理技术笔记
* 沉淀小工具和项目
* 证明自己在持续推进网络安全学习

后续会持续更新。
