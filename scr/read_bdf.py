from os.path import join

# TEST_FILE = join("..", ".font_test", "test.bdf")
TEST_FILE = join("..", ".font_test", "umplus_j10r.bdf")

def get_lines_from_file(file_name):
    lines = []
    with open(file_name, "r") as f:
        lines = f.read()
    return lines.splitlines()

def get_data_from_lines(lines):
    bitmap = []
    record = False
    glyphs = dict()
    
    for line in lines:
        if line.startswith("FONTBOUNDINGBOX"):
            # print(line.split(" "))
            pass
        elif line.startswith("ENCODING"):
            code = int(line.split(" ")[1])
        # elif line.startswith("DWIDTH"):
            # print(line.split(" "))
        # elif line.startswith("BBX"):
            # print(line.split(" "))
        elif line.startswith("BITMAP"):
            record = True
            bitmap = []
        elif line.startswith("ENDCHAR"):
            # print(bitmap)
            record = False
            glyphs[code] = bitmap
        else:
            if record:
                bit = bin(int(line, 16))[2:].zfill(4*len(line))
                bit = bit.replace('0', ' ')
                bit = bit.replace('1', '█')
                bitmap.append(bit)
    
    print("-"*52)
    with open("test.txt", 'bw') as f:
        for k in glyphs:
            f.write("─".encode("utf-8")*52)
            f.write(b'\n')
            f.write(f"{k}:\n".encode("utf-8"))
            for b in glyphs[k]:
                f.write(b.encode("utf-8"))
                f.write(b'\n')


def main():
    lines = get_lines_from_file(TEST_FILE)
    get_data_from_lines(lines)


if __name__ == "__main__":
    main()
