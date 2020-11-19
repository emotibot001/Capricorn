package com.emotibot.quick.start.simple.qa;

import com.alibaba.fastjson.JSONArray;
import com.emotibot.engine.core.Bot;
import com.emotibot.engine.entity.Answer;

public class QaTest{
	
	public static void main(String[] args) {
		Bot bot = Bot.create_bot();
		trainForFile(bot);
//		publish(bot);
		queryQaList(bot);
		query(bot);
//		export(bot);
	}
	
	
	
	public static void trainForFile(Bot bot) {
		boolean b= bot.qa.train("./config/银行行业标准问.xlsx", null, false);
	}
	
	public static void publish(Bot bot) {
		boolean b = bot.qa.publish();
		System.out.println(b);
	}
	
	public static void queryQaList(Bot bot) {
		JSONArray arr = bot.qa.qa_list();
		System.out.println("问题列表："+arr);
	}
	
	public static void query(Bot bot) {
		Answer result = bot.qa.query("什么是账单日", false);
		System.out.println("qa出话：" + result);
	}
	
	public static void export(Bot bot) {
		bot.qa.export("./data/问答.xlsx", "./data/语料.xlsx");
	}
}
