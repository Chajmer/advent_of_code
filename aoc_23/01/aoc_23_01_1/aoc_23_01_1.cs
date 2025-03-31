using System;
using System.IO;
using System.Linq;

// =============== SOLUTION PART =============== //

int Solve(string weatherInput)
{
    int result = 0;
    foreach (var line in weatherInput.Split('\n'))
    {
        int first = '0';
        for (int i = 0; i < line.Length; ++i)
        {
            if (char.IsDigit(line[i]))
            {
                first = line[i];
                break;
            }
        }
        int last = first;
        for (int i = line.Length - 1; i >= 0; --i)
        {
            if (char.IsDigit(line[i]))
            {
                last = line[i];
                break;
            }
        }
        result += (first - '0') * 10 + (last - '0');
    }
    return result;
}

// =============== TEMPLATE PART =============== //

// README INPUTS:
// Inputs are separete files in this path-name template:
// {this_file_dir}/../inputs/input_*.txt

// Ugly form due to an inconsistency bug between dotnet run and VS Code run
string inputDir = Path.Combine(Directory.GetParent(AppDomain.CurrentDomain.BaseDirectory)!.Parent!.Parent!.Parent!.Parent!.FullName, "inputs");

//  Iterate over all files matching the pattern 'input_*.txt'
foreach (var inputFile in Directory.EnumerateFiles(inputDir, "input_*.txt").OrderBy(f => f))
{
    Console.WriteLine($"Input {Path.GetFileNameWithoutExtension(inputFile).Substring(6)}:");
    Console.WriteLine(Solve(File.ReadAllText(inputFile).Trim()));
}

Console.WriteLine("Test done");
