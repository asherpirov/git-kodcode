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

        if (speed <= 100)
        {
            return "slow";
        }
        else if (speed < 300)
        {
            return  "medium";
        }
        else
        {
            return  "fast";
        }
       
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


    //static string GetValidStatus()
    //{
    //    string status = "";
    //    string[] allowedStatuses =  { "cruising", "turning", "stopped", "accelerating" };

    //    bool validStatus = false;

    //    while (!validStatus)
    //    {
    //        Console.WriteLine("Please enter the status (cruising, turning, stopped, accelerating): ");
    //        string statusInput = Console.ReadLine();
    

    //        foreach (string allowedStatus in allowedStatuses)
    //        {
    //            if (statusInput == allowedStatus)

    //            {
    //                status = statusInput;
    //                validStatus = true;
    //                break;
    //            }
                
                
    //        }

    //    }
    //    if (!validStatus)
    //    {
    //        Console.WriteLine("Error: Please enter one of the exact status words.");
    //    }
    //    return status;
    //}

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
            result = $"[trackId: {tracks[i]}, speed: {speeds[i]} kn, heading: {headings[i]}]";
        }
        else
        {
           Console.WriteLine($"Error: Track {id} not found");
        }
     return result;


    }

    static string ListAllTrack(List<int> tracks, List<double> speeds, List<int> headings)
    {
        if (tracks.Count == 0)
        {
            return "The fleet is currently empty.";
        }


        string allLists = "";
        for (int i = 0; i < tracks.Count; i++)
        {
            allLists += $"[trackId: {tracks[i]}, speed: {speeds[i]} kn, heading: {headings[i]}]\n";
        }

        return allLists;

    }
    
    static List<int> FilterBySpeed(List<int> tracks, List<double> speeds, double threshold)
    {
        List<int> fastTrack = new List<int>();

        for (int i = 0; i< tracks.Count; i++)
        {
            if (speeds[i] > threshold)
            {
                fastTrack.Add(tracks[i]);
            }

        }
    return fastTrack;
    }

    static double CalculateAverage(List<double> speeds)
    {
        if (speeds.Count == 0)
        {
            return 0.0;
        }

        double sum = 0;

        foreach (double s in speeds)
        {
            sum += s;
        }
        return sum / speeds.Count;
    }

    static string Summarize(List<int> tracks, List<double> speeds)
    {
        double avgSpeed = CalculateAverage(speeds);
        List<int> fastestTracks = FilterBySpeed(tracks, speeds, 300);
        string fastTracksText = string.Join(",", fastestTracks);

        string fleet = $"Track count:{tracks.Count}\nAverage speed: {avgSpeed} kn\nFastest tracks (over 300 km/h): [TrackId: {fastTracksText}])";

        return fleet;
    }



    static void Main()
    {
        List<int> tracks = new List<int>();
        List<double> speeds = new List<double>();
        List<int> headings = new List<int>();


        while (true)
        {
            Console.WriteLine("==== Tracks Menu ====");
            Console.WriteLine("1.Add track");
            Console.WriteLine("2.Remove track");
            Console.WriteLine("3.Show all tracks");
            Console.WriteLine("4.Show fastest tracks");
            Console.WriteLine("5.Search track by id");
            Console.WriteLine("6.Show Reports");
            Console.WriteLine("7.Exit");

            Console.WriteLine("Enter your choice: ");
            string choice = Console.ReadLine();


            if (choice == "1")
            {
                int newTrackId = GetValidId();
                int newSpeed = GetValidSpeed();
                int heading = GetValidHeading();
                //string status = GetValidStatus();

                AddTrack(tracks, speeds, headings, newTrackId, newSpeed, heading);
                Console.WriteLine("Track added successfully!");
            }
            else if (choice == "2")
            {
                int newTrackId = GetValidId();
                RemoveById(tracks, speeds, headings, newTrackId);
            }
            else if (choice == "3")
            {
                Console.WriteLine(ListAllTrack(tracks, speeds, headings));
            }
            else if (choice == "4")
            {
                List<int> fastTracks = FilterBySpeed(tracks, speeds, 300);
                Console.WriteLine("Fastest tracks (over 300): " + string.Join(", ", fastTracks));
            }
            else if (choice == "5")
            {
                int searchId = GetValidId();
                Console.WriteLine(FindById(tracks, speeds, headings, searchId));
            }
            else if (choice == "6")
            {
                Console.WriteLine();
                Console.WriteLine(Summarize(tracks, speeds));
            }
            else if (choice == "7")
            {
                Console.WriteLine("Exiting program... Goodbye!");
                break;
            }
            else
            {
                Console.WriteLine("Error: not valid input, please try again");
            }
            
        }
      
    }

}