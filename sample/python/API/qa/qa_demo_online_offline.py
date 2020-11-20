import bf_engine
import json

# 机器人创建
bot = bf_engine.init()

# 机器人appid
print("appid: " + bot.app_id)

# 训练问答语料
bot.qa.train(data={"data":
    [{
        "sq": "谁是NLP宇宙第一",
        "category_id": "-1",
        "lq": ["在NLP领域谁是第一名", "NLP第一名是哪家"],
        "answer": "竹间是NLP宇宙第一"
    }]}, append=False)

# 问答出话
print('qa出话：' + str(bot.qa.query('NLP第一名是谁家')))

# 训练问答语料
bot.qa.train(data={"data":
    [
        {
            "sq": "谁是NLP宇宙第一",
            "lq": ["竹间你好呀", "竹间你好吗"],
            "category_id": "-1",
            "answers": [
                {"answer": "未来竹间是NLP宇宙第一","time_tag":"NLP混沌时间"},
                {"answer": "竹间是NLP宇宙第一", "time_tag":"竹间成立时间"}
            ]
        }
    ]},append=False)

# 训练问答语料(增量:append=True)
bot.qa.train(data={"data":
    [
        {
            "sq": "竹间你好",
            "related": ["谁是NLP宇宙第一"],
            "lq": ["竹间你好呀", "竹间你好吗"],
            "answer": "欢迎加入竹间"
        }
    ]}, append=True)

# 问答出话(线下)
print('qa出话：' + str(bot.qa.query('谁是NLP宇宙第一')))
print('qa出话：' + str(bot.qa.query('竹间你好')))

# 发布
bot.qa.publish()
# 问答出话(线上)
print('qa出话：' + str(bot.qa.query('竹间你好', online=True)))
# 问答出话(时间段)
print('qa出话：' + str(bot.qa.query('NLP宇宙第一是谁')))

# qa列表
print("语料列表" + str(json.dumps(bot.qa.qa_list(), ensure_ascii=False, indent=2)))

# 导出问答和语料
bot.qa.export(sq_path="data/问答.xlsx", lq_path="data/语料.xlsx")