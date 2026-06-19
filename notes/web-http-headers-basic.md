# HTTP 请求头与响应头基础

## 1. 实验环境

- 本地站点：http://127.0.0.1
- 工具：Burp Suite Community
- 环境：phpstudy

## 2. 请求行

示例：

POST /index.php HTTP/1.1

说明：

- POST：请求方法
- /index.php：请求路径
- HTTP/1.1：协议版本

## 3. 常见请求头

| 请求头 | 作用 |
|---|---|
| Host | 访问的主机 |
| User-Agent | 浏览器身份 |
| Content-Type | 请求体数据格式 |
| Content-Length | 请求体长度 |
| Origin | 请求来源站点 |
| Referer | 请求来源页面 |
| Cookie | 会话信息 |

## 4. 常见响应头

| 响应头 | 作用 |
|---|---|
| Server | Web 服务器信息 |
| X-Powered-By | 后端技术信息 |
| Content-Type | 返回内容类型 |
| Content-Length | 响应体长度 |

## 5. 今日理解

- 请求头是浏览器发给服务器的附加信息。
- 响应头是服务器返回给浏览器的附加信息。
- POST 表单数据通常在请求体中。
- Content-Type 说明数据格式。
- Content-Length 表示数据长度。