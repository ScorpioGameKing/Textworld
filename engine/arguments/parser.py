import sys

def __get_value(index: int):
    value: str = sys.argv[index]
    
    if value.startswith('--') or value.startswith('-'):
        return True
    else: 
        return value

def parse_args():
    parsed_args = {}
    for i, a in enumerate(sys.argv):
        if a.startswith('--'):
            parsed_args[a[2:].replace("-", "_")] = __get_value(i + 1)
        elif a.startswith('-'):
            parsed_args[a[1:].replace("-", "_")] = __get_value(i + 1)
    return parsed_args