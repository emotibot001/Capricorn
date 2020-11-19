package com.emotibot.quick.start.simple.act;

import java.util.List;

import com.alibaba.fastjson.JSONArray;
import com.emotibot.engine.core.Bot;
import com.emotibot.engine.entity.ActAnswer;

public class DialogueActDemo{
	
	/***
	 * 指定分类器数据
	 * Why_call：询问来电原因
	 * Who_are_you：询问对方身份
	 */
	private static final String datas = "[\"Why_call\",\"Who_are_you\"]";
	
	public static void main(String[] args) {
		Bot bot = Bot.create_bot();
		String sentence = "不好意思，我现在没空，请稍后再给我打电话";
		System.out.println("所有行为分类器预测的问题："+sentence);
		//使用所有行为分类器预测
		List<ActAnswer> results = bot.act.predict(sentence, null);
		printResult(results);
		
		System.out.println("*******************************************");
		
		sentence = "哪位？打电话给我有什么事么？";
		System.out.println("指定分类器预测的问题："+sentence);
		JSONArray arr = JSONArray.parseArray(datas);
		//指定分类器预测
		results = bot.act.predict(sentence, arr);
		//可以预测出 Why_call(询问来电原因)， Who_are_you(询问对方身份)
		printResult(results);
		
	}
	
	/**
	 * 打印查询结果
	 * @param results
	 */
	private static void printResult(List<ActAnswer> results) {
		results.forEach((result) -> {
			System.out.println(String.format("result:%s(%s)",result.getName(),result.getScore()));
		});
	}
	
}
