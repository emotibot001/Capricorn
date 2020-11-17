import bf_engine

# 机器人创建
bot = bf_engine.init()

# 机器人appid
print("appid: "+bot.app_id)

# 训练问答语料
bot.qa.train(question_path="data/问答上传模板.xlsx", append=False)

# 问答出话
print('qa出话：' + bot.qa.query('竹间你好').text)

# 导出问答和语料
bot.qa.export(sq_path="data/问答.xlsx", lq_path="data/语料.xlsx")
