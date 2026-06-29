using System;
namespace Day2;

abstract class Platform
{
    private int _trackid;
    private double _speedKnots;
    private double _heading;
    protected int TrackId { get => _trackid;

       private set
        {
            if (value < 0)
            {
                throw new ArgumentException("The TrackId must be positive.");
            }
            _trackid = value;
        }
    }
    protected double SpeedKnots
    { get => _speedKnots;

      set
        {
            if (value < 0)
            {
                throw new ArgumentException("The SpeedKnots must be positive.");
            }
            _speedKnots = value;
        }
    }

    protected double Heading
    {
        get => _heading;

        set
        {
            if (value < 0 || value > 359)
            {
                throw new ArgumentException("The Heading must be between 0-359.");
            }
            _heading = value;
        }
    }

    protected Platform(int trackId, double speedKnots, double heading)
    {

        TrackId = trackId;
        SpeedKnots = speedKnots;
        Heading = heading;

    }
    public abstract string StatusLine();
    public abstract bool IsTrackable();

    public override string ToString()
    {
        return $"[ID: {TrackId}, Speed: {SpeedKnots} kn, Heading: {Heading}°]";
    }


}

class AirPlatform : Platform
{
    protected double AltitudeFeet { get; set; }
    public AirPlatform(int trackId, double speedKnots, double heading, double altitudeFeet)
       : base(trackId, speedKnots, heading)
    {
         AltitudeFeet = altitudeFeet;
    }
    public override string StatusLine() => $"AirPlatform {TrackId}, {SpeedKnots} kn, {Heading}, {AltitudeFeet} ft";
    public override bool IsTrackable() => (AltitudeFeet >= 100 && AltitudeFeet <= 60000 && SpeedKnots > 0);



}

class SeaPlatform : Platform
{
    protected double DepthMeters { get; set; }

    public SeaPlatform(int trackId, double speedKnots, double heading, double depthMeters)
        : base(trackId, speedKnots, heading)
    {
        DepthMeters = depthMeters;
    }
    public override string StatusLine() => $"SeaPlatform {TrackId}: {SpeedKnots} kn, {Heading}°, Depth: {DepthMeters} m";
    public override bool IsTrackable() => (0 <= DepthMeters && DepthMeters <= 300);


}

class GroundPlatform : Platform
{
    private string _terrainType = string.Empty;
    protected string TerrainType
    {
        get => _terrainType;

        set
        {

            if (string.IsNullOrWhiteSpace(value))
            {
                throw new ArgumentException("The TerrainType cennot be null or empty.");
            }

            _terrainType = value;
        }
    }

    public GroundPlatform(int trackId, double speedKnots, double heading, string terrainType)
        : base (trackId, speedKnots, heading)
    {
        TerrainType = terrainType;
    }

    public override string StatusLine() => $"GroundPlatform {TrackId}: {SpeedKnots} kn, {Heading}°, Terrain: {TerrainType}";
    public override bool IsTrackable() => (TerrainType != "tunnel");


}

class Program
{
    public static void Main()
    {

        List<Platform> platformList = new List<Platform>();

        platformList.Add(new AirPlatform(1, 400, 98, 20000));
        platformList.Add(new AirPlatform(2, 1100, 158, 10));
        platformList.Add(new SeaPlatform(3, 30, 55, 70));
        platformList.Add(new SeaPlatform(4, 30, 155, 700));
        platformList.Add(new GroundPlatform(5, 130, 75, "tunnel"));
        platformList.Add(new GroundPlatform(6, 80, 55, "road"));

        Console.WriteLine("=== RADAR REPORT ===");

        foreach (Platform paltform in platformList)
        {
            Console.WriteLine($"{paltform.StatusLine()} | Trackable: {paltform.IsTrackable()}");
        }
       
    }

}
    