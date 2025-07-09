import yaml
import re

def load_config(yaml_path):
    with open(yaml_path, 'r') as f:
        return yaml.safe_load(f)

def generate_def(template_path, config, output_path):
    with open(template_path, 'r') as f:
        content = f.read()
    # Replace all @KEY@ with config[KEY]
    def replacer(match):
        key = match.group(1)
        return str(config.get(key, match.group(0)))
    content = re.sub(r'@(\w+)@', replacer, content)
    with open(output_path, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python generate_suite_def.py <config.yaml> <template.def> <output.def>")
        sys.exit(1)
    config_path, template_path, output_path = sys.argv[1:4]
    config = load_config(config_path)
    generate_def(template_path, config, output_path)