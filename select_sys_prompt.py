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
    current_prompt = os.environ.get('system_prompt', '')
    # Read yaml file
    with open("system_prompts.yaml", "r") as file:
        avail_prompts = yaml.safe_load(file)
    
    # Get top keys
    if len(args[-1]) == 0:            
        init_response = f"# Current prompt: \n---\n```\n{current_prompt}\n```\n"
        out_json = json.dumps({
            "response": init_response + "# Available Prompts \n---\n" + "\n".join([f"## `{r}`:\n```\n {avail_prompts[r]} \n```" for r in avail_prompts.keys()]) + f"\n```\n{args}\n```", 
        }, indent=4, ensure_ascii=False, separators=(',',':'))
        print(out_json)
        return 
    else:
        # If key is selected
        key = args[-1]
        if key in avail_prompts:
            out_json = json.dumps({
                "response": f"# Selected prompt: \n```\n{avail_prompts[key]}\n```", 
                "variables": {
                    "system_prompt": avail_prompts[key]
                }
            }, indent=4, ensure_ascii=False, separators=(',',':'))
            print(out_json)
            return
        else:
            out_json = json.dumps({
                "response": f"# Wrong input!"+ f"\n```\n{args}\n```"
            }, indent=4, ensure_ascii=False, separators=(',',':'))
            print(out_json)
    
    

if __name__ == '__main__':
    args = sys.argv
    main(args)
