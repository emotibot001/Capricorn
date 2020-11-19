package com.emotibot.quick.start.simple.kg;

import com.emotibot.engine.core.Bot;
import com.emotibot.engine.entity.Answer;

public class KGDemoSample {
	
	public static void main(String[] args) {
		Bot bot = Bot.create_bot();
		//机器人appId
		System.out.println("appId:"+bot.getAppId());
		//全量训练知识图谱
		//bot.kg.train_by_path("./src/main/resources/kg/知识图谱上传模板v2.02.xlsx", false);
		
		query("华为P40怎么卖的，多贵啊?", bot);
		query("摄像头像素是多少，我想要拍照清楚一些的", bot);
		query("内存是多大的", bot);
		query("待机是多久", bot);
		query("屏幕是多大的", bot);
	}
	
	public static void query(String sentence, Bot bot) {
		try {
			Answer answer = bot.kg.query(sentence, true);
			System.out.println("问题:" +sentence + "，kg出话:" + answer.getText());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
