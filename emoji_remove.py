# -*- coding: utf-8 -*-

import re

def remove_emoji(target_string):
    emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                "]+", flags=re.UNICODE)
    return remove_string(emoji_pattern, target_string)

def remove_string(target_pattern, target_string):
    result = target_string
    try:
       result = re.sub(target_pattern, '', target_string)
    except Exception as msg:
        print(msg)
    return result
