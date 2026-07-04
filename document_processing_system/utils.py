def save_text(texts):

    with open(
        "output/result.txt",
        "w",
        encoding="utf-8"
    ) as file:

        for index,text in enumerate(texts):

            file.write(f"========== Region {index+1} ==========\n")

            file.write(text)

            file.write("\n\n")
