using System;
using System.IO;
using System.Linq;

// =============== SOLUTION PART =============== //

int[][] DIRECTIONS = new int[][] {
    new int[] { 0,  1},   // 0: down
    new int[] { 0, -1},   // 1: up
    new int[] { 1,  0},   // 2: right
    new int[] {-1,  0}    // 3: left
};
var DIRECTION_MAP = new Dictionary<char, List<int>> {
    { '|', new List<int> {0, 1} },
    { '-', new List<int> {2, 3} },
    { 'L', new List<int> {1, 2} },
    { 'J', new List<int> {1, 3} },
    { '7', new List<int> {0, 3} },
    { 'F', new List<int> {0, 2} },
    { 'S', new List<int> {0, 1, 2, 3} }
};

(int x, int y) LocateStart(string[] grid)
{
    for (int y = 0; y < grid.Length; ++y) 
        for (int x = 0; x < grid[y].Length; ++x)
            if (grid[y][x] == 'S') 
                return (x, y);

    return (-1, -1);
}

int LoopLen(string[] grid)
{
    var (x, y) = LocateStart(grid);

    if (x == -1)
        return 0;

    // walk the loop
    int result = 0, prevX = x, prevY = y;

    while (grid[y][x] != 'S' || result == 0) {
        bool next = false;

        foreach (int dir in DIRECTION_MAP![grid[y][x]]) {
            int nx = x + DIRECTIONS[dir][0], ny = y + DIRECTIONS[dir][1];

            // verify in bounds
            if (nx < 0 || ny < 0 || ny >= grid.Length || nx >= grid[ny].Length)
                continue;

            // verify not old
            if (nx == prevX && ny == prevY)
                continue;

            // opposite direction index: clever 0 <-> 1 and 2 <-> 3 switching
            int opposite = dir ^ 1;

            // verify suitability for continuing the loop
            if (DIRECTION_MAP.ContainsKey(grid[ny][nx]) && DIRECTION_MAP[grid[ny][nx]].Contains(opposite)) {
                prevX = x; prevY = y;
                x = nx; y = ny;
                next = true;
                break;
            }
        }
        if (!next)
            return 0;
        ++result;
    }
    return result;
}

int Solve(string input)
{
    string[] grid = input.Split(new string[] { "\r\n", "\r", "\n" },StringSplitOptions.None);

    return LoopLen(grid) / 2;
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
