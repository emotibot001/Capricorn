import bf_engine

# 机器人创建
bot = bf_engine.init()

# 机器人appid
print("appid: " + bot.app_id)

# qa 训练、测试、发布与对话
bot.qa.train(question_path='保险行业标准问.xlsx', corpus_path='保险行业语料.xlsx')
qa_test_set = bf_engine.TestSet([
    ('如何解除微信绑定', '您如需解除微信的绑定，可以前往我公司的服务柜面办理，也可以联系您的代理人为您办理。'),
    ('如何查看下载电子保单', '您可登陆公司官网查看并下载您的电子保单'),
])
bot.qa.test(qa_test_set).show()
bot.qa.publish()
print(bot.qa.query(text='如何解除微信绑定', online=True).text)

# kg 训练与对话
bot.kg.train(path='保险行业知识推理引擎.xlsx')
print(bot.kg.query(text='易安行犹豫多久', online=True).text)

# te 加载与对话
bot.te.load(path='保险回访.json')
print('保险')
print(bot.te.query('保险').text)
print('是我')
print(bot.te.query('是我').text)
print('现在还算有点时间，你说吧')
print(bot.te.query('现在还算有点时间，你说吧').text)
print('我想想，0730')
print(bot.te.query('我想想，0730').text)
print('不太了解，你再帮我讲讲吧')
print(bot.te.query('不太了解，你再帮我讲讲吧').text)
print('这样清楚多了')
print(bot.te.query('这样清楚多了').text)
