import bf_engine

# 机器人创建
bot = bf_engine.init(app_id="0297c1010f244a70822d287484a08889")

# 训练问答语料
bot.qa.train(data={"data": [{"sq": "竹间你好", "lq": ["竹间你好呀", "竹间你好吗"], "answer": "竹间是NLP宇宙第一"}]})
# or 指定问答和语料文件
# bot.qa.train(question_path="data/问答上传模板.xlsx",corpus_path="data/语料上传模板.xlsx")
# 问答出话
print('qa出话：' + bot.qa.query('竹间你好').text)
# qa发布
bot.qa.publish()

# 训练知识图谱
bot.kg.train(data={"data": [{"entity": "竹间", "property": "年龄", "value": "5"}]})
# 知识出话
print('kg出话: ' + bot.kg.query('竹间的年龄').text)
# 未知回复出话
print('backfill出话: ' + bot.dm.query('未知回复').text)

# 加载任务
bot.te.load(path='data/taskengine.json')
# 任务出话
print('te出话: ' + bot.te.query('我要买火车票').text)
print('te出话: ' + bot.te.query('北京').text)
print('te出话: ' + bot.te.query('是的').text)

bot.dm.load([{"qa": 90}, {"kg": 92}, {"qa": 60, "kg": 65}, {"te": 60}])
# or 需指定配置文件
# bot.dm.load_by_path(config_path='data/对话配置.json')
#
print("对话管理出话: " + bot.dm.query("竹间的年龄").text)
print("对话管理出话: " + bot.dm.query("竹间你好").text)
print("对话管理出话: " + bot.dm.query("我要买火车票").text)
print("对话管理出话: " + bot.dm.query("北京").text)
print("对话管理出话: " + bot.dm.query("是的").text)

# 生成二维码到指定目录
bot.dm.qrcode()
# or 控制台生成二维码
# bot.dm.qrcode(filePath="data/qrcode.png")
