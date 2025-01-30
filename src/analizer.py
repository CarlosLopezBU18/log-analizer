import threading as th
from typing import List, Dict, Any
from utils import Level


def analize(parsed: List[Dict[str, str]]) -> Dict[str, Any]:
    if not parsed:
        return {'total_logs': 0, 'log_levels': {}, 'top_errors': [], 'first_log': None, 'last_log': None}

    total_logs: int = len(parsed)
    log_levels: Dict[str, int] = {}

    top_errors: List[Dict[str, str|int]] = []
    message_to_index: Dict[str, int] = {}

    first_log: str = parsed[0]['date'] + ' ' + parsed[0]['hour']
    last_log: str = parsed[-1]['date'] + ' ' + parsed[-1]['hour']

    max_index:int = 0
    for entry in parsed:

        curr_level = entry['level']
        if curr_level not in log_levels:
            log_levels[curr_level] = 1
        else:
            log_levels[curr_level] += 1

        if curr_level == Level.ERROR.name:
            curr_message:str = entry['message']
            
            if curr_message not in message_to_index:
                message_to_index[curr_message] = max_index
                top_errors.append({'message': curr_message, 'count': 1})
            else:
                index: int = message_to_index[curr_message]
                top_errors[index]['count'] += 1 

    return {
        'total_logs': total_logs,
        'log_levels': log_levels,
        'top_errors': top_errors,
        'first_log': first_log,
        'last_log': last_log
    }




