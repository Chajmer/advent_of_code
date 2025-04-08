using System;
using System.IO;
using System.Linq;

// =============== SOLUTION PART =============== //

static List<ValueTuple<int, int, int>> Localize(string line)
{
    var result = new List<ValueTuple<int, int, int>>();
    bool numberMode = false;
    string number = "";
    int start = 0;
    for (int i = 0; i < line.Length; ++i)
    {
        if (char.IsDigit(line[i]))
        {
            number += line[i];
            if (!numberMode)
            {
                numberMode = true;
                start = i;
            }
        }
        else
        {
            if (numberMode)
            {
                numberMode = false;
                ValueTuple<int, int, int> ad = (Convert.ToInt32(number), start, i-1);
                result.Add(ad);
                number = "";
            }
        }
        
        if (numberMode && i == line.Length - 1)
        {
            ValueTuple<int, int, int> ad = (Convert.ToInt32(number), start, i);
            result.Add(ad);
        }
    }
    return result;
}

static bool IsUnknownSign(char c)
{
    return (!char.IsDigit(c)) && (c != '.');
}

static List<bool> SolveSingleLine(string line, List<ValueTuple<int, int, int>> localization)
{
    var numsBools = new List<bool>();
    for (int i = 0; i < localization.Count; ++i)
    {
        int start = localization[i].Item2;
        int end = localization[i].Item3;
        if ((start != 0 && IsUnknownSign(line[start-1])) || (end != line.Length-1 && IsUnknownSign(line[end+1])))
        {
            numsBools.Add(true);
        }
        else
        {
            numsBools.Add(false);
        }
    }
    return numsBools;
}

static void SolveWithNeighbour(string line, string neighbour, List<ValueTuple<int,int,int>> localization, List<bool> numsBools)
{
    for (int i = 0; i < localization.Count; ++i)
    {
        if (numsBools[i])
            continue;

        int start = localization[i].Item2;
        int end = localization[i].Item3;
        if (start != 0)
            --start;
        if (end != line.Length - 1)
            ++end;

        for (int k = start; k <= end; k++)
        {
            if (IsUnknownSign(neighbour[k]))
            {
                numsBools[i] = true;
                break;
            }
        }
    }
}

static int SolveLine(string currentLine, string upperLine, string downLine)
{
    List<ValueTuple<int, int, int>> localizedNums = Localize(currentLine);
    var nums_bools = SolveSingleLine(currentLine, localizedNums);

    if (upperLine is not null)
        SolveWithNeighbour(currentLine, upperLine, localizedNums, nums_bools);

    if (downLine is not null)
        SolveWithNeighbour(currentLine, downLine, localizedNums, nums_bools);

    int result = 0;
    for (int i = 0; i < nums_bools.Count; ++i)
    {
        if (nums_bools[i])
            result += localizedNums[i].Item1;
    }
    return result;
}

static int Solve(string puzzle)
{
    string[] lines = puzzle.Split(new string[] { "\r\n", "\r", "\n" },StringSplitOptions.None);
    int result = 0;
    for (int i = 0; i < lines.Length; i++)
    {
        result += SolveLine(lines[i], (i > 0) ? lines[i-1] : null, (i < lines.Length - 1) ? lines[i+1] : null);
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
