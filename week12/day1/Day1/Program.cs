using System;
namespace Day1;

public enum accountTypes { Checking, Savings, Business }
class BankAccount
{

    private int _accountNumber;
    private string _ownerName;
    private double _balance;
    private string _accountType;
    private bool _isActive;
    private List<string> _transactionHistory;


    public int AccountNumber { get => _accountNumber; }
    public string OwnerName
    {
        get => _ownerName;
        set
        {
            if (string.IsNullOrWhiteSpace(value))
            { _ownerName = "Unknown"; }

            else { _ownerName = value; }
        }
    }
    public double Balance
    {
        get => _balance;

        set
        {
            if (value < 0.0)
            { _balance = 0.0; }
            else { _balance = value; }
        }
    }

    public string AccountType
    {
        get => _accountType;
        set
        {
            if (Enum.TryParse<accountTypes>(value, true, out accountTypes result))
            {
                _accountType = result.ToString();
            }
            else { _accountType = accountTypes.Checking.ToString(); }

        }
    }
    public bool IsActive
    {
        get => _isActive;
        private set
        {
            _isActive = value;

        }

    }

    public void Activate()
    {
        IsActive = true;
    }

    public void DeActivate()
    {
        IsActive = false;
    }

    public BankAccount(int accountNumber, string ownerName, double balance, string accountType)
        {
            _accountNumber = accountNumber;
            OwnerName = ownerName;
            Balance = balance;
            AccountType = accountType;

            IsActive = true;
            _transactionHistory = new List<string>();

        }
    public BankAccount(int accountNumber, string ownerName)
        : this(accountNumber, ownerName, 0.0, "Checking") { }


    public override string ToString()
    {
        return $"Account {AccountNumber} | Owner: {OwnerName} | Balance: {Balance:F2}$ | Type: {AccountType}";
    }

    public void Deposit(double amount)

    {
        if (IsActive = true)
        {

        }
        if (amount > 0)
        {
            Balance += amount;
            _transactionHistory.Add($"Deposit ${amount:F2}");

        }
        else { Console.WriteLine("Error, the amonut must be positive."); }
    }

    public bool Withdraw(double amount)
    {
        if (!IsActive)
        {
            Console.WriteLine("Error, the account not active.");
            return false;
        }

        if (amount < 0)
        {
            Console.WriteLine("Error, the amonut must be positive.");
            return false;

        }
        if (Balance < amount)
        {
            Console.WriteLine("Error, There is not enough money in the account.");
            return false;
        }

        Balance -= amount;
        _transactionHistory.Add($"Withdrew ${amount:F2}");
        return true;
    }

    public void ApplyInterest()
    {
        if (IsActive && AccountType == "Savings")
        {
            double interest = Balance * 0.02;
            Balance += interest;
            _transactionHistory.Add($"Applied Interest ${interest:F2}");
        }
       
    }

    public void PrintTransactionHistory()
    {
        for (int i = 0; i < _transactionHistory.Count; i++)
        {
            Console.WriteLine(_transactionHistory[i]);
        }
    }

    public static bool Transfer(BankAccount from, BankAccount to, double amount)
    {
        
    }

class Program
{
    public void Main()
    {

    }
}





