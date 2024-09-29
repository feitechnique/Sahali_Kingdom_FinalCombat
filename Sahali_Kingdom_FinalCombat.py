import random
import time

def attack(name):
    attacks = ["踢", "打拳", "抱摔", "头槌", "肘击", "膝撞"]
    attack_type = random.choice(attacks)
    damage = random.randint(5, 10)
    return attack_type, damage

def use_skill(name):
    skills = {
        "葛飞": "龙卷风腿",
        "小猪": "野蛮冲撞",
        "小鑫": "暗影突袭"
    }
    skill_name = skills[name]
    skill_damage = random.randint(10, 20)
    return skill_name, skill_damage

def use_ultimate_skill(name):
    ultimates = {
        "葛飞": "神龙天降·九霄雷霆",
        "小猪": "猪王之怒·猪笼防御",
        "小鑫": "暗影统治·奥恩护体"
    }
    ultimate_name = ultimates[name]
    if name == "小鑫":
        return ultimate_name, 25  # 返回恢复量而不是伤害
    if name == "小猪":
        return ultimate_name, 2  # 返回持续回合数
    ultimate_damage = random.randint(20, 30)
    return ultimate_name, ultimate_damage

def display_health_bar(name, health, max_health=100):
    bar_length = 20
    filled_length = int(bar_length * health / max_health)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f"{name}的血量: [{bar}] {health}/{max_health}")

