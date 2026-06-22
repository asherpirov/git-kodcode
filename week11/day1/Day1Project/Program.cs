using System;

namespace Demo;

class Track

{
    static void Main()
    {
        int trackId = 0;
        int speed = 0;
        int heading = 0;
        string status = "";
        string[] allowedStatuses = ["cruising", "turning", "stopped", "accelerating"];
        string category = "slow";


        bool idIsNum = false;

        while (!idIsNum)
        {
            Console.WriteLine("Please enter the track id: ");
            string trackIdInput = Console.ReadLine();

            if (int.TryParse(trackIdInput, out trackId))
            {
                if (trackId > 0)
                {
                    idIsNum = true;
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

        bool validSpeed = false;

        while (!validSpeed)
        {
            Console.WriteLine("Please enter the speed: ");
            string speedInput = Console.ReadLine();


            if (int.TryParse(speedInput, out speed))
            {
                validSpeed = true;
            }
            else
            {
                Console.WriteLine("Error: The speed must be an integer.");
            }

        if (speed <= 100)
        {
            category = "slow";
        }
        else if (100 < speed && speed <= 300)
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


            if (int.TryParse(headindInput, out heading))
            {
                if (heading >= 0 && heading <= 359)
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


        int hedingDiv = heading / 30;
        double headingDivDouble = (double)heading / 30;

        int speedDiv = speed / 60;
        double speedDivDouble = (double)speed / 60;


        Console.WriteLine("=== Track Report ===");
        Console.WriteLine($"The new trackid is: {trackId}");
        Console.WriteLine($"The new speed is: {speed} km/h ({category})");
        Console.WriteLine($"Heading: {heading} degrees");
        Console.WriteLine($"The new status is: {status}");
        Console.WriteLine($"Division Demo 1: {heading} / 30 = {hedingDiv} (int) | {headingDivDouble}");
        Console.WriteLine($"Division Demo 2: {speed} / 60 = {speedDiv} (int) | {speedDivDouble}");

    }
}