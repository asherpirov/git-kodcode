using System;

namespace Demo;

class Track

{
    static void Main()
    {
        int trackid = 0;
        int Speed = 0;
        int Heading = 0;
        string status = "";
        string[] allowedStatuses = ["cruising", "turning", "stopped", "accelerating"];
        string category = "slow";


        bool Idisnum = false;

        while (!Idisnum)
        {
            Console.WriteLine("Please enter the trackid: ");
            string trackIdInput = Console.ReadLine();

            if (int.TryParse(trackIdInput, out trackid))
            {
                if (trackid > 0)
                {
                    Idisnum = true;
                }

                else
                {
                    Console.WriteLine("Error: The ID must be a positive number (greater than zero).");
                }
            }
            else
            {
                Console.WriteLine("Error: The ID must be an integer.");
            }

        }

        bool ValidSpeed = false;

        while (!ValidSpeed)
        {
            Console.WriteLine("Please enter the speed: ");
            string speedInput = Console.ReadLine();


            if (int.TryParse(speedInput, out Speed))
            {
                ValidSpeed = true;
            }
            else
            {
                Console.WriteLine("Error: The speed must be an integer.");
            }

        if (Speed <= 100)
        {
            category = "slow";
        }
        else if (100 < Speed && Speed <= 300)
        {
            category = "medium";
        }
        else
        {
            category = "fast";
        }
        }

        bool validHeading = false;

        while (!validHeading)
        {
            Console.WriteLine("Please enter the heading: ");
            string headindInput = Console.ReadLine();


            if (int.TryParse(headindInput, out Heading))
            {
                if (Heading >= 0 && Heading <= 359)
                {
                    validHeading = true;
                }
                else
                    Console.WriteLine("Error: The heading must be between 0-359.");
            }
            else
            {
                Console.WriteLine("Error: The Heading must be an integer.");
            }
        }

        bool validStatus = false;

        while (!validStatus)
        {
            Console.WriteLine("Please enter the status (cruising, turning, stopped, accelerating): ");
            string statusInput = Console.ReadLine();

            foreach (string allowedWord in allowedStatuses)
            {
                if (statusInput == allowedWord)
                {
                    validStatus = true;
                    status = statusInput;
                    break;

                }

            }
            if (!validStatus)
            {
                Console.WriteLine("Error: Please enter one of the exact status words.");
            }
        }


        int hedingDiv = Heading / 30;
        double headingDivDouble = (double)Heading / 30;

        int speedDiv = Speed / 60;
        double speedDivDouble = (double)Speed / 60;


        Console.WriteLine("=== Track Report ===");
        Console.WriteLine($"The new trackid is: {trackid}");
        Console.WriteLine($"The new speed is: {Speed} km/h and in category: {category}");
        Console.WriteLine($"The new status is: {status}");
        Console.WriteLine($"Division Demo 1: {Heading} / 30 = {hedingDiv} (int) | {headingDivDouble}");
        Console.WriteLine($"Division Demo 2: {Speed} / 60 = {speedDiv} (int) | {speedDivDouble}");



    }
}




