import bf_engine

# 机器人创建
bot = bf_engine.init(app_id='a4803aa5a3374938adba15eeb42eX9p4')

# 生成二维码到指定目录
# bot.dm.qrcode()
# or 控制台生成二维码
bot.dm.chat(filePath="data/qrcode.png")
