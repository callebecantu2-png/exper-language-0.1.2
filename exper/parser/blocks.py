def get_block(self, lines, i):
    block = []
    i += 1
    braces = 1

    while i < len(lines):
        line = lines[i].strip()
        braces += line.count("{")
        braces -= line.count("}")

        if braces == 0:
            break

        block.append(line)
        i += 1

    return block, i