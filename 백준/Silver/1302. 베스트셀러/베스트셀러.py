n = int(input())

book_dict = {}
for _ in range(n):
    book = input()
    book_dict[book] = book_dict.get(book, 0) + 1
    
book_list = list(book_dict.items())
book_list.sort(key=lambda x: (-x[1], x[0]))
print(book_list[0][0])