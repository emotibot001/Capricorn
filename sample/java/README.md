
## 安装方式
#### maven安装

将bf-engine-0.0.2-SNAPSHOT.jar放到硬盘中，如：D:\bf-engine-0.0.2-SNAPSHOT.jar，执行以下成功后，bf-engine-0.0.2-SNAPSHOT.jar会自动添加到本地maven仓库中。
```
mvn install:install-file -Dfile=D:\bf-engine-0.0.2-SNAPSHOT.jar -DgroupId=com.emotibot -DartifactId=bf-engine -Dversion=0.0.2-SNAPSHOT -Dpackaging=jar
```

## 使用方式
#### 在pom.xml中引入jar包
```
<dependency>
	<groupId>com.emotibot</groupId>
	<artifactId>bf-engine</artifactId>
	<version>0.0.2-SNAPSHOT</version>
</dependency>
```

#### 创建BOT
```
Bot bot = Bot.create_bot();
```

#### 问答管理
```
# 训练问答语料
String datas = "[{\"sq\": \"竹间你好\", \"lq\": [\"竹间你好呀\", \"竹间你好吗\"], \"answer\": [\"竹间是NLP宇宙第一\",\"宇宙第一\"]}]";
bot.qa.train(JSONObject.parseArray(datas));

# 训练问答语料
bot.qa.train(data={"data": [{"sq": "竹间你好", "lq": ["竹间你好呀", "竹间你好吗"], "answer": "竹间是中文NLP No. 1"}]})


# 问答发布
bot.qa.publish();

# 问答出话
Answer result = bot.qa.query("什么是账单日", false);
System.out.println("qa出话：" + result);


# 查询问题列表
bot.qa.qa_list();


# 导出FAQ问题和语料
bot.qa.export("./data/问答.xlsx", "./data/语料.xlsx");
```
