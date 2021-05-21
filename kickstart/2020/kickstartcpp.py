#!/usr/bin/env python3
from sys import argv
from os import system
import os.path
import platform

if len(argv) < 2:
    print("Usage: kickstartcpp arguments filename.cc")
    exit(1)

if "-h" in argv:
    print("Matthew's Google Kickstart C++ Compile and Tester version 0.1.0\n")
    print("Usage: kickstartcpp arguments filename.cc\n")
    print("Options")
    print("WIP")
    exit(0)

if "-v" in argv:
    print("Working on version information")
    print("Matthew's Google Kickstart C++ Compile and Tester version 0.1.0")
    print(platform.platform())
    exit(0)

if (argv[-1][argv[-1].find(".cc"):]) != ".cc":
    print("Please provide C++ file with .cc file extension")
    exit(1)

run = False
delete = False
test = False
version = False

for i in argv:
    if i == argv[0] or i == argv[-1]:
        pass
    elif i == "-r":
        run = True
    elif i == "-d":
        delete = True
    elif "-t=" in i:
        test_file = i[3:]
        if not os.path.isfile(test_file):
            print(test_file, "not found.")
            exit(1)
        test = True
    else:
        print(f"Invalid argument: {i}")
        exit(1)

if run and test:
    print("Cannot use run (-r) and test (-t) arguments at the same time!")
    exit(1)

output_file_name = argv[-1][:argv[-1].find(".cc")]

print(f"g++ {argv[-1]} -std=c++14 -pthread -O3 -o {output_file_name}")
compile_result = system(f"g++ {argv[-1]} -std=c++14 -pthread -O3 -o {output_file_name}")

if compile_result != 0:
    print(compile_result)
    exit(1)

if run:
    print(f"./{output_file_name}")
    system(f"./{output_file_name}")
elif test:
    print(f"cat {test_file} | ./{output_file_name}")
    system(f"cat {test_file} | ./{output_file_name}")
elif delete:
    print(f"rm {output_file_name}")
    system(f"rm {output_file_name}")