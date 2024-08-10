#Define Function
def canConstruct(ransomNote, magazine):
    out = True
    for char in ransomNote:
        out = ransomNote.count(char) <= magazine.count(char)
        if out == False:
            break
    return out

#Run Scenarios

print(canConstruct("a","b"))
print(canConstruct("aa","ab"))
print(canConstruct("aa","aab"))

