import bf_engine

def query(sentence, bot):
    print("User: ",  sentence)
    answer = bot.te.query(sentence)
    print("Bot: ", str(answer.text))

# 机器人初始化
bot =bf_engine.init()

#TE
bot.te.editor(path="taskengine.json")
# 任务出话
query("我要买火车票", bot)
query("北京", bot)
query("是的", bot)
