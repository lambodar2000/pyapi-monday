#!/usr/bin/python3
'''
python --version
'''
def main():
    hostipdict = { "host01":"10.10.2.3","host02":"10.0.1.1","host03":"72.5.4.22"}
    hostipdict["host04"] = "72.5.4.23"
    print(hostipdict)
#    print(hostipdict["host05"])
    print(hostipdict.key())

main()

