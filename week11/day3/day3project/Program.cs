using System;
namespace Day3;


        enum Classifications { Friendly, Hostile, Unidentified }
class Project
{
    static int GetValidSourceId()
    {
        bool ValidId = false;
        int SourceId = 0;

        while (!ValidId)

        Console.WriteLine("Enter SourceId: ");
        string idInput = Console.ReadLine();

        if (int.TryParse(idInput, out SourceId))
        {
                if (SourceId > 0)
                {
                return SourceId;
                }
                else
                {
                    Console.WriteLine("Error: the SourceId must be positive.");
                }
        }
        else
        {
            Console.WriteLine("Error: The id must be a integer nubmer");
        }

        return SourceId;
    }

    static Classifications GetValidClassification()
        
    {
       Classifications result = Classifications.Unidentified;
        bool validClassification = false;

        while (!validClassification)
        {
            Console.WriteLine("Enter classification (Friendly / Hostile / Unidentified): ");
            string classificationInput = Console.ReadLine();

            if (string.IsNullOrEmpty(classificationInput))
            {
                Console.WriteLine("Error: Input cannot be empty.");
                continue;
            }

            classificationInput = classificationInput.Trim().ToLower();
            
            if (Enum.TryParse(classificationInput,true, out result))
            {
                validClassification = true;
            }

            else
            {

            Console.WriteLine("Error: the classification must be Friendly, Hostile, or Unidentified");
            }

        }
        return result;
    }

    static double? getValidStrength()
    {   

        while (true)
        {
            Console.WriteLine("Enter Strength: ");
            string strengthInput = Console.ReadLine();

            if (string.IsNullOrEmpty(strengthInput))
            {
                return null;
            }

            if (double.TryParse(strengthInput , out double strength))
            {
                if (strength >= 0)
                {
                    return strength;
                }
                Console.WriteLine("Error: Strength cannot be negative.");
            }
            else
            {
                Console.WriteLine("Error: Invalid number. Please try again.");
            }
        }
    }


    static void AddSource(List<int> sourcesId, List<Classifications> classificationsList, List<double?> Strengths, int SourceId, Classifications classification, double? Strength)
    {
        sourcesId.Add(SourceId);
        classificationsList.Add(classification);
        Strengths.Add(Strength);
    }
        
    static void UpdateStrength(List<double?> Strengths, ref double? Strength)
    {
        double? newStrength = getValidStrength();
        Strength = newStrength;

     
    }




    static void Main()
    {

        List<int> sourcesId = new List<int>();
        List<Classifications> classificationsList = new List<Classifications>();
        List<double?> Strengths = new List<double?>();

        int getSourceId = GetValidSourceId();
    }
    
}
   