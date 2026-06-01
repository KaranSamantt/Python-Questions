def remove_and_strip(lst, word):
    stripped_word = word.strip()          # strip the given word first
    lst = [item for item in lst if item.strip() != stripped_word]  # remove & strip
    return lst


lst = ["  apple  ", "banana", "  mango  ", "apple", "  grape  "]
word = input("Enter word to remove: ")

print("Updated list: ", remove_and_strip(lst, word))

# "  apple  ".strip() → "apple" == "apple" ❌ removed
# "banana".strip()    → "banana" != "apple" ✅ kept
# "  mango  ".strip() → "mango"  != "apple" ✅ kept
# "apple".strip()     → "apple"  == "apple" ❌ removed
# "  grape  ".strip() → "grape"  != "apple" ✅ kept