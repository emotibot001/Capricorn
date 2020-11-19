package com.emotibot.quick.start.simple.kg;

import com.alibaba.fastjson.JSONObject;
import com.emotibot.engine.core.Bot;
import com.emotibot.engine.entity.Answer;

public class KGDemo {
	
	public static void main(String[] args) {
		Bot bot = Bot.create_bot();
		//机器人appId
		System.out.println("appId:"+bot.getAppId());
		//训练知识图谱
		String kgDatas = "[{\"entity\": \"黄金会员\", \"property\": \"价格\", \"value\": \"188元\"}]";
		bot.kg.train(JSONObject.parseArray(kgDatas), null);
		
		String sentence = "黄金会员的价格是多少？";
		Answer answer = bot.kg.query(sentence, true);
		System.out.println("问题："+sentence);
		System.out.println("KG出话结果:" + answer.getText() + "\n出话信心分：" + answer.getScore());
	}
	
}
