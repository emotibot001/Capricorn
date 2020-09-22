import bf_engine

bot = bf_engine.init()
print("app_id", bot.app_id)
bot.config.set_backfill_answer([
    "不好意思，没理解您的意思呢。",
    "这对我来说有点难呢，还需要继续努力，再换种问法试试呗~",
    "您可以试试别的问法呢~",
    "有点没明白您的意思呢，您可以换一种问法问我哦~"
])
print("获取未知回复话术", bot.config.get_backfill_answers())
print("未知回复出话: ", bot.dm.query("你好").text)
print("未知回复出话: ", bot.dm.query("你好").text)
