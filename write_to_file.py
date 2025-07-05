def write_to_file(text):
    overwrite = True
    choice = ["a", "w"]
    formatted_text = ""
    i = 0

    while i < len(text):
        if i == 0:
            formatted_text += text[i]
            i += 1
        elif i % 80 == 0:
            while ord(text[i]) != ord(" "):
                formatted_text += text[i]
                i += 1
            formatted_text += "\n"
        formatted_text += text[i]
        i += 1

    with open("output.txt", choice[overwrite]) as f:
        f.write(formatted_text)
