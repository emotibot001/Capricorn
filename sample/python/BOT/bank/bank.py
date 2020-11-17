import bf_engine

# 机器人创建
bot = bf_engine.init()

# 机器人appid
print("appid: " + bot.app_id)

# qa 训练、测试、发布与对话
bot.qa.train(question_path='银行行业标准问.xlsx', corpus_path='银行行业语料.xlsx')
qa_test_set = bf_engine.TestSet([
    ('申请哪种信用卡比较好', '申请信用卡，需要根据自己的需求和经济状况。一般来讲，当然是越高级的卡越好，但是高级卡的审批会关注工作单位、工资流水、财产证明。 如果您经常出国，推荐办理我行和国际卡组织合作推出的全币信用卡，VISA、Master、JCB、AE，各具特色，一应俱全，可以满足您的出境消费需求。 您可点击【信用卡产品介绍链接】，查看我行所有特色信用卡，根据您的实际消费环境和不同卡种的优惠活动进行选择。'),
    ('信用卡客服热线', '信用卡24小时客户服务热线：xxxxxxx。'),
])
bot.qa.test(qa_test_set).show()
bot.qa.publish()
print(bot.qa.query(text='什么是到期还款日', online=True).text)

# kg 训练与对话
bot.kg.train(path='银行业知识推理引擎.xlsx')
print(bot.kg.query(text='乐驾白金卡主卡年费', online=True).text)

# te 加载与对话
bot.te.load(path='银行催收.json')
print('银行催收')
print(bot.te.query('银行催收').text)
print('是我')
print(bot.te.query('是我').text)
print('明天行吗？今天没办法')
print(bot.te.query('明天行吗？今天没办法').text)
print('我现在手头钱不够啊')
print(bot.te.query('我现在手头钱不够啊').text)
print('哎，那我去借借看吧')
print(bot.te.query('哎，那我去借借看吧').text)
print('我尽量吧')
print(bot.te.query('我尽量吧').text)
print('我知道')
print(bot.te.query('我知道').text)
