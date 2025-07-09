#!/usr/bin/env python3

import re
import os

def find_params(content):
    # Find all unique @PARAM@ in the template
    return sorted(set(re.findall(r'@(\w+)@', content)))

def prompt_params(params):
    values = {}
    for p in params:
        values[p] = input(f"Enter value for {p}: ")
    return values

def replace_params(content, values):
    def repl(match):
        key = match.group(1)
        return values.get(key, match.group(0))
    return re.sub(r'@(\w+)@', repl, content)

def main():
    template_path = os.path.join(
        os.path.dirname(__file__),
        '..', 'ecf', 'defs', 'aqm_cycled_realtime.def'
    )
    output_path = os.path.join(
        os.path.dirname(__file__),
        '..', 'test', 'output_test1.dev'
    )
    with open(template_path, 'r') as f:
        content = f.read()
    params = find_params(content)
    values = prompt_params(params)
    result = replace_params(content, values)
    with open(output_path, 'w') as f:
        f.write(result)
    print(f"Output written to {output_path}")

if __name__ == "__main__":
    main()
