# 从compiled_json或源码中获取function的offset
* extractFromJson.py用于从json文件抽取function offset  
* extractFromSourcecode.py用于从sourcecode中抽取function offset
## 用法
1. 修改对应.py文件中json/contract及输出目录绝对路径
2. 执行.py文件输出offset
   

例如0x0dd080b66c88c325601fa7c9d9d4b6a816b820b3地址下生成offset文档内容如下：
> [{'file_name': '6_6_RocketMinipoolBase.sol', 'offset': '5938:6124', 'function_name': 'getEffectiveDelegate'}, {'file_name': '6_6_RocketMinipoolBase.sol', 'offset': '3685:4221', 'function_name': 'delegateUpgrade'}, {'file_name': '6_6_RocketMinipoolBase.sol', 'offset': '5052:5186', 'function_name': 'setUseLatestDelegate'}, {'file_name': '6_6_RocketMinipoolBase.sol', 'offset': '4282:4881', 'function_name': 'delegateRollback'}, {'file_name': '6_6_RocketMinipoolBase.sol', 'offset': '5279:5390', 'function_name': 'getUseLatestDelegate'}, {'file_name': '6_6_RocketMinipoolBase.sol', 'offset': '5466:5576', 'function_name': 'getDelegate'}, {'file_name': '6_6_RocketMinipoolBase.sol', 'offset': '5681:5803', 'function_name': 'getPreviousDelegate'}, {'file_name': '6_6_RocketMinipoolBase.sol', 'offset': '2423:3409', 'function_name': 'initialise'}, {'file_name': '6_6_RocketMinipoolBase.sol', 'offset': '6899:7222', 'function_name': 'getContractAddress'}, {'file_name': '6_6_RocketMinipoolBase.sol', 'offset': '7749:7971', 'function_name': 'contractExists'}, {'file_name': '6_6_RocketMinipoolBase.sol', 'offset': '7292:7598', 'function_name': 'getRevertMessage'}]
