using System;
namespace Day2;

class Fleet
{

    static int GetValidId()
    {
        int trackId = 0;
        bool isValidId = false;

        while (!isValidId)
        {
            Console.WriteLine("Please enter a trackId: ");
            string inputId = Console.ReadLine();

            if (int.TryParse(inputId, out trackId))
            {
                if (trackId > 0)
                {
                    return trackId;
              
                }
                else
                {
                    Console.WriteLine("Error: The id must be a positive nubmer");
                }
            }
            else
            {
                Console.WriteLine("Error: The id must be a integer nubmer");
            }

        }

        return trackId;
    }

    static int GetValidSpeed()
    {
        int speed = 0;
        bool isValidSpeed = false;

        while (!isValidSpeed)
        {
            Console.WriteLine("Please enter a speed: ");
            string inputSpeed = Console.ReadLine();

            if (int.TryParse(inputSpeed, out speed))
            {
                if (speed > 0)
                {
                    return speed;

                }
                else
                {
                    Console.WriteLine("Error: The speed must be a positive number");
                }
            }
            else
            {
                Console.WriteLine("Error: The speed must be a integer number");
            }

        }

        return speed;
    }

    static string CategorySpeed(int speed)
    {
        string category = "slow";

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
        return category;
    }
    

    static int GetValidHeading()
    {
        int heading = 0;
        bool isValidHeading = false;

        while (!isValidHeading)
        {
            Console.WriteLine("Please enter a heading: ");
            string inputHeading = Console.ReadLine();

            if (int.TryParse(inputHeading, out heading))
            {
                if (heading >= 0 && heading <= 359)
                {
                    return heading;

                }
                else
                {
                    Console.WriteLine("Error: The heading must be between 0-359.");
                }
            }
            else
            {
                Console.WriteLine("Error: The heading must be a integer nubmer");
            }

        }

        return heading;
    }


    static string GetValidStatus()
    {
        string status = "";
        string[] allowedStatuses =  { "cruising", "turning", "stopped", "accelerating" };

        bool validStatus = false;

        while (!validStatus)
        {
            Console.WriteLine("Please enter the status (cruising, turning, stopped, accelerating): ");
            string statusInput = Console.ReadLine();
    

            foreach (string allowedStatus in allowedStatuses)
            {
                if (statusInput == allowedStatus)

                {
                    status = statusInput;
                    validStatus = true;
                    break;
                }
                
                
            }

        }
        if (!validStatus)
        {
            Console.WriteLine("Error: Please enter one of the exact status words.");
        }
        return status;
    }

    static void AddTrack(List<int> tracks, List<double> speeds, List<int> headings, int id, double speed, int heading)
    {
        tracks.Add(id);
        speeds.Add(speed);
        headings.Add(heading);
    }

    static void RemoveById(List<int> tracks, List<double> speeds, List<int> headings, int id)
    {
            
        int i = tracks.IndexOf(id);

        if (i >= 0)
        {
            tracks.RemoveAt(i);
            speeds.RemoveAt(i);
            headings.RemoveAt(i);
            Console.WriteLine($"Track {id} was removed successfully");
        }
        else
        {
            Console.WriteLine($"Error: Track {id} not found");
        }
    }

    static string FindById(List<int> tracks, List<double> speeds, List<int> headings, int id)
    {
        int i = tracks.IndexOf(id);
        string result = "";

        if (i >= 0)
        {
            result = $"The track {id}, the speed: {speeds[i]} kn, the heading: {headings[i]} ";
        }
        else
        {
           Console.WriteLine($"Error: Track {id} not found");
        }
     return result;


    }

    static string ListAllTrack(List<int> tracks, List<double> speeds, List<int> headings)
    {
        string allLists = "";
        for (int i = 0; i < tracks.Count; i++)
        {
            allLists += $"[trackId: {tracks[i]}, speed: {speeds[i]}, heading: {headings[i]}]\n";
        }

        if (tracks.Count == 0)
        {
            return "The fleet is currently empty.";
        }

        return allLists;

    }
    
    static List<int> FilterBySpeed(List<int> tracks, List<double> speeds, List<int> headings, double speed)
    {
        List<int> fastTrack = new List<int>();

        for (int i = 0; i< tracks.Count; i++)
        {
            if (speeds[i] > speed)
            {
                fastTrack.Add(tracks[i]);
            }

        }
    return fastTrack;
    }


    static void Main()
    {
        List<int> tracks = new List<int>();
        List<double> speeds = new List<double>();
        List<int> headings = new List<int>();
        List<int> result = FilterBySpeed(tracks, speeds, headings, 100.4);


        //int newTrackId = GetValidId();
        //int newSpeed = GetValidSpeed();
        //string category = categorySpeed(newSpeed);
        //int heading = GetValidHeading();
        //string status = GetValidStatus();
        AddTrack(tracks, speeds, headings, 1, 100, 150);
        AddTrack(tracks, speeds, headings, 2, 180, 240);
        //Console.WriteLine((ListAllTrack(tracks, speeds, headings)));
        Console.WriteLine(string.Join(", ", result));
        //RemoveById(tracks, speeds, headings, newTrackId);
        //Console.WriteLine(findById(tracks, speeds, headings, 1));


        //Console.WriteLine("=== Track Report ===");
        //Console.WriteLine($"The new trackid is: {newTrackId}");
        //Console.WriteLine($"The new speed is: {newSpeed} km/h ({category})");
        //Console.WriteLine($"Heading: {heading} degrees");
        //Console.WriteLine($"The new status is: {status}");
    }

}

