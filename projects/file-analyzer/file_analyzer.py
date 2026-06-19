from pathlib import Path

def analyze_file (file_path):
    path = Path(file_path)

    if not path.exists():
        print("该文件不存在")
        return
    if not path.is_file():
        print("这不是一个文件")
        return
    content=path.read_text(encoding="utf-8")
    char_count=len(content)
    line_count=content.count("\n")+1 if content else 0
    word_count=len(content.split())

    print(f"字符数：{char_count}")
    print(f"行数：{line_count}")
    print(f"单词数：{word_count}")

analyze_file("test.txt")

