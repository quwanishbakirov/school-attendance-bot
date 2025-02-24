import ast

def parse_string_to_dict(s):
    data = ast.literal_eval(s)  # Stringni tuplega aylantiramiz
    return {"id": data[0], "full_name": data[1], "class": data[2]}

# Misol
while True:
    s = input()
    result = parse_string_to_dict(s[:-1])
    print(result,end=",\n")
