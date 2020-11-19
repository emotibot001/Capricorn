package com.emotibot.quick.start.simple.te;

import com.emotibot.engine.core.Bot;
import com.emotibot.engine.entity.Answer;

public class TEDemo{
	
	public static void main(String[] args) {
		//创建机器人
		Bot bot = Bot.create_bot();
		//机器人ID
		System.out.println("appId:"+bot.getAppId());
		//购买火车票场景
		//触发多轮
		query("我要买火车票", bot);
		//确认地点
		query("北京", bot);
		//确认时间
		query("是的", bot);
	}
	
	/**
	 * 查询多轮出话
	 * @param sentence 问题
	 * @param bot 机器人
	 */
	public static void query(String sentence, Bot bot) {
		try {
			Answer answer = bot.te.query(sentence);
			System.out.println("问题："+sentence);
			System.out.println("TE出话结果:" + answer.getText() + "\n出话信心分：" + answer.getScore()+"\n");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	
	
}
