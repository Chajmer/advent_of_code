using System;
using System.IO;
using System.Linq;

// =============== SOLUTION PART =============== //

static int Hail_intersection_valuation(Hail first, Hail second, long low, long high)
{
    // some a == 0
    // not happening in test case

    // (ay-bx)/a == same of second
    if (first.b * second.a == first.a * second.b)
        return (first.c * second.a == second.c * first.a) ? 1 : 0;
    // normal calculation
    var x_cor = (((double)second.c / second.a) - ((double)first.c / first.a)) / (((double)first.b / first.a) - ((double)second.b / second.a));
    var y_cor = (double)first.b / first.a * x_cor + (double)first.c / first.a;
    // return if on boudnries 200000000000000 and at most 400000000000000
    // ano skarede - da sa dat do funkcie
    bool boudry_bool = x_cor >= low && x_cor <= high && y_cor >= low && y_cor <= high;
    bool first_x_bool = (x_cor < first.x && first.a < 0) || (x_cor > first.x && first.a > 0) || (x_cor == first.x);
    bool first_y_bool = (y_cor < first.y && first.b < 0) || (y_cor > first.y && first.b > 0) || (y_cor == first.y);
    bool second_x_bool = (x_cor < second.x && second.a < 0) || (x_cor > second.x && second.a > 0) || (x_cor == second.x);
    bool second_y_bool = (y_cor < second.y && second.b < 0) || (y_cor > second.y && second.b > 0) || (y_cor == second.y);
    bool direction_bool = first_x_bool && first_y_bool && second_x_bool && second_y_bool;
    return (boudry_bool && direction_bool) ? 1 : 0;
}

static Hail Count_info_line(string hail_info)
{
    var coords_separ_vector = hail_info.Split(" @ ");
    var coords = coords_separ_vector[0].Split(", ");
    var vectors = coords_separ_vector[1].Split(", ");
    return new Hail(Convert.ToInt64(coords[0]), Convert.ToInt64(coords[1]), Convert.ToInt64(vectors[0]), Convert.ToInt64(vectors[1]));
}

static List<Hail> Count_info_whole(string hails_info)
{
    string[] lines = hails_info.Split(new string[] { "\r\n", "\r", "\n" }, StringSplitOptions.None);
    var result = new List<Hail>();
    foreach (var line in lines)
    {
        result.Add(Count_info_line(line));
    }
    return result;
}

static int Count_hail_intersection(string hails_info, long low, long high)
{
    int result = 0;
    // count needed for each line store in List
    var hails_counted_info = Count_info_whole(hails_info);
    // inner for cycle List check 2 info against
    // if cross in boudries ++result
    // done
    for (int i = 0; i < hails_counted_info.Count; ++i)
    {
        for (int j = i + 1; j < hails_counted_info.Count; ++j)
        {
            result += Hail_intersection_valuation(hails_counted_info[i], hails_counted_info[j], low, high);
        }
    }
    return result;
}

static int Solve(string input)
{
    string example = @"19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3";
    Console.WriteLine(Count_hail_intersection(example, 7, 27));
    int result = Count_hail_intersection(input, 200000000000000, 400000000000000);
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

// =============== CLASS DEFINITION =============== //
class Hail
{
    public long x;
    public long y;
    public long a;
    public long b;
    public long c;
    public Hail(long h_x, long h_y, long h_a, long h_b)
    {
        x = h_x;
        y = h_y;
        a = h_a;
        b = h_b;
        c = h_y * h_a - h_b * h_x;
    }
}