#!/usr/bin/python3
import yaml
def main():
    with open("datacenter.yaml","r") as yammy:
        pyyaml_read = yammy.read()
        pyyaml_load = yaml.dumps(yammy)

    print(pyyaml_read)
    print("----------------------------------")
    print(pyyaml_load)


main()
