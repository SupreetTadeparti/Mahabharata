import os


def main():
    with open("sdata.json", "w", encoding="utf-8") as json:
        json.write("{\n\t")
        books = len(os.listdir("SanskritBooks"))
        for book in range(books):
            json.write(f"\"Book {book + 1}\": {{\n\t\t")
            sections = len(os.listdir(f"SanskritBooks/Book {book + 1}"))
            for section in range(sections):
                json.write(f"\"Section {section + 1}\": [\n\t\t\t")
                with open(f"SanskritBooks/Book {book + 1}/Section {section + 1}.txt", "r", encoding="utf-8") as file:
                    lines = file.readlines()[:-2]
                    for i, line in enumerate(lines):
                        line = line.replace("\"", "'").replace("\n", "")
                        json.write(f"\"{line}\"")
                        if i != len(lines) - 1:
                            json.write(",\n\t\t\t")
                        else:
                            json.write("\n\t\t")
                if section != sections - 1:
                    json.write("],\n\t\t")
                else:
                    json.write("]\n\t")
            if book != books - 1:
                json.write("},\n\t")
            else:
                json.write("}\n")
        json.write("}")


if __name__ == "__main__":
    main()
