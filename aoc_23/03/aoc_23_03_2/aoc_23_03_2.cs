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

static List<int> StarsLocalize(string line)
{
    var result = new List<int>();
    for (int i = 0; i < line.Length; ++i)
    {
        if (line[i] == '*')
            result.Add(i);
    }
    return result;
}

static bool IsInNumInterval(int position, ValueTuple<int,int,int> localizedNum)
{
    for (int i = localizedNum.Item2; i <= localizedNum.Item3; ++i)
    {
        if (position == i)
            return true;
    }
    return false;
}

static void EvalNumWithStar(int location, ValueTuple<int,int,int> localizedNum, List<int> alignedNums)
{
    for (int i = -1; i < 2; ++i)
    {
        if (IsInNumInterval(location + i, localizedNum))
        {
            alignedNums.Add(localizedNum.Item1);
            break;
        }
    }
    return;
}

static void EvalLineWithStar(int location, List<ValueTuple<int,int,int>> localizedLine, List<int> alignedNums)
{
    foreach (var localizedNum in localizedLine)
        EvalNumWithStar(location, localizedNum, alignedNums);
}

static int StarEval(int line_index, int location, List<List<ValueTuple<int, int, int>>> localizedMap)
{
    var alignedNums = new List<int>();
    for (int i = -1; i < 2; ++i)
    {
        if ((line_index == 0 && i== -1) || (line_index == localizedMap.Count-1 && i == 1))
            continue;
        if (alignedNums.Count > 2)
            break;
        EvalLineWithStar(location, localizedMap[line_index+i], alignedNums);
    }
    return (alignedNums.Count == 2) ? (alignedNums[0] * alignedNums[1]) : 0;
}

static int SolveLine(int lineIndex, string line, List<List<ValueTuple<int, int, int>>> localizedMap)
{
    int result = 0;
    var starLocations = StarsLocalize(line);
    
    foreach (int location in starLocations)
        result += StarEval(lineIndex, location, localizedMap);

    return result;
}

static int Solve(string puzzle)
{
    string[] lines = puzzle.Split(new string[] { "\r\n", "\r", "\n" },StringSplitOptions.None);
    int result = 0;
    var localizedMap = new List<List<ValueTuple<int, int, int>>>();

    for (int i = 0; i < lines.Length; i++)
        localizedMap.Add(Localize(lines[i]));

    for (int i = 0; i < lines.Length; i++)
        result += SolveLine(i, lines[i], localizedMap);

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
