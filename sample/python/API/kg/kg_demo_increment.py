import bf_engine

# 机器人创建
print('机器人创建')
# bot = bf_engine.init("kg_example_id1")
bot = bf_engine.init("kg_example_id4")

# bot = bf_engine.create_bot(url="http://172.16.103.106")

# 机器人appid
# print("appid: " + bot.app_id)

# 知识推理引擎 增量添加三元组
print('\n知识推理引擎 增量添加三元组')
bot.kg.add_triple_value(data={"data": [{"entity": "华为P40", "property": "价格", "value": "4488", "unit": "元"},
                                       {"entity": "华为P40Pro", "property": "价格", "value": "5988", "unit": "元"},
                                       {"entity": "华为P40", "property": "电池容量", "value": "3800", "unit": "毫安时"},
                                       {"entity": "华为P40Pro", "property": "电池容量", "value": "4200", "unit": "毫安时"},
                                       {"entity": "华为P40", "property": "拍照效果", "value": "可以满足您平时的拍照需求"},
                                       {"entity": "华为P40Pro", "property": "拍照效果", "value": "基本可以用于专业摄影"}
                                       ]})

# 知识推理引擎 增量添加语料
print('\n知识推理引擎 增量添加语料')
bot.kg.add_property_corpus(data={"data": [{"name": "价格", "corpus": "多少钱"},
                                          {"name": "价格", "corpus": "怎么卖呢"},
                                          {"name": "价格", "corpus": "最低多少"},
                                          {"name": "电池容量", "corpus": "续航怎么样"},
                                          {"name": "电池容量", "corpus": "待机多久"},
                                          {"name": "拍照效果", "corpus": "拍照咋样"}
                                          ]})
bot.kg.train()

print('User: 华为P40价格?\nBot:' + bot.kg.query("华为P40价格", False).text)
print('User: 华为P40Pro多少钱?\nBot:' + bot.kg.query("华为P40Pro多少钱", False).text)
print('User:那电池容量呢?\nBot:' + bot.kg.query("那电池容量呢", False).text)

# 知识推理引擎 增量添加话术
print('\n知识推理引擎 增量添加话术')
bot.kg.update_property_speech(data={"data": [{"name": "价格",
                                              "speech": "亲亲，[XEON_ENTITY]的[XEON_PROPERTY]是[XEON_VALUE]呢"}]})
bot.kg.train()

print('User:华为P40价格?\nBot:' + bot.kg.query("华为P40价格", False).text)
print('User:华为P40Pro多少钱?\nBot:' + bot.kg.query("华为P40Pro多少钱", False).text)
print('User:那电池容量呢?\nBot:' + bot.kg.query("那电池容量呢", False).text)

# 知识推理引擎 增量添加实体和属性简介
print('\n知识推理引擎 增量添加实体和属性简介')
bot.kg.add_intro(data={"data": [{"type": "entity", "name": "华为P40", "intro": "华为P40搭载麒麟990 5G SoC芯片，凭借性能优势，带来更加疾速的使用体验。同时搭载多光谱色温传感器和AI AWB算法，带来更丰富准确的色彩效果，800万像素长焦摄像头，可实现3倍光学变焦、5倍混合变焦以及30倍数字变焦，长焦镜头搭载OIS+AIS防抖，不打扰，也能捕获你眼中的美。"},
                                {"type": "property", "name": "价格", "intro": "华为实行全国统一零售价"}]})
bot.kg.train()

print('User:华为P40?\nBot:' + bot.kg.query("华为P40", False).text)

# 知识推理引擎 增量添加同义词
print('\n知识推理引擎 增量添加同义词')
bot.kg.add_word_synonym("华为P40", ["P40", "HUAWEI P40"])
bot.kg.add_word_synonym("华为P40Pro", ["pro", "P40pro"])

print('对话整体效果展示')
bot.kg.publish()

print('User:价格5000以内的手机有哪些?\nBot:' + bot.kg.query("价格5000以内的手机", False).text)
print('User:介绍下P40。\nBot:' + bot.kg.query("P40", False).text)
print('User:它的续航呢?\nBot:' + bot.kg.query("它的电池容量呢", False).text)
print('User:那pro呢\nBot:' + bot.kg.query("那P40pro呢", False).text)
print('User:多少钱?\nBot:' + bot.kg.query("它多少钱", False).text)
print('User:那P40pro拍照咋样?\nBot:' + bot.kg.query("那P40pro拍照咋样", False).text)
