import re
import os
# 定义用于提取函数的正则表达式
function_pattern = re.compile(r'\bfunction\s+([a-zA-Z0-9_]+)\s*\(')

# 用于存储所有函数信息的列表


# 文件名
contract_path = 'D:/pytest/sourcemap/contract'
output_path_unique = 'D:/pytest/sourcemap/function_loc'
for root, ds, fs in os.walk(contract_path):
    os.chdir(root)
    functions_info = []
    for f in fs: 
        if f.endswith('.sol'):
            fullname = os.path.join(root, f)
            fullname = fullname.replace("\\","/")
            root = root.replace("\\","/")
# Loading data 
            with open(fullname, 'r',encoding='utf-8') as file:
                content = file.read()

        # 查找所有匹配的函数
            matches = list(function_pattern.finditer(content))

        # 遍历所有匹配，提取函数名和位置信息
            for match in matches:
                # 函数名
                function_name = match.group(1)
                # 查找函数体结束的位置
                start_pos = match.start()
                # 尝试找到函数体的结束位置（基于大括号匹配）
                end_pos = content.find('}', start_pos) + 1  # 包含结束的大括号
                # 将信息添加到列表中
                functions_info.append({
                    'file_name': f,
                    'offset': f'{start_pos}:{end_pos}',
                    'function_name': function_name
                })
    current_dir = os.path.abspath('.')
    dir_name = os.path.basename(current_dir)
    with open(output_path_unique+'/'+dir_name+'.txt', 'w', encoding='utf-8') as file:
        file.writelines(str(functions_info))
# 输出提取到的信息

