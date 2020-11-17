import bf_engine
import json

# 机器人创建
bot = bf_engine.init()

# 机器人appid
print("appid: " + bot.app_id)

# 机器人数据
qalist  = bot.qa.qa_list()

print("语料列表： " + str(json.dumps(qalist, ensure_ascii=False, indent=2)))

print('qa出话：' + str(bot.qa.query('竹间你好呀')))

# 删除问题
print("删除一条标准问题")
bot.qa.delete_question()
# 机器人数据
print("语料列表： " + str(json.dumps(bot.qa.qa_list(), ensure_ascii=False, indent=2)))

# 添加问题
print("添加一条标准问题")
bot.qa.add_question(
    {
        "sq": "谁是NLP宇宙第一",
        "tags": ["你好呢"],
        "lq": ["竹间你好呀", "竹间你好吗", "你好呀"],
        "answers": [
            {"answer": "未来竹间是NLP NO1", "time_tag": "NLP混沌时间"},
            {"answer": "竹间是NLP NO1", "time_tag": "竹间成立时间"}
        ]
    }
)
# 机器人数据
print("语料列表： " + str(json.dumps(bot.qa.qa_list(), ensure_ascii=False, indent=2)))
