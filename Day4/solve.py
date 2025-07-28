#this is best exercise to practise for loops

file = open("/home/nahomkasa/Documents/puzzel/Day4/input.txt", "r")
content = file.read()

grid = []
target_word = "XMAS"
word_length = len(target_word)

XMAS_COUNT = 0

directions = [
    (0, 1),   
    (0, -1),  
    (1, 0),   
    (-1, 0),  
    (1, 1),   
    (-1, -1),
    (1, -1),  
    (-1, 1) 
]

for text in content.split("\n"):
    if text:
        grid.append(list(text))
        #[['X', 'M', 'A', 'S']]
        #[['X', 'M', 'A', 'S'], ['S', 'A', 'M', 'X']]
        #[['X', 'M', 'A', 'S'], ['S', 'A', 'M', 'X'], ['S', 'M', 'X', 'A']]
        #[['X', 'M', 'A', 'S'], ['S', 'A', 'M', 'X'], ['S', 'M', 'X', 'A'], ['X', 'M', 'A', 'S']] the final grid
num_rows = len(grid) # we is 4
num_colomns = len(grid[0]) # which is X M A S = 4

for row in range(num_rows):#[[],[],[],[]]
    for col in range(num_colomns): #[['X' <- first itertaion, 'M', 'A', 'S'], ['S', 'A', 'M', 'X'], ['S', 'M', 'X', 'A'], ['X', 'M', 'A', 'S']]
        # here for every element we have 8 direction, which we should go through and find a combinantion
        for dr, dc in directions:
            
            current_candidate_word = []
            current_r, current_c = row, col
            
            for i in range(word_length):
                if 0 <= current_r < num_rows and 0 <= current_c < num_colomns:
                    current_candidate_word.append(grid[current_r][current_c])
                    current_r += dr
                    current_c += dc
                else:
                    break
                
            if len(current_candidate_word) == 4 and "".join(current_candidate_word) == target_word:
                XMAS_COUNT += 1
print(XMAS_COUNT)