using System;
using System.IO;
using System.Linq;

// =============== SOLUTION PART =============== //

static int LineSolver(string line)
{
    // parsing
    var rightLeftSide = line.Split(" | ");
    var leftStrNums = rightLeftSide[0].Split(": ")[1].Split(new []{" "}, StringSplitOptions.RemoveEmptyEntries);
    var rightStrNums = rightLeftSide[1].Split(new []{" "}, StringSplitOptions.RemoveEmptyEntries);
    // List<str> -> List<int>
    var leftNums = new List<int>();
    foreach (var str_num in leftStrNums)
        leftNums.Add(Convert.ToInt32(str_num));
    var rightNums = new List<int>();
    foreach (var str_num in rightStrNums)
        rightNums.Add(Convert.ToInt32(str_num));
    // end of parsing

    // actual solving
    int result = 0;
    foreach (var num in rightNums)
    {
        if (leftNums.Contains(num))
            ++result;
    }
    return result;
}

static int Solve(string rounds)
{
    string[] lines = rounds.Split(new string[] { "\r\n", "\r", "\n" },StringSplitOptions.None);
    var countsInLines = new List<int>();
    var numOfCards = new Dictionary<(int, int), int>();
    int lineIndex = 0;

    foreach (var line in lines)
    {
        ++lineIndex;
        int solvedLine = LineSolver(line);
        countsInLines.Add(solvedLine);
        numOfCards[(lineIndex, solvedLine)] = 1;
    }

    for (int i = 1; i <= lineIndex; ++i)
    {
        for (int j = 1; j <= countsInLines[i-1]; ++j)
        {
            if (j+i > countsInLines.Count)
                break;
            numOfCards[(i+j, countsInLines[i+j-1])] += numOfCards[(i, countsInLines[i-1])];
        }
    }

    int result = 0;
    foreach (var kv in numOfCards)
        result += kv.Value;
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
