T =int(input())

for _ in range(T):

    word = input().split()

    word_list = []
    word_list = word

    wow_word = []
    for i in word_list:
        wow_word.append(i[::-1])


    print(*wow_word)