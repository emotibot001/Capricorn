package com.emotibot.quick.start.simple.ner;

import java.util.ArrayList;
import java.util.List;

import com.alibaba.fastjson.JSONArray;
import com.emotibot.engine.core.Bot;
import com.emotibot.engine.core.PredictAnswer;

public class NerDemo{
	
	private static String sentence = "我要去北京，帮我订下周三晚上8点的车票, 从上海出发，联系电话：13212341234";
	
	public static void main(String[] args) {
		Bot bot = Bot.create_bot();
		predict(bot);
		//get_parsers(bot);
	}
	
	/**
	 * 获取所有解析器
	 * @param bot
	 */
	public static void get_parsers(Bot bot) {
		JSONArray result = bot.ner.get_parsers();
		System.out.println("result=" + result);
	}
	
	/**
	 * parsers中的parserId 可以通过
	 * @param bot
	 */
	public static void predict(Bot bot) {
		List<String> parsers = new ArrayList<String>();
		parsers.add("transport@1");
		parsers.add("chrono@1");
		parsers.add("phone@1");
		List<PredictAnswer> results = bot.ner.predict(sentence, parsers);
		results.forEach((result) -> {
			System.out.println(("提取到了：" + result.slot_content + "-----" + result.slot_name + "(" + result.slot_desc.replace("\n", "") + "); "));
		});
	}
	
}
