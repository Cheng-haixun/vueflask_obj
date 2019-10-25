class Config(object):
    #连接数据库的信息,# url的格式为：数据库的协议：//用户名：密码@ip地址：端口号（默认可以不写）/数据库名
    QLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@47.97.25.111:3306/vueflask"
    # 动态追踪数据库的修改.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 会打印原生sql语句，便于观察测试
    SQLALCHEMY_ECHO = True  # 会打印原生sql语句，便于观察测试
    # 在flask项目中，Session, Cookies以及一些第三方扩展都会用到SECRET_KEY值，这是一个比较重要的配置值。
    #设置秘钥
    SECRET_KEY="123456"