#ファイル名
file_name = "kaigyou_del.txt"

with open(file_name, encoding="utf-8") as f:
    line = f.read().replace('\n', ' ').replace('. ', '.\n')
    
with open(file_name, mode="w", encoding="utf-8") as f:
    f.write(line)