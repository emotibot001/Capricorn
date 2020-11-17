import json

import bf_engine

# 机器人创建
bot = bf_engine.init()

# 问答出话
sentence = '我要去北京，帮我订下周三晚上8点的车票, 从上海出发，联系电话：13212341234'

# 可获取可调用的的所有parser
parsers = bot.ner.get_parsers()

#  parsers中的parserId 可以通过
results = bot.ner.predict(sentence=sentence, parsers=['transport', 'chrono', 'phone'])

for result in results:
    print('提取到了 ' + result.slot_content + '-----' + result.slot_name + '(' + result.slot_desc.replace('\n', '') + '): ')