file = open("/home/nahomkasa/Documents/puzzel/Day5/input.txt", "r")
content = file.read()

rules, tests = content.split("\n\n")

order_rule = set () 

for test in rules.splitlines():
    parts = test.split("|")
    
    page_X = int(parts[0])
    page_Y = int(parts[1])
    
    order_rule.add((page_X, page_Y))
    