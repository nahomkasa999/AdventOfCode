file = open("/home/nahomkasa/Documents/puzzel/Day5/input.txt", "r")
content = file.read()

rules, tests = content.split("\n\n")

order_rule = set()
all_updates_data = []

for rule in rules.splitlines():
    parts = rule.split("|")
    
    page_X = int(parts[0])
    page_Y = int(parts[1])
    
    order_rule.add((page_X, page_Y))

for listsOfTest in tests.splitlines():
    if listsOfTest.strip():
        correctedNumber = listsOfTest.split(",")
        current_update_pages = [int(x.strip()) for x in correctedNumber]
        
        all_updates_data.append(current_update_pages)

total_middle_pages_sum = 0

for current_update_pages in all_updates_data:
    is_update_correct = True

    for i in range(len(current_update_pages)):
        page_A = current_update_pages[i]

        for j in range(i + 1, len(current_update_pages)):
            page_B = current_update_pages[j]

            if (page_B, page_A) in order_rule:
                is_update_correct = False
                break
        if not is_update_correct:
            break

    if is_update_correct:
        update_length = len(current_update_pages)
        middle_index = update_length // 2
        middle_page_number = current_update_pages[middle_index]

        total_middle_pages_sum += middle_page_number

print(total_middle_pages_sum)