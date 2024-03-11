import json
import re
import os

# Function to simulate the extraction of "assembly" data from a given JSON structure
def extract_assembly_data(json_data):
    assembly_data = {}
    contracts = json_data.get("contracts", {})

    for file_name, contracts_in_file in contracts.items():
        for contract_name, contract_data in contracts_in_file.items():
            evm_data = contract_data.get("evm", {})
            assembly = evm_data.get("assembly", "")
            
            # Using file name and contract name as key to store assembly
            assembly_data[f"{file_name}:{contract_name}"] = {
                "assembly": assembly,
            }
            
    return assembly_data

# Function to process assembly data and extract unique function information
def process_assembly_data(assembly_data):
    extracted_data = []
    seen = set()

    for key, value in assembly_data.items():
        # print(value["assembly"])
        matches = pattern.findall(value["assembly"])

        for match in matches:
            # Create a unique key for each function based on file name and function name
            unique_key = (match[0], match[2])
            if unique_key not in seen:
                seen.add(unique_key)
                extracted_data.append({
                    "file_name": match[0],
                    "offset": match[1],
                    "function_name": match[2]
                })
        
    
    return extracted_data


# Regular expression pattern to find function names and offsets
pattern = re.compile(r'\"([^\"]+)\":(\d+:\d+).*function ([\w\d_]+)\(')

json_path = 'D:/pytest/sourcemap/compiled_info2'
output_path_unique = 'D:/pytest/sourcemap/function_loc'
for filename in os.listdir(json_path):
# Loading JSON data 
    with open(json_path+'/'+filename) as file:
        data = json.load(file)

    # Extract assembly data from the loaded JSON data
    assembly_data = extract_assembly_data(data)

    # Process the extracted assembly data to find unique functions
    unique_functions = process_assembly_data(assembly_data)

    # Output or save the result as needed
    print(unique_functions)  # Print a sample of the output


    with open(output_path_unique+'/'+filename[:-11]+'.txt', 'w', encoding='utf-8') as file:
        file.writelines(str(unique_functions))
