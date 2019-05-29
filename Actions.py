list_actions = ["YouTube"]  # add supported commands here


def compare_words(text, text_corr):
    loop_length = min(len(text), len(text_corr))
    matching = 0
    while loop_length > 0:
        if text[loop_length - 1] == text_corr[loop_length - 1]:
            matching += 1
        loop_length -= 1
    return [matching / len(text_corr), text_corr]


def similar(text):
    max_match = 0
    word = ""
    for el in list_actions:
        compare_element = compare_words(text, el)
        if compare_element[0] > max_match:
            max_match = compare_element[0]
            word = compare_element[1]
    if max_match > 0.5:
        return word
    else:
        return "WrongInstruction"


def get_action_name(instruction):
    action = similar(instruction.split()[0])
    if action == "WrongInstruction":
        print("Sorry I did't catch that")
    else:
        print(action)
    return action


def get_arguments(instruction):
    return instruction.split()[1:]


def get_instruction_with_args(instruction):
    return [get_action_name(instruction), get_arguments(instruction)]


if __name__ == '__main__':
    print(get_instruction_with_args("Youtube ala ma kota"))
