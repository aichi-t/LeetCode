def canConstruct(ransomNote, magazine):
    magazine = list(magazine)
    for letter in ransomNote:
        try:
            magazine.remove(letter)
        except:
            return False
    return True


if __name__ == "__main__":

    ransomNote = "aa"
    magazine = "aba"
    print(canConstruct(ransomNote, magazine))
