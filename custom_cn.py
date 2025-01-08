import re
import os

# 文件路径
js_file_path = 'PS5-UMTX-Jailbreak-main/document/en/ps5/payload_map.js'
html_file_path = 'PS5-UMTX-Jailbreak-main/document/en/ps5/index.html'

# 读取并修改 payload_map.js 文件
with open(js_file_path, 'r', encoding='utf-8') as file:
    content = file.readlines()  # 按行读取文件内容

# 逐行修改 payload_map.js 内容
for i, line in enumerate(content):
    if 'displayTitle' in line:  # 只处理包含 displayTitle 的行
        # 检查 displayTitle 中包含的关键字并添加对应的描述
        display_title_match = re.search(r'displayTitle:\s*"(.*?)"', line)
        if display_title_match:
            display_title = display_title_match.group(1).lower()
            if 'etahen' in display_title:
                content[i] = content[i].replace(display_title_match.group(1), display_title_match.group(1) + " (支持PS5游戏)")
            elif 'kstuff' in display_title:
                content[i] = content[i].replace(display_title_match.group(1), display_title_match.group(1) + " (支持PS4游戏)")
            elif 'byepervisor hen' in display_title:
                content[i] = content[i].replace(display_title_match.group(1), display_title_match.group(1) + " (HV)")
            elif 'libhijacker' in display_title:
                content[i] = content[i].replace(display_title_match.group(1), display_title_match.group(1) + " (解锁帧率)")
            elif 'ps5debug' in display_title:
                content[i] = content[i].replace(display_title_match.group(1), display_title_match.group(1) + " (金手指)")
            elif 'appcache' in display_title:
                content[i] = content[i].replace(display_title_match.group(1), display_title_match.group(1) + " (清缓存)")

# 将修改后的内容保存回文件
with open(js_file_path, 'w', encoding='utf-8') as file:
    file.writelines(content)
    print("payload_map.js 文件已成功保存！")

# 读取并修改 index.html 文件
if os.path.exists(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # 修改 id="run-jb" 的 <a> 标签中的文本
    modified_html_content = re.sub(r'(<a [^>]*id="run-jb"[^>]*>)(.*?)(</a>)', r'\1Jailbreak 开始\3', html_content)

    # 修改 id="run-wk-only" 的 <a> 标签中的文本，拼接 " 注入器"
    modified_html_content = re.sub(r'(<a [^>]*id="run-wk-only"[^>]*>)(.*?)(</a>)', r'\1\2 注入器\3', modified_html_content)

    # 保存修改后的 index.html 文件
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(modified_html_content)
        print("index.html 文件已成功保存！")
else:
    print(f"{html_file_path} 文件未找到！")
