package com.emotibot.quick.start.simple.qa;

import com.alibaba.fastjson.JSONArray;
import com.emotibot.engine.core.Bot;
import com.emotibot.engine.entity.Answer;

public class QaDemo{
	
	public static void main(String[] args) {
		//创建机器人
		Bot bot = Bot.create_bot();
		//机器人ID
		System.out.println("appId:"+bot.getAppId());
		//上传语料并训练
		bot.qa.train("./config/银行行业标准问.xlsx", null, false);
		
		//FAQ出话
		String sentence = "什么是账单日"; 
		Answer answer = bot.qa.query(sentence, false);
		System.out.println("问题："+sentence);
		System.out.println("FAQ出话结果：" + answer.getText() + "\n出话信心分：" + answer.getScore());
	}
	
	
	/**
	 * 发布
	 * @param bot
	 */
	public static void publish(Bot bot) {
		boolean b = bot.qa.publish();
		System.out.println(b);
	}
	
	/**
	 * 查询FAQ列表
	 * @param bot
	 */
	public static void queryQaList(Bot bot) {
		JSONArray arr = bot.qa.qa_list();
		System.out.println("问题列表："+arr);
	}
	
	/**
	 * 导出FAQ
	 * @param bot
	 */
	public static void export(Bot bot) {
		bot.qa.export("./data/问答.xlsx", "./data/语料.xlsx");
	}
}
