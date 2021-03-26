from AssetCloud import AssetCloudRequest

ret = AssetCloudRequest.http_request(
    url = 'http://platform.assetcloud.org.cn/dev-api/blade-system/api/acttodo/getallacttodo?current=1&size=10',
    key = '347bf4794ff54b1fa3068d1fc66dc6ccqhTRwqW6FRGXVTfeNV', 
    secret = 'b1f1905b67014eddaf274a78f398d2618ADE22CCFAABEF258E0AA4E2AB411FACFC3A9803C732E473E526B778E6CCE8A1', 
    httpMethods = 'GET')
print(ret)