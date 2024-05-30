import json
import argparse

def convert_neostore_to_json(neostore_file):
    with open(neostore_file, 'r') as f:
        neostore_data = f.read().strip()

    apps = []
    favourite_apps = []
    for app_str in neostore_data.split('>'):
        app_data = app_str.strip('}')
        app_data = app_data + '}'
        app_json = json.loads(app_data)
        apps.append(app_json)
        if app_json.get('favorite', False):
            favourite_apps.append(app_json['packageName'])

    return favourite_apps

def main():
    parser = argparse.ArgumentParser(description="Convert Neostore xts files into JSON format")
    parser.add_argument("--input", help="Input Neostore xts file", required=True)
    parser.add_argument("--output", help="Output file", required=True)
    args = parser.parse_args()

    neostore_file = args.input
    output_file = args.output

    if not output_file.endswith('.json'):
        output_file += '.json'

    favourite_apps = convert_neostore_to_json(neostore_file)

    output_json = {
        "favouriteApps": favourite_apps
    }

    with open(output_file, 'w') as f:
        json.dump(output_json, f, indent=4)

if __name__ == "__main__":
    main()
