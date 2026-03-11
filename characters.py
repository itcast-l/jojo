"""
JoJo's Bizarre Adventure - 角色与替身能力数据模块
"""

PARTS = {
    1: "幽波纹的战士（ファントムブラッド）",
    2: "战斗潮流（戦闘潮流）",
    3: "星尘斗士（スターダストクルセイダース）",
    4: "不灭钻石（ダイヤモンドは砕けない）",
    5: "黄金之风（黄金の風）",
    6: "石之海（ストーンオーシャン）",
    7: "钢之球跑（スティール・ボール・ラン）",
    8: "乔乔利昂（ジョジョリオン）",
}

CHARACTERS = [
    {
        "name": "乔纳森·乔斯达",
        "name_jp": "ジョナサン・ジョースター",
        "part": 1,
        "stand": None,
        "ability": "波纹（ハモン）",
        "description": "乔斯达家族的第一代 JoJo，使用波纹能量与吸血鬼战斗。",
    },
    {
        "name": "约瑟夫·乔斯达",
        "name_jp": "ジョセフ・ジョースター",
        "part": 2,
        "stand": None,
        "ability": "波纹（ハモン）",
        "description": "乔纳森的孙子，天才式的战略头脑，善用陷阱和即兴发挥。",
    },
    {
        "name": "空条承太郎",
        "name_jp": "空条承太郎",
        "part": 3,
        "stand": "白金之星（スタープラチナ）",
        "ability": "时间停止（ザ・ワールド同等）、超高速度与力量",
        "description": "冷酷沉着的高中生，拥有强大的近战型替身白金之星。",
    },
    {
        "name": "东方仗助",
        "name_jp": "東方仗助",
        "part": 4,
        "stand": "疯狂钻石（クレイジー・ダイヤモンド）",
        "ability": "修复物体或生命（除自身外），近战攻击力极强",
        "description": "杜王町的高中生，性格热情，极度重视发型。",
    },
    {
        "name": "乔鲁诺·乔巴拿",
        "name_jp": "ジョルノ・ジョバァーナ",
        "part": 5,
        "stand": "黄金体验（ゴールド・エクスペリエンス）",
        "ability": "赋予生命、最终形态可将一切行为与意志归零",
        "description": "迪奥之子，立志成为黑道之王的少年。",
    },
    {
        "name": "空条徐伦",
        "name_jp": "空条徐倫",
        "part": 6,
        "stand": "石之自由（ストーン・フリー）",
        "ability": "将身体分解为线并自由操控",
        "description": "承太郎之女，在监狱中觉醒替身，寻找真相。",
    },
    {
        "name": "强尼·乔斯达",
        "name_jp": "ジョニィ・ジョースター",
        "part": 7,
        "stand": "旋转马蹄铁（タスク）",
        "ability": "发射无限旋转的指甲子弹，最终可穿透次元",
        "description": "前赛马骑手，为治好双腿踏上钢之球跑旅程。",
    },
    {
        "name": "东方定助",
        "name_jp": "東方定助",
        "part": 8,
        "stand": "软湿男孩（ソフト＆ウェット）",
        "ability": "发射抢夺特定性质的泡泡",
        "description": "失忆青年，在仙台市寻找自己的真实身份。",
    },
    {
        "name": "迪奥·布兰度",
        "name_jp": "DIO",
        "part": 3,
        "stand": "世界（ザ・ワールド）",
        "ability": "时间停止",
        "description": "乔纳森的宿敌，吸血鬼，拥有可停止时间的替身。",
    },
    {
        "name": "吉良吉影",
        "name_jp": "吉良吉影",
        "part": 4,
        "stand": "杀手皇后（キラークイーン）",
        "ability": "将物体变为炸弹，第二炸弹循环时间，第三炸弹无限爆炸",
        "description": "杜王町的连环杀手，渴望平静生活的变态。",
    },
]


def get_all_characters():
    """返回所有角色列表。"""
    return CHARACTERS


def get_characters_by_part(part_number):
    """根据部数返回该部的角色列表。"""
    return [c for c in CHARACTERS if c["part"] == part_number]


def get_character_by_name(name):
    """根据角色名称（中文或日文）查找角色，返回第一个匹配结果。"""
    name_lower = name.lower()
    for character in CHARACTERS:
        if name_lower in character["name"].lower() or name_lower in character["name_jp"].lower():
            return character
    return None


def search_by_ability(keyword):
    """根据替身能力关键字搜索角色列表。"""
    keyword_lower = keyword.lower()
    results = []
    for character in CHARACTERS:
        ability = character.get("ability") or ""
        stand = character.get("stand") or ""
        if keyword_lower in ability.lower() or keyword_lower in stand.lower():
            results.append(character)
    return results


def format_character(character):
    """格式化单个角色信息为可读字符串。"""
    part_name = PARTS.get(character["part"], f"第{character['part']}部")
    lines = [
        f"姓名: {character['name']}（{character['name_jp']}）",
        f"所在部: 第{character['part']}部 - {part_name}",
    ]
    if character.get("stand"):
        lines.append(f"替身: {character['stand']}")
    if character.get("ability"):
        lines.append(f"能力: {character['ability']}")
    lines.append(f"简介: {character['description']}")
    return "\n".join(lines)
