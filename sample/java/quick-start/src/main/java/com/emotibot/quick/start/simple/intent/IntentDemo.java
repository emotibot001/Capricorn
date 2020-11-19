package com.emotibot.quick.start.simple.intent;

import com.alibaba.fastjson.JSONArray;
import com.emotibot.engine.core.Bot;
import com.emotibot.engine.util.FileUtil;

public class IntentDemo{
	
	public static void main(String[] args) {
		Bot bot = Bot.create_bot();
//		bot.intent.trainForFile("./src/main/resources/提醒意图.xlsx", false);
		//训练意图语料
		train(bot);
		//关闭内置意图
//		bot.intent.close_inner_intents();
		//打开内置意图
//		bot.intent.open_inner_intents();
		//打开"通用"意图
//		bot.intent.open_intent_group("chat");
		//关闭"通用"意图
//		bot.intent.close_intent_group("chat");
		
		//意图测试
		System.out.println("intent：" + bot.intent.predict("提醒我吃饭", false));
		//意图测试
		System.out.println("intent：" + bot.intent.predict("太困了", false));
		//内置意图
		System.out.println("intent：" + bot.intent.predict("打开爱奇艺应用", false));
		//获取意图列表
		JSONArray intents = bot.intent.intents_list();
		System.out.println("intents：" + intents);
		
	}
	
	public static void open_intent_group(Bot bot) {
		bot.intent.open_intent_group("dadbf33b8aa64fe2b9d2ef96c4969309");
	}
	
	/**
	 * 训练意图语料
	 * @param bot
	 */
	public static void train(Bot bot) {
		String filecontent = FileUtil.loadFile("./src/main/resources/intent-train.json");
		if(filecontent != null) {
			try {
				JSONArray arr = JSONArray.parseArray(filecontent);
				bot.intent.trainForJson(arr, false);
			} catch (Exception e) {
			}
		}
	}
	
	
}
