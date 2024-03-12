# 从compiled_json或源码中获取function的offset
* extractFromJson.py用于从json文件抽取function offset  
* extractFromSourcecode.py用于从sourcecode中抽取function及contract offset
## 用法
1. 修改对应.py文件中json/contract及输出目录绝对路径
2. 执行.py文件输出offset
   

例如0x1a666f2961642ec5f5a504C883283B0982EBcE53_CharlieGrinSunflowerBlue地址下生成offset文档内容如下：
> [{'file_name': '19_19_StorageSlotUpgradeable.sol', 'offset': '533:832', 'item_name': 'ERC1967', 'type': 'contract'}, {'file_name': '19_19_StorageSlotUpgradeable.sol', 'offset': '686:832', 'item_name': '_getImplementation', 'type': 'function'}, {'file_name': '19_19_StorageSlotUpgradeable.sol', 'offset': '843:1112', 'item_name': '_setImplementation', 'type': 'function'}, {'file_name': '19_19_StorageSlotUpgradeable.sol', 'offset': '1553:1694', 'item_name': 'getAddressSlot', 'type': 'function'}, {'file_name': '19_19_StorageSlotUpgradeable.sol', 'offset': '1798:1939', 'item_name': 'getBooleanSlot', 'type': 'function'}, {'file_name': '19_19_StorageSlotUpgradeable.sol', 'offset': '2043:2184', 'item_name': 'getBytes32Slot', 'type': 'function'}, {'file_name': '19_19_StorageSlotUpgradeable.sol', 'offset': '2288:2429', 'item_name': 'getUint256Slot', 'type': 'function'}]
