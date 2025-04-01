using System;
using System.IO;
using System.Linq;

// =============== SOLUTION PART =============== //

static (int, int, int) TakeParse(string take)
{
    string[] numsWithColors = take.Split(',');
    int red = 0;
    int green = 0;
    int blue = 0;
    foreach (var item in numsWithColors)
    {
        string[] numAndColor = item.Trim().Split(' ');
        int num = Convert.ToInt32(numAndColor[0]);
        string color = numAndColor[1];
        if (color == "red") red = num;
        if (color == "green") green = num;
        if (color == "blue") blue = num;
    }
    return (red, green, blue);
}

static int RoundSolve(string line)
{
    string[] headAndBody = line.Split(':');
    string[] bagTakes = headAndBody[1].Split(';');

    int redMax = 0;
    int greenMax = 0;
    int blueMax = 0;

    foreach (var take in bagTakes)
    {
        var rgbTake = TakeParse(take);
        if (redMax < rgbTake.Item1) redMax = rgbTake.Item1;
        if (greenMax < rgbTake.Item2) greenMax = rgbTake.Item2;
        if (blueMax < rgbTake.Item3) blueMax = rgbTake.Item3;
    }

    return redMax * greenMax * blueMax;
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
