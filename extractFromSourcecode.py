import re
import os

# 定义用于提取函数和合约的正则表达式
function_pattern = re.compile(r'\bfunction\s+([^\s(]+)\s*\(')
contract_pattern = re.compile(r'\b(abstract\s+contract|contract)\s+([^\s{]+)')  

# 文件名
contract_path = 'D:/pytest/sourcemap/contract3'  # 示例路径，需要根据实际情况调整
output_path_unique = 'D:/pytest/sourcemap/function_loc'  # 示例输出路径，需要根据实际情况调整

def find_next_char_index(string, index):
    try:
        index_semicolon = string.index(';', index)
    except ValueError:
        index_semicolon = len(string)

    try:
        index_brace = string.index('{', index)
    except ValueError:
        index_brace = len(string)

    return min(index_semicolon, index_brace)

def find_end_brace(content, start_index):
    brace_stack = []
    for index, char in enumerate(content[start_index:], start=start_index):
        if char == '{':
            brace_stack.append('{')
        elif char == '}':
            if brace_stack:  # 在尝试弹出之前检查栈是否为空
                brace_stack.pop()
                if not brace_stack:  # 当栈为空时，找到了匹配的结束大括号
                    return index
            else:  # 如果栈为空，意味着没有与之匹配的开启大括号
                break  # 提前退出循环
    return None  # 如果没有找到匹配的结束大括号，返回None

# 遍历文件夹中的文件
for root, ds, fs in os.walk(contract_path):
    os.chdir(root)
    for f in fs:
        if f.endswith('.sol'):
            fullname = os.path.join(root, f)
            with open(fullname, 'r', encoding='utf-8') as file:
                content = file.read()

            # 初始化存储列表
            items_info = []

            # 处理合约
            contract_matches = list(contract_pattern.finditer(content))
            for match in contract_matches:
                contract_name = match.group(2)
                start_pos = match.start()
                end_pos = find_end_brace(content, content.find('{', start_pos))
                if end_pos:
                    items_info.append({
                        'file_name': f,
                        'offset': f'{start_pos}:{end_pos+1}',
                        'item_name': contract_name,
                        'type': 'contract'
                    })

            # 处理函数
            matches = list(function_pattern.finditer(content))
            for match in matches:
                function_name = match.group(1)
                start_pos = match.start()
                end_pos = find_end_brace(content, content.find('{', start_pos))
                if content[find_next_char_index(content,start_pos)]=="{":
                    items_info.append({
                        'file_name': f,
                        'offset': f'{start_pos}:{end_pos+1}',
                        'item_name': function_name,
                        'type': 'function'
                    })
                else:
                    # 如果没有找到大括号，将偏移量设置为到第一个分号的位置
                    end_pos = content.find(';', start_pos)
                    if end_pos != -1:
                        items_info.append({
                            'file_name': f,
                            'offset': f'{start_pos}:{end_pos+1}',
                            'item_name': function_name,
                            'type': 'function'
                        })

            # 排序
            items_info.sort(key=lambda x: int(x['offset'].split(':')[0]))

            # 写入输出文件
            if not os.path.exists(output_path_unique):
                os.makedirs(output_path_unique)
            output_file_path = os.path.join(output_path_unique, os.path.basename(root) + '.txt')
            with open(output_file_path, 'w', encoding='utf-8') as file:
                for item in items_info:
                    file.write(f"{item}\n")
