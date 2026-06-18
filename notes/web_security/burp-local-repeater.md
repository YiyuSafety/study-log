## 删除 email 参数测试

原始请求参数：
username、password、email、phone、submit

修改后请求参数：
username、password、phone、submit

观察结果：
- 请求 Content-Length 从 102 变成 76
- 响应状态码仍然是 200 OK
- 响应 Content-Length 仍然是 1996
- 页面返回内容没有明显变化

初步判断：
删除 email 参数后，后端没有返回明显不同的响应，可能没有严格校验 email 参数，或者错误处理没有体现在页面响应中。