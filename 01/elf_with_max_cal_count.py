def get_raw_elf_calorie_data() -> list[str]:
    with open("./elf_calorie_count.txt", "r") as f:
        return f.readlines()


def count_elf_calorie_data(data) -> dict[str, int]:
    elf_count = 0
    elf_calorie_data = {}
    for v in data:
        if v.isspace():
            elf_count += 1
            continue
        elf = f"elf_{str(elf_count)}"
        if elf not in elf_calorie_data:
            elf_calorie_data[elf] = int(v)
            continue
        elf_calorie_data[elf] += int(v)
    return elf_calorie_data


def main():
    raw_elf_calorie_data = get_raw_elf_calorie_data()
    elf_calorie_counts = count_elf_calorie_data(raw_elf_calorie_data)
    sorted_counts = sorted(elf_calorie_counts.items(),key=lambda item: item[1], reverse=True)
    top_three_elves = sorted_counts[0][1] + sorted_counts[1][1] + sorted_counts[2][1]
    print(f"Top three elves calorie count: {top_three_elves}")


if __name__ == "__main__":
    main()