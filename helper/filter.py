import json

def process_line(line, pinpp_len, passport_len):
    parts = [x.replace(' ', '').replace(';', '').strip() for x in line.split('\t') if x.strip()]
    if len(parts) == 2 and parts[1][0] == 'A' and \
       len(parts[0]) == pinpp_len and len(parts[1]) == passport_len and \
       parts[1][:2].isalpha() and parts[1][2:].isdigit():
        return parts
    return None

def _filter_data(file_name, pinpp_len, passport_len):
    step = 0
    result = []
    
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            step += 1
            filtered_line = process_line(line, pinpp_len, passport_len)
            if filtered_line:
                result.append(filtered_line)
    
    print(f'{step:4}.', len(result))            
    return result

def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def filter_data(name: str):
    pinpp_len = 14
    passport_len = 9
    
    input_file = f'text_data/{name}.txt'
    output_file = f'json_data/{name}.json'
    
    data = _filter_data(input_file, pinpp_len, passport_len)
    save_to_json(data, output_file)
    
    
    print('Done !')
    