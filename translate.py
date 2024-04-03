from googletrans import Translator

translator = Translator()

# 待翻译的文本
text_to_translate = "Your text here."

# 翻译函数
def translate_text(text):
    translation = translator.translate(text, src='auto', dest='zh-cn')  # auto表示自动检测语言，zh-cn表示中文简体
    return translation.text

# 读取文本文件，逐行进行翻译并写入新文件
input_file = 'E:\IntellectualProperty-main\Data\专利名1.txt'
output_file = 'E:\IntellectualProperty-main\Data\专利名2.txt'

with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open(output_file, 'w', encoding='utf-8') as f:
    for line in lines:
        translated_text = translate_text(line.strip())
        f.write(translated_text + '\n')

print("Translation done.")
