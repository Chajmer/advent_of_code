using System;
using System.IO;
using System.Linq;

// =============== SOLUTION PART =============== //

static bool TakeSolve(string take)
{
    string[] numsWithColors = take.Split(',');
    foreach (var item in numsWithColors)
    {
        string[] numAndColor = item.Trim().Split(' ');
        int num = Convert.ToInt32(numAndColor[0]);
        string color = numAndColor[1];
        if (color == "red" && num > 12) return false;
        if (color == "green" && num > 13) return false;
        if (color == "blue" && num > 14) return false;
    }
    return true;
}

static int RoundSolve(string line)
{
    string[] headAndBody = line.Split(':');
    string[] bagTakes = headAndBody[1].Split(';');

    foreach (var take in bagTakes)
    {
        if (!TakeSolve(take)) return 0;
    }

    return Convert.ToInt32(headAndBody[0].Split(' ')[1]);
}

static int Solve(string games)
{
    string[] rounds = games.Split('\n');
    int result = 0;
    foreach (var line in rounds)
    {
        result += RoundSolve(line);
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