def game():
    gefei_health = 100
    pig_health = 100
    xiaoxin_health = 100
    gefei_ultimate = True
    pig_ultimate = True
    xiaoxin_ultimate = True
    round_count = 0
    pig_buff_rounds = 0

    while (gefei_health > 0 and (pig_health > 0 or xiaoxin_health > 0)) or \
          (pig_health > 0 and (gefei_health > 0 or xiaoxin_health > 0)) or \
          (xiaoxin_health > 0 and (gefei_health > 0 or pig_health > 0)):
        round_count += 1
        time.sleep(1)
        print("\n")
        display_health_bar("葛飞", gefei_health)
        display_health_bar("小猪", pig_health)
        display_health_bar("小鑫", xiaoxin_health)

        if pig_buff_rounds > 0:
            pig_buff_rounds -= 1
            print(f"猪王之怒·猪笼防御还剩 {pig_buff_rounds} 回合")
            if pig_buff_rounds == 0:
                print("猪王之怒·猪笼防御已经消失！")

        # 葛飞的回合
        if gefei_health > 0:
            ultimate_chance = 0.1 if round_count <= 2 else 0.5
            if gefei_ultimate and random.random() < ultimate_chance:
                ultimate_name, ultimate_damage = use_ultimate_skill("葛飞")
                target = random.choice(["小猪", "小鑫"])
                if target == "小猪":
                    damage = ultimate_damage // 2 if pig_buff_rounds > 0 else ultimate_damage
                    pig_health = max(0, pig_health - damage)
                    print(f"葛飞对小猪使用终极技能{ultimate_name}，造成了{damage}点伤害！")
                else:
                    xiaoxin_health = max(0, xiaoxin_health - ultimate_damage)
                    print(f"葛飞对小鑫使用终极技能{ultimate_name}，造成了{ultimate_damage}点伤害！")
                gefei_ultimate = False
            elif random.random() < 0.3:  # 30% 概率使用普通技能
                skill_name, skill_damage = use_skill("葛飞")
                target = random.choice(["小猪", "小鑫"])
                if target == "小猪":
                    damage = skill_damage // 2 if pig_buff_rounds > 0 else skill_damage
                    pig_health = max(0, pig_health - damage)
                    print(f"葛飞对小猪使用技能{skill_name}，造成了{damage}点伤害！")
                else:
                    xiaoxin_health = max(0, xiaoxin_health - skill_damage)
                    print(f"葛飞对小鑫使用技能{skill_name}，造成了{skill_damage}点伤害！")
            else:
                gefei_attack, gefei_damage = attack("葛飞")
                target = random.choice(["小猪", "小鑫"])
                if target == "小猪":
                    damage = gefei_damage // 2 if pig_buff_rounds > 0 else gefei_damage
                    pig_health = max(0, pig_health - damage)
                    print(f"葛飞对小猪使用{gefei_attack}，造成了{damage}点伤害！")
                else:
                    xiaoxin_health = max(0, xiaoxin_health - gefei_damage)
                    print(f"葛飞对小鑫使用{gefei_attack}，造成了{gefei_damage}点伤害！")

        # 小猪的回合
        if pig_health > 0:
            ultimate_chance = 0.1 if round_count <= 2 else 0.5
            if pig_ultimate and random.random() < ultimate_chance:
                ultimate_name, buff_duration = use_ultimate_skill("小猪")
                pig_buff_rounds = buff_duration
                print(f"小猪使用终极技能{ultimate_name}，获得了{buff_duration}回合的50%减伤效果！")
                pig_ultimate = False
            elif random.random() < 0.3:  # 30% 概率使用普通技能
                skill_name, skill_damage = use_skill("小猪")
                target = random.choice(["葛飞", "小鑫"])
                if target == "葛飞":
                    gefei_health = max(0, gefei_health - skill_damage)
                    print(f"小猪对葛飞使用技能{skill_name}，造成了{skill_damage}点伤害！")
                else:
                    xiaoxin_health = max(0, xiaoxin_health - skill_damage)
                    print(f"小猪对小鑫使用技能{skill_name}，造成了{skill_damage}点伤害！")
            else:
                pig_attack, pig_damage = attack("小猪")
                target = random.choice(["葛飞", "小鑫"])
                if target == "葛飞":
                    gefei_health = max(0, gefei_health - pig_damage)
                    print(f"小猪对葛飞使用{pig_attack}，造成了{pig_damage}点伤害！")
                else:
                    xiaoxin_health = max(0, xiaoxin_health - pig_damage)
                    print(f"小猪对小鑫使用{pig_attack}，造成了{pig_damage}点伤害！")

        # 小鑫的回合
        if xiaoxin_health > 0:
            ultimate_chance = 0.1 if round_count <= 2 else 0.5
            if xiaoxin_ultimate and random.random() < ultimate_chance:
                ultimate_name, heal_amount = use_ultimate_skill("小鑫")
                xiaoxin_health = min(100, xiaoxin_health + heal_amount)
                print(f"小鑫使用终极技能{ultimate_name}，恢复了{heal_amount}点生命值！")
                xiaoxin_ultimate = False
            elif random.random() < 0.3:  # 30% 概率使用普通技能
                skill_name, skill_damage = use_skill("小鑫")
                target = random.choice(["葛飞", "小猪"])
                if target == "葛飞":
                    gefei_health = max(0, gefei_health - skill_damage)
                    print(f"小鑫对葛飞使用技能{skill_name}，造成了{skill_damage}点伤害！")
                else:
                    damage = skill_damage // 2 if pig_buff_rounds > 0 else skill_damage
                    pig_health = max(0, pig_health - damage)
                    print(f"小鑫对小猪使用技能{skill_name}，造成了{damage}点伤害！")
            else:
                xiaoxin_attack, xiaoxin_damage = attack("小鑫")
                target = random.choice(["葛飞", "小猪"])
                if target == "葛飞":
                    gefei_health = max(0, gefei_health - xiaoxin_damage)
                    print(f"小鑫对葛飞使用{xiaoxin_attack}，造成了{xiaoxin_damage}点伤害！")
                else:
                    damage = xiaoxin_damage // 2 if pig_buff_rounds > 0 else xiaoxin_damage
                    pig_health = max(0, pig_health - damage)
                    print(f"小鑫对小猪使用{xiaoxin_attack}，造成了{damage}点伤害！")

    # 战斗结束，宣布获胜者
    if gefei_health > 0:
        print("葛飞获胜！")
    elif pig_health > 0:
        print("小猪获胜！")
    else:
        print("小鑫获胜！")

if __name__ == "__main__":
    game()