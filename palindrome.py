import sys
if len(sys.argv) == 3:
    script_name = sys.argv[0]
    input_str = sys.argv[1]
else:
    script_name = sys.argv[0]
    input_str = "racecar"
reversed_str = input_str[::-1]
if input_str == reversed_str:
    print(f'"{input_str}" is a palindrome.')    
else:
    print(f'"{input_str}" is not a palindrome.')