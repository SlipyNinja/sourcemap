import re
import os

# 定义用于提取函数和合约的正则表达式
function_pattern = re.compile(r'\bfunction\s+([a-zA-Z0-9_]+)\s*\(')
contract_pattern = re.compile(r'\bcontract\s+([a-zA-Z0-9_]+)\s*')

# 文件名
contract_path = 'D:/pytest/sourcemap/contract3'  # 示例路径，需要根据实际情况调整
output_path_unique = 'D:/pytest/sourcemap/function_loc'  # 示例输出路径，需要根据实际情况调整

for root, ds, fs in os.walk(contract_path):
    os.chdir(root)
    for f in fs: 
        if f.endswith('.sol'):
            fullname = os.path.join(root, f)
            # Loading data 
            with open(fullname, 'r', encoding='utf-8') as file:
                content = file.read()

            # 初始化存储列表
            items_info = []

            # 查找所有匹配的合约
            contract_matches = list(contract_pattern.finditer(content))
            for match in contract_matches:
                # 合约名
                contract_name = match.group(1)
                # 查找合约定义结束的位置
                start_pos = match.start()
                end_pos = content.find('}', start_pos) + 1  # 包含结束的大括号
                # 将信息添加到列表中
                items_info.append({
                    'file_name': f,
                    'offset': f'{start_pos}:{end_pos}',
                    'item_name': contract_name,
                    'type': 'contract'
                })

            # 查找所有匹配的函数
            matches = list(function_pattern.finditer(content))
            for match in matches:
                # 函数名
                function_name = match.group(1)
                # 查找函数体结束的位置
                start_pos = match.start()
                end_pos = content.find('}', start_pos) + 1  # 包含结束的大括号
                # 将信息添加到列表中
                items_info.append({
                    'file_name': f,
                    'offset': f'{start_pos}:{end_pos}',
                    'item_name': function_name,
                    'type': 'function'
                })

            # 写入输出文件
            current_dir = os.path.abspath('.')
            dir_name = os.path.basename(current_dir)
            with open(os.path.join(output_path_unique, dir_name + '.txt'), 'w', encoding='utf-8') as file:
                file.writelines(str(items_info))
