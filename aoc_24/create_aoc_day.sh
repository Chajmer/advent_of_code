#!/bin/bash

# Get the directory of the script
script_dir=$(dirname "$(realpath "$0")")
dir_name=$(basename "$script_dir")

read -p "Enter day number: " day
day=$(printf "%02d" "$day")

read -p "Enter file extension (e.g., py, cpp, js): " ext
file_ext=".${ext}"

# code file names
file1="${script_dir}/${day}/${dir_name}_${day}_1${file_ext}"
file2="${script_dir}/${day}/${dir_name}_${day}_2${file_ext}"

template_file="${script_dir}/code_templates/template${file_ext}"

mkdir -p "${script_dir}/${day}"

# paste template file if it exists
if [ ! -e "$file1" ]; then
    if [ -e "$template_file" ]; then
        cp "$template_file" "$file1"
    else
        touch "$file1"
    fi
fi

if [ ! -e "$file2" ]; then
    if [ -e "$template_file" ]; then
        cp "$template_file" "$file2"
    else
        touch "$file2"
    fi
fi

# input file names
input_dir="${script_dir}/${day}/inputs"
input1="${input_dir}/input_1.txt"
input2="${input_dir}/input_2.txt"

mkdir -p "$input_dir"
touch "$input1" "$input2"

echo "Files created:"
echo "$file1"
echo "$file2"
echo "$input1"
echo "$input2"
