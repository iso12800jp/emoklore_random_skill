import random
import unicodedata
import collections

# https://qiita.com/delicious-locomoco/items/1adfe3ede4247b72759d から引用
def left(digit, msg):
    for c in msg:
        if unicodedata.east_asian_width(c) in ('F', 'W', 'A'):
            digit -= 2
        else:
            digit -= 1
    return msg + ' ' * digit

ALL_TECHS_LIST = [
    ("検索", {"is_ex": False}),
    ("洞察", {"is_ex": False}),
    ("洞察", {"is_ex": False}),
    ("マッピング", {"is_ex": False}),
    ("直感", {"is_ex": False}),
    ("鑑定", {"is_ex": False}),
    ("観察眼", {"is_ex": False}),
    ("聞き耳", {"is_ex": False}),
    ("毒見", {"is_ex": False}),
    ("危機察知", {"is_ex": False}),
    ("[ex]霊感", {"is_ex": True}),
    ("社交術", {"is_ex": False}),
    ("ディベート", {"is_ex": False}),
    ("心理", {"is_ex": False}),
    ("魅了", {"is_ex": False}),
    ("専門知識", {"is_ex": False}),
    ("事情通", {"is_ex": False}),
    ("業界", {"is_ex": False}),
    ("スピード", {"is_ex": False}),
    ("ストレングス", {"is_ex": False}),
    ("アクロバット", {"is_ex": False}),
    ("ダイブ", {"is_ex": False}),
    ("武術", {"is_ex": False}),
    ("[ex]奥義", {"is_ex": True}),
    ("[ex]射撃", {"is_ex": True}),
    ("耐久", {"is_ex": False}),
    ("根性", {"is_ex": False}),
    ("医術", {"is_ex": False}),
    ("[ex]蘇生", {"is_ex": True}),
    ("技巧", {"is_ex": False}),
    ("芸術", {"is_ex": False}),
    ("操縦", {"is_ex": False}),
    ("暗号", {"is_ex": False}),
    ("電脳", {"is_ex": False}),
    ("隠匿", {"is_ex": False}),
    ("[ex]強運", {"is_ex": True})
]

LV_COSTS = {
    "normal": [1, 5, 15], 
    "ex": [2, 10, 30]
}

tmp_tech_list = []
for tech in ALL_TECHS_LIST:
    tmp_tech_list.append([tech[0], {"lv": 0, "cost": 0}])
choose_techs = collections.OrderedDict(tmp_tech_list)

tech_points = 30

while tech_points > 0:
    (choose_tech_name, choose_tech_type) = random.choice(ALL_TECHS_LIST)

    choose_lv = random.choices([1, 2, 3], weights=[15, 5, 1])[0]

    choose_cost = None
    if choose_tech_type["is_ex"]:
        choose_cost = LV_COSTS["ex"][choose_lv - 1]
    else:
        choose_cost = LV_COSTS["normal"][choose_lv - 1]
    
    if choose_techs[choose_tech_name]["lv"] == 0 and tech_points - choose_cost >= 0:
        tech_points -= choose_cost
        choose_techs[choose_tech_name]["lv"] = choose_lv
        choose_techs[choose_tech_name]["cost"] = choose_cost

print("\n[選択した技能]\n")

print("Skill".center(12) + " │ " + "Lv".center(6) + " │ " + "Cost".center(6))
print("─" * 13 + "┼" + "─" * 8 + "┼" +"─" * 7)
for tech in choose_techs.items():
    if tech[1]["lv"] > 0:
        print(
            left(12, tech[0]) + " │ " + 
            str(tech[1]["lv"]).rjust(6) + " │ " + 
            str(tech[1]["cost"]).rjust(6)
        )


# print("\n\n[すべての技能]\n")

# print("Skill".center(12) + " │ " + "Lv".center(6) + " │ " + "Cost".center(6))
# print("─" * 13 + "┼" + "─" * 8 + "┼" +"─" * 7)
# for choose_tech in choose_techs.items():
#     print(
#         left(12, choose_tech[0]) + " │ " + 
#         str(choose_tech[1]["lv"]).rjust(6) + " │ " + 
#         str(choose_tech[1]["cost"]).rjust(6)
#     )