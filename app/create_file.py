import sys
import os
import datetime


def create_dir(current_dir: str, list_parts_dir: list[str]) -> str:
    directory_path = os.path.join(current_dir, *list_parts_dir)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    else:
        print(f"This directory {directory_path} exists")
    return directory_path


def create_file(current_dir: str, name_file: str) -> None:
    file_path = os.path.join(current_dir, name_file)

    with open(f"{file_path}", "a") as f:
        current_time = datetime.datetime.now()
        f.write(f"{str(current_time).split('.')[0]}\n")  # 2022-02-01 14:41:10
        number_line = 0
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            number_line += 1
            f.write(f"{number_line} {line}\n")
        f.write("\n")


if (len(sys.argv) > 2
        and sys.argv[1] + sys.argv[2] != "-d-f"
        and sys.argv[-1] != "-f"):

    flag = sys.argv[1]
    current_directory = os.path.dirname(sys.argv[0])

    if flag == "-d" and sys.argv[2:]:
        if "-f" not in sys.argv[2:]:
            create_dir(current_directory, sys.argv[2:])
        elif sys.argv[-2] == "-f":
            index_f = sys.argv.index("-f", 2)
            new_directory = create_dir(current_directory, sys.argv[2:index_f])
            create_file(new_directory, sys.argv[-1])

    if flag == "-f" and sys.argv[-1] != "-f":
        create_file(current_directory, sys.argv[-1])

else:
    print(
        "Enter correctly command please:\n",
        "[-d dir1 [dir2..]] for create directory\n",
        "[-f file.txt] for create file \n",
        "[-d dir1 dir2..] [-f file.txt] for create directory ",
        "and file in this directory"
    )
