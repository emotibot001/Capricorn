import json
import logging

import bf_engine


def query(sentence, bot):
    print("User: ", sentence)
    answer = bot.dm.query(sentence)
    print("Bot: ", str(answer.text))
    print("_" * 100)


bot = bf_engine.init(app_id="a4803aa5a3374938adba15eeb42eX9xx")

bot.intent.train(data={
    "data": [
        {
            "name": "无法开机",
            "corpus": ["耳机不能开机了", "还是不能开机", "开机还是没反应", "依然开不了机", "耳机无法开机"]
        },
        {
            "name": "无法充电",
            "corpus": ["不行，充不上", "充电没反应", "充不了电", "充了好久没反应"]
        },
        {
            "name": "蓝牙无法连接",
            "corpus": ["蓝牙连不上了", "蓝牙连接失败", "无法连接", "蓝牙还是连不上"]
        }
    ]}, append=False)

# 训练意图
bot.intent.publish()

#导入多轮
bot.te.load('data/耳机无法充电.json')
bot.te.load('data/耳机无法开机.json')
bot.te.load('data/耳机蓝牙无法连接.json')

# 加载对话配置
bot.dm.load(path='data/dialogue_jumper.json')

query("你好，我的耳机无法开机了", bot)
query("充电没反应啊", bot)
query("开机了，蓝牙现在连不上了", bot)
query("好了，谢谢", bot)

