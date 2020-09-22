import bf_engine

# 机器人创建
bot = bf_engine.init()

sentence = '不好意思，我现在没空，请稍后再给我打电话'
print('User: ' + sentence + "\n")
# 使用所有行为分类器预测
results = bot.act.predict(sentence=sentence)

for result in results:
    print('ACT： {}({})'.format(result.name, result.code))


print('*' * 100)

# 指定分类器预测

sentence = '哪位？打电话给我有什么事么？'
print('User: ' + sentence + "\n")

results = bot.act.predict(sentence=sentence, acts=['Why_call', 'Who_are_you'])

# 可以预测出 Who_are_you(询问来电原因)， How_much(询问对方身份)
for result in results:
    print('ACT： {}({})'.format(result.name, result.code))
