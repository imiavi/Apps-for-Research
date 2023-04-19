file_name = "kaigyou_del.txt"　#ファイル名

with open(file_name, encoding="utf-8") as f:
    line = f.read().replace('\n', ' ').replace('.', '.\n').replace('\n ', '\n')
    
with open(file_name, mode="w", encoding="utf-8") as f:
    f.write(line)
