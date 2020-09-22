import bf_engine
import json

# 机器人创建
bot = bf_engine.init()

# 设置意图预值
bot.set.intent_threshold=65.0

# 机器人appid
print("appid: "+bot.app_id)

# 训练意图语料
bot.intent.train(data={"data":
    [
        {
            "domain":"闹钟提醒",
            "intents":[
                {
                    "name":"设置，提醒",
                    "corpus":{
                        "positive":[
                            "每天早上七点提醒我天气预报",
                            "提前半小时提醒我",
                            "把闹钟给我调到六点半",
                            "到下午6点提醒我吃药"
                        ],
                        "negative":[
                            "吵死了",
                            "噪音太大",
                            "没睡好"
                        ]
                    }
                },
                {
                    "name": "取消，提醒",
                    "corpus": {
                        "positive": [
                            "取消后天上午十点的闹钟",
                            "明天九点的闹铃取消了",
                            "删掉关于去医院的提醒",
                            "不要闹钟"
                        ],
                        "negative": [
                            "记得明天要吃饭哦",
                            "声音太大了"
                        ]
                    }
                }
            ]
        }
    ]})
# 关闭内置意图
bot.intent.close_inner_intents()
# 打开内置意图
bot.intent.open_inner_intents()
# 打开"通用"意图
bot.intent.open_intent_group(group_id="chat")
# 关闭"通用"意图
bot.intent.close_intent_group(group_id="chat")

# 意图测试
print('intent：'+str(bot.intent.predict("提醒我吃饭")))
# 意图测试
print('intent：'+str(bot.intent.predict("太困了")))
# 内置意图
print('intent：'+str(bot.intent.predict("打开爱奇艺应用")))
# 获取意图列表
print('intents：'+str(json.dumps(bot.intent.intents_list(), ensure_ascii=False, indent=2)))