using System;
using System.IO;
using System.Linq;

// =============== SOLUTION PART =============== //

int[][] DIRECTIONS = [
    [0,  1],   // 0: down
    [0, -1],   // 1: up
    [1,  0],   // 2: right
    [-1,  0]   // 3: left
];
var DIRECTION_MAP = new Dictionary<char, List<int>> {
    { '|', new List<int> {0, 1} },
    { '-', new List<int> {2, 3} },
    { 'L', new List<int> {1, 2} },
    { 'J', new List<int> {1, 3} },
    { '7', new List<int> {0, 3} },
    { 'F', new List<int> {0, 2} },
    { 'S', new List<int> {0, 1, 2, 3} }
};
var VERTICAL_MAP = new Dictionary<char, int> {
    { 'L', -1 },
    { 'J', -1 },
    { '7',  1 },
    { 'F',  1 }
};

(int x, int y) LocateStart(string[] grid)
{
    for (int y = 0; y < grid.Length; ++y) 
        for (int x = 0; x < grid[y].Length; ++x)
            if (grid[y][x] == 'S') 
                return (x, y);

    return (-1, -1);
}

HashSet<(int, int)> GetLoop(string[] grid, int x, int y)
{
    HashSet<(int, int)> visited = [];

    while (!visited.Contains((x, y))) {
        visited.Add((x, y));

        foreach (int dir in DIRECTION_MAP![grid[y][x]]) {
            int nx = x + DIRECTIONS[dir][0], ny = y + DIRECTIONS[dir][1];

            // verify in bounds
            if (nx < 0 || ny < 0 || ny >= grid.Length || nx >= grid[ny].Length)
                continue;

            // verify not old
            if (visited.Contains((nx, ny)))
                continue;

            // opposite direction index: clever 0 <-> 1 and 2 <-> 3 switching
            int opposite = dir ^ 1;

            // verify suitability for continuing the loop
            if (DIRECTION_MAP.ContainsKey(grid[ny][nx]) && DIRECTION_MAP[grid[ny][nx]].Contains(opposite)) {
                x = nx; y = ny;
                break;
            }
        }
    }
    return visited;
}

int GetEnclosedCount(string[] grid, HashSet<(int, int)> visited)
{
    int result = 0;

    for (int y = 0; y < grid.Length; ++y) {
        bool is_in = false;
        char enter = 'F';

        for (int x = 0; x < grid[y].Length; ++x) {
            if (visited.Contains((x, y))) {

                if (grid[y][x] == '|')
                    is_in = !is_in;
                else if (grid[y][x] == 'F' || grid[y][x] == 'L')
                    enter = grid[y][x];
                else if ((grid[y][x] == '7' || grid[y][x] == 'J') && VERTICAL_MAP![enter] != VERTICAL_MAP![grid[y][x]])
                    is_in = !is_in;
            }
            else if (is_in)
                ++result;
        }
    }
    return result;
}

void ReplaceStart(string[] grid, int x, int y)
{
    List<int> suitable = [];

    foreach (int dir in DIRECTION_MAP!['S']) {
        int nx = x + DIRECTIONS[dir][0], ny = y + DIRECTIONS[dir][1];

        // verify in bounds
        if (nx < 0 || ny < 0 || ny >= grid.Length || nx >= grid[ny].Length)
            continue;

        // opposite direction index: clever 0 <-> 1 and 2 <-> 3 switching
        int opposite = dir ^ 1;

        // verify suitability
        if (DIRECTION_MAP.ContainsKey(grid[ny][nx]) && DIRECTION_MAP[grid[ny][nx]].Contains(opposite))
            suitable.Add(dir);
    }
    char replacement = (suitable[0], suitable[1]) switch
    {
        (0, 1) => '|',
        (0, 2) => 'F',
        (0, 3) => '7',
        (1, 2) => 'L',
        (1, 3) => 'J',
        (2, 3) => '-',
        _ => ' '
    };
    // C# string is immutable eh
    char[] rowChars = grid[y].ToCharArray();
    rowChars[x] = replacement;
    grid[y] = new string(rowChars);
}

int Solve(string input)
{
    string[] grid = input.Split(["\r\n", "\r", "\n"], StringSplitOptions.None);

    var (x, y) = LocateStart(grid);

    if (x == -1)
        return 0;

    var visited = GetLoop(grid, x, y);

    ReplaceStart(grid, x, y);

    return GetEnclosedCount(grid, visited);
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
