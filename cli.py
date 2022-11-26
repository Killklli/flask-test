"""CLI script for running seed generation."""
import argparse
import codecs
import json
import pickle
import random
import sys
import os
from randomizer.Fill import Generate_Spoiler
from randomizer.Settings import Settings
from randomizer.SettingStrings import decrypt_setting_string
from randomizer.Spoiler import Spoiler


def generate(generate_settings, file_name):
    """Gen a seed and write the file to an output file."""
    settings = Settings(generate_settings)
    spoiler = Spoiler(settings)
    Generate_Spoiler(spoiler)
    encoded = codecs.encode(pickle.dumps(spoiler), "base64").decode()
    with open(file_name, "w") as outfile:
        outfile.write(encoded)


def main(arg1, arg2):
    """CLI Entrypoint for generating seeds."""
    # presets = json.load(open("static/presets/preset_files.json"))
    # default = json.load(open("static/presets/default.json"))
    # found = False
    # for file in presets.get("progression"):
    #     with open("static/presets/" + file, "r") as preset_file:
    #         data = json.load(preset_file)
    #         if "Season 1 Race Settings" == data.get("name"):
    #             setting_data = default
    #             for key in data:
    #                 setting_data[key] = data[key]
    #             setting_data.pop("name")
    #             setting_data.pop("description")
    #             found = True
    # if found is False:
    #     sys.exit(2)
    loaded_data = os.environ["POST_BODY"]
    print(loaded_data)
    setting_data = json.loads(loaded_data)
    print(setting_data)
    setting_data["seed"] = random.randint(0, 100000000)
    generate(setting_data, "out.lanky")


if __name__ == "__main__":
    main(None, None)
