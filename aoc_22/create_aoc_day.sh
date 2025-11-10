#!/bin/bash

# Get day and file extension from user
read -p "Enter day number: " day
day=$(printf "%02d" "$day")

read -p "Enter file extension (e.g., py, cpp, js, cs): " ext
file_ext=".$ext"

# Get the directory of the script
script_dir=$(dirname "$(realpath "$0")")
dir_name=$(basename "$script_dir")

# Create dirs and files
day_dir="$script_dir/$day"
day_base_name="${dir_name}_$day"

mkdir -p "$day_dir"

path1="$day_dir/${day_base_name}_1"
path2="$day_dir/${day_base_name}_2"

template_file="$script_dir/code_templates/template$file_ext"

create_file_from_template() {
    local file="$1"
    if [ ! -e "$file" ]; then
        [ -e "$template_file" ] && cp "$template_file" "$file" || touch "$file"
    fi
}

create_dotnet_project() {
    local project_dir="$1"
    local file="$2"
    if [ ! -d "$project_dir" ]; then
        dotnet new console -o "$project_dir"
        if [ -e "$template_file" ]; then
            rm "$project_dir/Program.cs"
        else
            mv "$project_dir/Program.cs" "$file"
        fi
    fi
}

if [ "$file_ext" == ".cs" ]; then
    # code file names
    file1="$path1/${day_base_name}_1$file_ext"
    file2="$path2/${day_base_name}_2$file_ext"
    create_dotnet_project "$path1" "$file1"
    create_dotnet_project "$path2" "$file2"
else
    # code file names
    file1="${path1}$file_ext"
    file2="${path2}$file_ext"
fi

# paste template file if it exists
create_file_from_template "$file1"
create_file_from_template "$file2"

# input file names
input_dir="$day_dir/inputs"
input1="$input_dir/input_1.txt"
input2="$input_dir/input_2.txt"

mkdir -p "$input_dir"
touch "$input1" "$input2"

echo "Files created (or exist already):"
echo "$file1"
echo "$file2"
echo "$input1"
echo "$input2"
