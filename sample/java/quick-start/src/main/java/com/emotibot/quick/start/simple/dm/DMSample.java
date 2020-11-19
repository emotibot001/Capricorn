package com.emotibot.quick.start.simple.dm;

import com.alibaba.fastjson.JSONObject;
import com.emotibot.engine.config.ConfigManager;
import com.emotibot.engine.core.Bot;

public class DMSample {
	
	public static void main(String[] args) {
		//机器人创建
//		Bot bot = Bot.create_bot("0297c1010f244a70822d287484a08809");
		Bot bot = Bot.create_bot();
		System.out.println("appId:"+bot.getAppId());
		
		//训练问答语料
		//String datas = "[{\"sq\": \"竹间你好\", \"lq\": [\"竹间你好呀\", \"竹间你好吗\"], \"answer\": [\"竹间是NLP宇宙第一\",\"宇宙第一\"]}]";
		//bot.qa.train(JSONObject.parseArray(datas));
		//问答出话
		//System.out.println("qa出话：" + bot.qa.query("竹间你好", false).getText());
		
		//qa发布
		//bot.qa.publish();
		//问答出话
		//System.out.println("qa线上出话：" + bot.qa.query("竹间你好", true).getText());
		
		//训练知识图谱
		//String kgDatas = "[{\"entity\": \"竹间\", \"property\": \"年龄\", \"value\": \"5\"}]";
		//bot.kg.train(JSONObject.parseArray(kgDatas), null);
		//知识图谱出话
		//System.out.println("kg出话：" + bot.kg.query("竹间的年龄", true).getText());
		//未知回复出话
		//System.out.println("kg出话：" + bot.qa.query("未知回复", false).getText());
		
		//加载任务
//		bot.te.load("./src/main/resources/dm/taskengine.json");
		//bot.te.editor(null, true);
		//TE出话
		//System.out.println("te出话：" + bot.te.query("我要买火车票").getText());
		//System.out.println("te出话：" + bot.te.query("北京").getText());
		//System.out.println("te出话：" + bot.te.query("是的").getText());
		
		String dmDatas = "[{\"qa\": 90}, {\"kg\": 92}, {\"te\": 60}]";
		bot.dm.load(JSONObject.parseArray(dmDatas), null);

		System.out.println("对话管理出话：" + bot.dm.query("竹间的年龄").getText());
		System.out.println("对话管理出话：" + bot.dm.query("竹间你好").getText());
		System.out.println("对话管理出话：" + bot.dm.query("我要买火车票").getText());
		System.out.println("对话管理出话：" + bot.dm.query("北京").getText());
		System.out.println("对话管理出话：" + bot.dm.query("是的").getText());
		
		//生成二维码到指定目录
		//bot.dm.qrcode()
	}
}
