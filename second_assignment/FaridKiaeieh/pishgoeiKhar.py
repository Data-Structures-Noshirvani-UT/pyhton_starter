def split(ref_str, character, output_size):
    result = ref_str.split(character)
    return result[:output_size] + [''] * (output_size - len(result))

def find_answer(key_value, size_key, goat_speech):
    for i in range(size_key):
        if key_value[i][0] == goat_speech:
            return key_value[i][1]
    return ""

if __name__ == "__main__":
    m, n = map(int, input().split())

    key_value = [['', ''] for _ in range(m)]

    # m lines
    for i in range(m):
        temp = input().strip()
        while temp == "":
            temp = input().strip()
        space_index = temp.find(' ')
        key_value[i][0] = temp[:space_index]
        key_value[i][1] = temp[space_index + 1:]

    # Last line
    temp = input().strip()
    goat_speech = split(temp, ' ', n)
    result = ""

    for i in range(n):
        answer = find_answer(key_value, m, goat_speech[i])
        if answer:
            result += answer + " kachal!"
        else:
            result += "kachal!"

        if i != n - 1:
            result += " "

    print(result)
