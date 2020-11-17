import bf_engine

# 机器人创建
bot = bf_engine.init()
# bot = bf_engine.init(app_id="kg_demo_file", url="http://127.0.0.1")

# 机器人appid
print("appid: " + bot.app_id)


def query(sentence, bot):
    print("User: ",  sentence)
    answer = bot.kg.query(sentence)
    print("Bot: ", str(answer.text))

# 全量训练知识图谱
bot.kg.train_by_path(data_path="知识图谱上传模板v2.02.xlsx")

# 问答出话

query("华为P40怎么卖的，多贵啊?",bot)
query("摄像头像素是多少，我想要拍照清楚一些的",bot)
query("内存是多大的",bot)
query("待机是多久",bot)
query("屏幕是多大的",bot)

