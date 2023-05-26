def freq_of_char(str: str) -> dict:
    all_char_freq = {}
    for i in str:
        if i in all_char_freq:
            all_char_freq[i] += 1
        else:
            all_char_freq[i] = 1
    return all_char_freq

print("Frequency of characters:\n%s" % freq_of_char(input("Input sequence: ")))

