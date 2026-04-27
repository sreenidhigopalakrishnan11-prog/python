def minion_game(string):
    vowels = 'AEIOU'
    stuart_score = 0  # Consonants
    kevin_score = 0   # Vowels
    n = len(string)

    for i in range(n):
        # The number of substrings starting at index i is (n - i)
        if string[i] in vowels:
            kevin_score += (n - i)
        else:
            stuart_score += (n - i)

    # Determine the winner
    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
