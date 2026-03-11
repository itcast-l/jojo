"""
JoJo's Bizarre Adventure - 角色与替身能力查询程序
"""

from characters import (
    PARTS,
    get_all_characters,
    get_characters_by_part,
    get_character_by_name,
    search_by_ability,
    format_character,
)


def print_separator(char="=", width=50):
    print(char * width)


def show_menu():
    print_separator()
    print("  JoJo的奇妙冒险 - 角色查询系统")
    print_separator()
    print("1. 查看所有角色")
    print("2. 按部数查询角色")
    print("3. 按名字查询角色")
    print("4. 按替身能力关键字搜索")
    print("5. 查看各部简介")
    print("0. 退出")
    print_separator()


def show_all_characters():
    characters = get_all_characters()
    print(f"\n共有 {len(characters)} 位角色:\n")
    for char in characters:
        part_name = PARTS.get(char["part"], f"第{char['part']}部")
        stand_info = f" / 替身: {char['stand']}" if char.get("stand") else " / 无替身（波纹使）"
        print(f"  [{char['part']}部] {char['name']}（{char['name_jp']}）{stand_info}")


def show_characters_by_part():
    print("\n可选部数:")
    for num, name in sorted(PARTS.items()):
        print(f"  {num}. {name}")
    try:
        part_num = int(input("\n请输入部数 (1-8): ").strip())
    except ValueError:
        print("请输入有效的数字。")
        return

    characters = get_characters_by_part(part_num)
    if not characters:
        print(f"第{part_num}部没有找到角色数据。")
        return

    part_name = PARTS.get(part_num, f"第{part_num}部")
    print(f"\n第{part_num}部「{part_name}」的角色:\n")
    for char in characters:
        print(format_character(char))
        print()


def show_character_by_name():
    name = input("\n请输入角色名（支持中文或日文）: ").strip()
    if not name:
        print("名字不能为空。")
        return

    character = get_character_by_name(name)
    if character:
        print()
        print(format_character(character))
    else:
        print(f"未找到名为「{name}」的角色。")


def show_search_by_ability():
    keyword = input("\n请输入替身/能力关键字: ").strip()
    if not keyword:
        print("关键字不能为空。")
        return

    results = search_by_ability(keyword)
    if not results:
        print(f"未找到包含「{keyword}」的替身或能力。")
        return

    print(f"\n找到 {len(results)} 个结果:\n")
    for char in results:
        print(format_character(char))
        print()


def show_parts_overview():
    print("\n《JoJo的奇妙冒险》各部简介:\n")
    for num, name in sorted(PARTS.items()):
        print(f"  第{num}部: {name}")


def main():
    print("\n欢迎使用 JoJo的奇妙冒险 角色查询系统！")
    while True:
        show_menu()
        choice = input("请选择功能: ").strip()
        if choice == "1":
            show_all_characters()
        elif choice == "2":
            show_characters_by_part()
        elif choice == "3":
            show_character_by_name()
        elif choice == "4":
            show_search_by_ability()
        elif choice == "5":
            show_parts_overview()
        elif choice == "0":
            print("\nYARE YARE DAZE... 再见！\n")
            break
        else:
            print("无效选项，请重新输入。")
        print()


if __name__ == "__main__":
    main()
