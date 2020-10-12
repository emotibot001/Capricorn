# 机器人工厂引擎
Capricorn是竹间BF2020的核心对话引擎，内嵌了竹间自研的中文自然语言处理技术，主要功能包括语义问答，知识推理问答，多轮对话，以及整体的对话管理控制。在Capricorn上可以快速进行二次开发，大型企业可以将引擎快速的集成到自己公司已有的AI平台，加强语义理解和智能对话的能力，甚至轻松处理复杂的机器人对话场景。集成商以及IT开发者们，可以基于Capricorn引擎开发自己的对话解决方案，给更多的行业赋能。
通过Capricorn，您可以定制个性化的AI服务，打造个性化BOT平台，以及和已有系统做深度集成。并且在此之上，快速开发各类对话场景，例如客服服务，业务办理，企业助手，智能家居控制，语音技能等。

>>>

## 目录
* [安装方式](#安装方式)
* [使用方式](#使用方式)
* [Object Hierarchy](#ObjectHierarchy)

---
提供的功能有:
* 创建Bot
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
要求Python 3.6以上。

## 使用方式
####  创建Bot

```
import bf_engine
bot = bf_engine.init()
```

#### 问答管理
```
# 训练问答语料
bot.qa.train(data={"data": [{"sq": "竹间你好", "lq": ["竹间你好呀", "竹间你好吗"], "answer": "竹间是NLP宇宙第一"}]})

# 问答出话
print('qa出话：' +str(bot.qa.query('竹间你好')))
```

#### 知识图谱
```
# 训练知识图谱
bot.kg.train(data={"data": [{"entity": "竹间", "property": "年龄", "value": "5"}]})

# 知识出话
print('kg出话: ' + bot.kg.query('竹间的年龄').text)
```

#### 任务引擎

```
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

#### 意图引擎

```
# 内嵌意图
print("intent:"+str(bot.intent.predict("来一首音乐")))
print("intent:"+str(bot.intent.predict("打开爱奇艺软件")))
```
#### 对话管理
```
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

