from pathlib import Path

path = Path('../linux/test.txt')
content = path.read_text(encoding="utf-8")

char_count=len(content)
s_count=content.count(" ")
l_count=len(content.splitlines())
print("字符数：",char_count)
print("空格数:",s_count)
print("行数：",l_count)
