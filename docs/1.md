# Python SDK的用法说明

- ```url```：完整的请求路径 http://platform.assetcloud.org.cn/dev-api/+请求路径；

- ```key```、```secret```:平台获取的key和secret

安装：

```python
python setup.py install
```

Get调用方法：

```python
from AssetCloud import AssetCloudRequest

AssetCloudRequest.http_request(
    url = '',
    key = '', 
    secret = '', 
    httpMethods = 'GET')
```

Post调用方法：
```python
from AssetCloud import AssetCloudRequest

AssetCloudRequest.http_request(
    url = '',
    key = '', 
    secret = '', 
    body = '', 
    httpMethods = 'POST')
```

Delete调用方法：

```python
from AssetCloud import AssetCloudRequest

AssetCloudRequest.http_request(
    url = '',
    key = '', 
    secret = '', 
    httpMethods = 'DELETE')
```

Put调用方法：
```python
from AssetCloud import AssetCloudRequest

AssetCloudRequest.http_request(
    url = '',
    key = '', 
    secret = '', 
    body = '', 
    httpMethods = 'PUT')
```
返回结果为：```dict```

| 字段    | 类型    | 说明     |
| ------- | ------- | -------- |
| code    | int     | 状态码   |
| success | boolean | 是否成功 |
| data    | dict    | 承载数据 |
| msg     | string  | 返回消息 |