# Burp 本地抓包与 Repeater 练习

## 1. 实验环境
- 本地站点：http://127.0.0.1
- 环境：phpstudy
- 工具：Burp Suite Community
- 页面：学生信息登记表

## 2. 抓到的请求
- GET / ：访问首页
- POST /index.php ：提交表单
- GET /login.php ：访问登录页面

## 3. POST 请求体观察
原始请求参数：
username、password、email、phone、submit

## 4. 删除 email 参数测试
修改后请求参数：
username、password、phone、submit

观察结果：
- 请求 Content-Length 从 102 变成 76
- 响应状态码仍然是 200 OK
- 响应 Content-Length 仍然是 1996
- 页面返回内容没有明显变化

## 5. 初步判断
删除 email 参数后，后端没有返回明显不同响应，可能说明：
- 后端没有严格校验 email 参数；
- 或者后端有校验，但错误提示没有体现在页面响应中；
- 或者该页面只是返回原页面，并未完成完整注册逻辑。

## 6. 今日结论
Repeater 可以手动修改 HTTP 请求并重复发送，用来观察服务器对不同参数的响应。
前端限制不能代表后端限制，Web 安全测试需要直接观察 HTTP 请求和响应。
