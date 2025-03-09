USAGE
    Copy and rename this folder as you wish.
    Then each day just run the script "create_aoc_day.sh".
    It will ask you to set the day number and file extension.

    It will create a folder inside:
        01/
        ├── dir_name_01_1.py
        ├── dir_name_01_2.py
        └── inputs
            ├── input_1.txt
            └── input_2.txt

    If there is a file with your entered extension in the `code_templates/` folder,
    it will be copy-pasted to the solution files.

    Attention: To ensure proper functionality, use these file path-name templates:
        Solutions:
            "${script_dir}/${day}/${dir_name}_${day}_{part}${file_ext}"
        Inputs:
            "${script_dir}/${day}/inputs/input_*.txt"
        Templates:
            "${script_dir}/code_templates/template${file_ext}"

INFO
    https://adventofcode.com/
    This directory is a template for Advent of Code events,
    but it can also be reused elsewhere.

    The script "create_aoc_day.sh" automatically creates the necessary files.

    There is also a prepared Python file template.

    Made by https://github.com/Chajmer
