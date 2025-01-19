# 106. Sys Module
import sys

if len(sys.argv) > 1:
    print("Command-line arguments:", sys.argv[1:])
else:
    print("No command-line arguments provided.")