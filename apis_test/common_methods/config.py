#encoding:utf-8

"""
1、hosts  每个环境、接口的域名＋端口；
2、apis   每个接口具体路径   注意：前面需要加"/"
3、datas  每个环境数据库详细信息
"""

hosts={
    "sit" :"http://mjkalphanew.chinatopcredit.com",
    "uat" :"http://mjkbetanew.chinatopcredit.com",
    "beta":"http://域名"
}

apis = {
    "51fund授权码接口Access-Token":{
        "path":"/api/authority",
        "method":"post"
    },
    "获取51公积金数据":{
        "path":"/housing-fund/51/notification",
        "method":"post"
    }
    }

datas={
    "sit-mysql":{
        "数据库类型":"mysql",
        "数据库hosts":"rm-uf6s86ucfa1mvy1m8o.mysql.rds.aliyuncs.com",
        "数据库名称":"ppmiao_test",
        "数据库端口":"3306",
        "用户名":"ppmiao",
        "用户密码":"PPmiao1234"
           },
    "sit-redis":{
        "数据库类型":"redis",
        "数据库hosts":"10.1.5.1",
        "数据库名称":"0",
        "数据库端口":"6384",
    }
}

emails={
    "mail_info":{
    "sender":"renyx@ppmiao.cn",
    "sender_pass": "Zxm506540345",
    "recipient":["506540345@qq.com"],
    }
}

