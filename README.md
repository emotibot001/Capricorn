# 机器人工厂引擎
>>>

## 目录
* [安装方式](#安装方式)
* [使用方式](#使用方式)
* [Object Hierarchy](#ObjectHierarchy)

---
提供的功能有:
* 创建BOT
* 问答管理
* 知识图谱
* 任务引擎
* 意图引擎
* 对话管理
---

## 安装方式
#### pip安装
```shell
pip install -U bfengine
# 按照requirements 安装
# pip install -U -r requirements.txt
```
如果比较慢，可以使用清华的pip源：-i https://pypi.tuna.tsinghua.edu.cn/simple
要求Python 3.6以上,支持Linux,可以在CPU上运行

## 使用方式
```
1.快速上手：问答管理、知识图谱
```python
import bf_engine

# 机器人初始化(云端)
bot = bf_engine.init()

# 机器人创建(本地)
# bot = bf_engine.init(local=True)

# 训练意图语料
bot.intent.train(data={"data":[{"name": "听，音乐","corpus": ["高迪的歌来一首", "放tfboys的宠爱", "我想听音乐"]},{"name": "查，天气","corpus": ["今天空气污染程度", "今天什么天气"]}]})

# 意图测试
print('intent：' + str(bot.intent.query('今天天气如何')))

# 训练问答语料
bot.qa.train(data={"data": [{"sq": "竹间你好", "lq": ["竹间你好呀", "竹间你好吗"], "answer": "竹间是NLP宇宙第一"}]})

# 问答出话
print('qa出话：' +str(bot.qa.query('竹间你好')))

# 训练知识图谱
bot.kg.train(data={"data": [{"entity": "竹间", "property": "年龄", "value": "5"}]})

# 知识出话
print('kg出话: ' + bot.kg.query('竹间的年龄').text)

# test
test_set = bf_engine.TestSet([
    ('竹间你好', '竹间是NLP宇宙第一'),
    ('竹间你好吗', '竹间是NLP宇宙第一'),
    ('竹间的年龄', '竹间的年龄是5'),
    ('竹间的年龄是多少', '竹间的年龄是5'),
    ('今天天气如何', '查，天气'),
])
bot.qa.test(test_set).show()
bot.kg.test(test_set).show()
bot.dm.test(test_set).show()

```

2.任务引擎
```python
import bf_engine

# 机器人初始化
bot = bf_engine.init()
# 编辑任务
bot.te.editor(path='data/taskengine.json')


# 任务出话
print('te出话: ' + bot.te.query('我要买火车票').text)
print('te出话: ' + bot.te.query('北京').text)
print('te出话: ' + bot.te.query('是的').text)
```

3.对话管理
```python
import bf_engine

# 机器人初始化
bot = bf_engine.init()

# 机器人appid
print("appid: "+bot.app_id)

# 训练问答语料
bot.qa.train(data={"data": [{"sq": "竹间你好", "lq": ["竹间你好呀", "竹间你好吗"], "answer": "竹间是NLP宇宙第一"}]})

# 训练知识图谱
bot.kg.train(data={"data": [{"entity": "竹间", "property": "年龄", "value": "5"}]})

# 加载任务
bot.te.load(path='data/taskengine.json')
# 编辑任务
bot.te.editor()

bot.dm.load([{"qa": 90}, {"kg": 92}, {"qa": 60, "kg": 65}, {"te": 60}])
# or 需指定配置文件
# bot.dm.load_by_path(config_path='data/对话配置.json')
#

print("对话管理出话: " + bot.dm.query("今天天气如何").text)
print("对话管理出话: " + bot.dm.query("竹间的年龄").text)
print("对话管理出话: " + bot.dm.query("竹间你好").text)
print("对话管理出话: " + bot.dm.query("我要买火车票").text)
print("对话管理出话: " + bot.dm.query("北京").text)
print("对话管理出话: " + bot.dm.query("是的").text)

```

## Object Hierarchy

```
## 对象结构图
# *:方法; -: 对象
bf_engine
   *init
    -intent
      *train
      *query
      *test
   -qa
      *train
      *query
      *qa_list
      *question_list
      *corpus_list
      *test
   -kg
      *train
      *query
      *test
      *add_triple_value
      *add_intro
      *add_property_corpus
      *add_word_synonym
   -te
      *load
      *editor
      *train
      *query
      *test
   -dm
      *query
      *chat
      *test
```

