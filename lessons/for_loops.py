"""For loops syntax + practice!"""

pets: list[str] = ["Louie", "Bo", "Bear"]

for animal in pets:
    # Tell every pet they're a good boy!
    #print("Good boy, " + animal + "!")  # Normal concatenation
    #print(f"Good boy, {animal}!")  # Using f-string

names:list[str] = ["Alyssa", "Janet", "Vrinda"]

for index in range(0, len(names)):
    print(str(index)+names[index])
    print(f"{index}:{names[index]}")
