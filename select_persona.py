#!/Users/lwong/Toolkits/Anaconda/bin/python

import json
import yaml
import sys, os, re

def find_keys_by_value(d, target_value):
    for k, v in d:
        if target_value == v:
            return k
    return None

def main(args):
    if len(args) <= 1:
        # Read yaml file
        with open("system_prompts.yaml", "r") as file:
            avail_prompts = yaml.safe_load(file)

        out_json = json.dumps({
            "items": [{
                "uid": f"{k}", 
                "title": f"{k}",
                "subtitle": avail_prompts[k],
                "arg": f"{k}"
            } for k in avail_prompts]
        }, indent=4, ensure_ascii=False, separators=(',',':'))
        print(out_json)
    else:
        # Read yaml file
        with open("system_prompts.yaml", "r") as file:
            avail_prompts = yaml.safe_load(file)
        
        if args[1] in avail_prompts:
            # Dump into active_system_prompt
            with open("active_system_prompt.txt", "w") as f:
                # yaml.safe_dump({args[1]: f"{avail_prompts[args[1]]}"}, file)
                f.write(avail_prompts[args[1]])
                
            with open("active_persona.txt", 'w') as f:
                f.write(args[1])


if __name__ == '__main__':
    args = sys.argv
    main(args)