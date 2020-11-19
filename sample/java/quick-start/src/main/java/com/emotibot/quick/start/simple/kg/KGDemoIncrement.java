package com.emotibot.quick.start.simple.kg;

import com.alibaba.fastjson.JSONArray;
import com.emotibot.engine.core.Bot;
import com.emotibot.engine.entity.Answer;
import com.emotibot.engine.entity.BfEngineException;
import com.emotibot.engine.util.FileUtil;

public class KGDemoIncrement {
	
	public static void main(String[] args) throws BfEngineException {
		Bot bot = Bot.create_bot();
		//知识推理引擎 增量添加三元组
		System.out.println("知识推理引擎 增量添加三元组");
		JSONArray datas = fileToJsonArray("./src/main/resources/kg/kg-triple-value.json");
		bot.kg.add_triple_value(datas);
		
		System.out.println("知识推理引擎 增量添加语料");
		JSONArray props = fileToJsonArray("./src/main/resources/kg/kg-property-corpus.json");
		bot.kg.add_property_corpus(props);
		
		bot.kg.train(null, null);
		
		System.out.println("User: 华为P40价格?\\nBot:" + bot.kg.query("华为P40价格", false).getText());
		System.out.println("User: 华为P40Pro多少钱?\\nBot:" + bot.kg.query("华为P40Pro多少钱", false).getText());
		System.out.println("User:那电池容量呢?\\nBot:" + bot.kg.query("那电池容量呢", false).getText());
		
		System.out.println("知识推理引擎 增量添加话术");
		JSONArray speechs = fileToJsonArray("./src/main/resources/kg/kg-property-speech.json");
		bot.kg.update_property_speech(speechs);
		
		bot.kg.train(null, null);
		
		System.out.println("User: 华为P40价格?\\nBot:" + bot.kg.query("华为P40价格", false).getText());
		System.out.println("User: 华为P40Pro多少钱?\\nBot:" + bot.kg.query("华为P40Pro多少钱", false).getText());
		System.out.println("User:那电池容量呢?\\nBot:" + bot.kg.query("那电池容量呢", false).getText());
		
		System.out.println("知识推理引擎 增量添加实体和属性简介");
		JSONArray intros = fileToJsonArray("./src/main/resources/kg/kg-add-intro.json");
		bot.kg.add_intro(intros);
		
		bot.kg.train(null, null);
		
		System.out.println("User: 华为P40?\\nBot:" + bot.kg.query("华为P40", false).getText());
		
		System.out.println("知识推理引擎 增量添加同义词");
		JSONArray synonym1 = new JSONArray();
		synonym1.add("P40");
		synonym1.add("HUAWEI P40");
		JSONArray synonym2 = new JSONArray();
		synonym2.add("pro");
		synonym2.add("P40pro");
		bot.kg.add_word_synonym("华为P40", synonym1);
		bot.kg.add_word_synonym("华为P40Pro", synonym2);
		
		bot.kg.publish();
		
		System.out.println("User: 价格5000以内的手机有哪些?\\nBot:" + bot.kg.query("价格5000以内的手机", false).getText());
		System.out.println("User: 介绍下P40?\\nBot:" + bot.kg.query("P40", false).getText());
		System.out.println("User: 它的续航呢?\\nBot:" + bot.kg.query("它的电池容量呢", false).getText());
		System.out.println("User: 那pro呢?\\nBot:" + bot.kg.query("那P40pro呢", false).getText());
		System.out.println("User: 多少钱?\\nBot:" + bot.kg.query("它多少钱", false).getText());
		System.out.println("User: 那P40pro拍照咋样?\\nBot:" + bot.kg.query("那P40pro拍照咋样", false).getText());/***/
	}
	
	public static JSONArray fileToJsonArray(String file) {
		String filecontent = FileUtil.loadFile(file);
		if(filecontent != null) {
			try {
				JSONArray arr = JSONArray.parseArray(filecontent);
				return arr;
			} catch (Exception e) {
			}
		}
		return new JSONArray();
	}
}
