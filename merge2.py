#Resumo da opera: dentro do Workspace, haverá uma pasta chamada bags. Dentro dessa pasta, haverão várias pastas com o nome de sua respectiva bag, q estará dentro
#test
import os
import yaml
import subprocess

ROOT_DIR = "/home/nicolas/ws/bags"
MERGED_BAG_NAME = "merged_bag"
CONFIG_PATH = "merge_config.yaml"
decoyVariable = 0

def find_all_mcap_files(root_dir):
    """Recursively find all .mcap files inside subdirectories."""
    mcap_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".mcap"):
                mcap_files.append(os.path.join(dirpath, filename))
    return mcap_files

def write_merge_yaml(output_uri, yaml_path):
    """Create the YAML config file for ros2 bag convert -o."""
    config = {
        "output_bags": [
            {
                "uri": output_uri,
                "storage_id": "mcap",
                "all_topics": True,
                "all_services": True,
                "all_actions": True
            }
        ]
    }
    with open(yaml_path, "w") as f:
        yaml.dump(config, f)

def merge_bags():
    mcap_files = find_all_mcap_files(ROOT_DIR)
    if len(mcap_files) < 2:
        print("Not enough .mcap files to merge.")
        return

    print(f"Found {len(mcap_files)} .mcap files. Generating YAML config...")
    write_merge_yaml(MERGED_BAG_NAME, CONFIG_PATH)

    print(f"Merging into '{MERGED_BAG_NAME}' using config '{CONFIG_PATH}'...")

    cmd = ["ros2", "bag", "convert"]
    for mcap in mcap_files:
        cmd += ["-i", mcap]
    cmd += ["-o", CONFIG_PATH]

    subprocess.run(cmd, check=True)
    print("Merge complete.")

if __name__ == "__main__":
    merge_bags()
