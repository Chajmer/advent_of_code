using System;
using System.IO;
using System.Linq;

// =============== SOLUTION PART =============== //

static bool Hail_intersection_valuation(Hail h1, Hail h2, long low, long high)
{
    double det = h1.b * h2.a - h2.b * h1.a;

    // parralell lines
    if (det == 0)
        return h1.c * h2.a == h2.c * h1.a; // (ay-bx)/a compare

    // intersection point - kind of Cramer's solution
    var x = (h2.c * h1.a - h1.c * h2.a) / det;
    var y = (h2.c * h1.b - h1.c * h2.b) / det;

    // boundary check solution
    if (x < low || x > high || y < low || y > high) return false;

    // direction check (dot product)
    bool h1_direction_bool = (x - h1.x) * h1.a + (y - h1.y) * h1.b >= 0;
    bool h2_direction_bool = (x - h2.x) * h2.a + (y - h2.y) * h2.b >= 0;

    return h1_direction_bool && h2_direction_bool;
}

static Hail Parse_hail_info(string hail_info)
{
    var parts = hail_info.Split(" @ ");
    var coords = parts[0].Split(", ").Select(double.Parse).ToArray();
    var vectors = parts[1].Split(", ").Select(double.Parse).ToArray();
    return new Hail(coords[0], coords[1], vectors[0], vectors[1]);
}

static List<Hail> Get_hails_info(string hails_info)
{
    var result = new List<Hail>();
    foreach (var line in hails_info.Split("\n"))
    {
        result.Add(Parse_hail_info(line));
    }
    return result;
}

static int Count_hail_intersection(string hails_input, long low, long high)
{
    int result = 0;
    var hails_info = Get_hails_info(hails_input);
    for (int i = 0; i < hails_info.Count; ++i)
    {
        for (int j = i + 1; j < hails_info.Count; ++j)
        {
            if (Hail_intersection_valuation(hails_info[i], hails_info[j], low, high))
                ++result;
        }
    }
    return result;
}

static int Solve(string input)
{
    var head_and_body = input.Split("\n\n");
    var head = head_and_body[0].Split(", ").Select(long.Parse).ToArray();
    return Count_hail_intersection(head_and_body[1], head[0], head[1]);
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

// =============== CLASS DEFINITION =============== //
class Hail
{
    public double x;
    public double y;
    public double a;
    public double b;
    public double c;
    public Hail(double h_x, double h_y, double h_a, double h_b)
    {
        x = h_x;
        y = h_y;
        a = h_a;
        b = h_b;
        c = h_a * h_y - h_b * h_x;
    }
}