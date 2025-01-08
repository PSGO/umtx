import re
import sys

def modify_payload_map(js_file_path, version):
    """Modify payload_map.js by adding a new entry for each etaHEN entry by copying and modifying the required fields."""
    try:
        # 读取 payload_map.js 文件内容
        with open(js_file_path, 'r', encoding='utf-8') as file:
            js_content = file.read()

        # 使用正则表达式匹配所有含有 "etaHEN" 的条目（忽略大小写）
        pattern = re.compile(r'(\s*{[^}]*?etaHEN[^}]*?}),?', re.IGNORECASE)

        # 查找所有包含 "etaHEN" 的条目
        matches = list(pattern.finditer(js_content))

        if not matches:
            print("No 'etaHEN' entries found to modify.")
            return

        # 在每个匹配的条目后面插入一个新条目
        modified_content = js_content
        offset = 0
        for i, match in enumerate(matches):
            start_idx = match.start()
            end_idx = match.end()

            # 提取现有条目内容
            existing_entry = js_content[start_idx:end_idx]

            # 使用正则提取 version 和 fileName
            version_match = re.search(r'version: "(.*?)"', existing_entry)
            file_name_match = re.search(r'fileName: "(.*?)"', existing_entry)

            if version_match and file_name_match:
                current_version = version_match.group(1)
                current_file_name = file_name_match.group(1)

                # 修改条目中的 fileName 和 version
                modified_entry = existing_entry.replace(current_file_name, "etaHENold.bin")
                modified_entry = modified_entry.replace(f'version: "{current_version}"', f'version: "{version}"')

                # 新增 displayTitle 修改，使用传入的版本号拼接
                modified_entry = re.sub(r'displayTitle: "(.*?)"', f'displayTitle: "etaHEN v{version}-old"', modified_entry)

                # 在原有条目的逗号后插入新条目
                modified_content = (modified_content[:end_idx + offset] +
                                    modified_entry +
                                    modified_content[end_idx + offset:])
                offset += len(modified_entry)  # 更新偏移量，防止插入过程中出现错位

        # 保存修改后的文件内容
        with open(js_file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)

        print("File updated successfully with new entries.")

    except FileNotFoundError:
        print(f"File not found: {js_file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # 从命令行获取版本号参数
    if len(sys.argv) != 2:
        print("Usage: python modify_payload_map.py <version>")
        sys.exit(1)

    version = sys.argv[1]
    js_file_path = 'PS5-UMTX-Jailbreak-main/document/en/ps5/payload_map.js'  # 请根据实际路径修改
    modify_payload_map(js_file_path, version)
