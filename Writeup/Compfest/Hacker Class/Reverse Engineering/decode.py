import importlib

module = importlib.import_module("secret")
output = ""

i = 0
while True:
    importlib.reload(module)
    module.c.w = int("9" * (i+1))
    char = module.c()
    output += char
    print(".", end="", flush=True)
    i+=1
    if char == "}":
        print()
        break

print(output)
