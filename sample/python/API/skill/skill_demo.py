import bf_engine
import json


def query(sentence, bot):
    print("User: ", sentence)
    answer = bot.skill.query(sentence)
    print("Bot: ", str(answer.text))
    print("")


# 机器人创建
bot = bf_engine.init()

skill_list = bot.skill.skill_list()


# 打印了前三个。
for skill in skill_list[:4]:
    print(json.dumps(skill, ensure_ascii=False, indent=2))

# 技能开关打开
bot.skill.update_status(7, True)
bot.skill.update_status(3, True)
bot.skill.update_status(10, True)

# 技能出话
#星座运势
query("射手座明日运势怎么样", bot)

#防催宝典
query("妈妈催我做作业怎么办", bot)

#猜谜
query("我们玩猜谜语吧", bot)
