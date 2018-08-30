# Redis 数据库地址
REDIS_HOST = 'localhost'

# Redis 端口
REDIS_PORT = 6379

# Redis密码,无填None
REDIS_PASSWORD = None

# 生产器使用的浏览器
BROWSER_TYPE = 'Chrome'

# 生产器类，如扩展其他站点，请在此配置
GENERATOR_MAP = {
    'weibo':'WeiboCookiesGenerator'
}

# 测试类，如扩展其他站点，请在此配置
TESTER_MAP = {
    'weibo':'WeibovalidTester'
}

TEST_URL_MAP = {
    'weibo':'https://m.weibo.cn/'
}

# 生产器和验证器循环周期
CYCLE = 120

# api地址和端口
API_HOST = '0.0.0.0'
API_PORT = 5000

# 生产器开关，模拟登录添加Cookies
GENERATOR_PROCESS = False

# 验证器开关，循环检测数据库中的Cookies是否可用，不可用删除
VALID_PROCESS = False

# API 接口服务
API_PROCESS = True