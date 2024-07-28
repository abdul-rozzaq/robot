import json


def process_line(line):
    parts = [x.replace(' ', '').replace(';', '').strip() for x in line.split('\t') if x.strip()]
    if len(parts) == 2 and len(parts[0]) == 14:
        return parts
    return None


def _filter_data(file_name):
    step = 0
    result = []

    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            step += 1
            filtered_line = process_line(line)
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

    data = _filter_data(input_file)
    save_to_json(data, output_file)

    print('Done !')
