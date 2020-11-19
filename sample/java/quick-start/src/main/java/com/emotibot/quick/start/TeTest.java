package com.emotibot.quick.start;

import com.emotibot.engine.core.Bot;
import com.emotibot.engine.entity.Answer;

public class TeTest{
	
	
	public static void main(String[] args) {
		Bot bot = Bot.create_bot();
		//load(bot);
		query(bot);
	}
	
	public static void load(Bot bot) {
		boolean b = bot.te.load("./src/main/resources/task-engine.json");
		System.out.println("load te result:" + b);
	}
	
	public static void query(Bot bot) {
		Answer a = bot.te.query("我要买火车票");
		System.out.println("query te result:" + a);
		a = bot.te.query("北京");
		System.out.println("query te result:" + a);
		a = bot.te.query("是的");
		System.out.println("query te result:" + a);
	}
	
	
	
}
