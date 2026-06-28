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
        if (!IsActive)
        {
            Console.WriteLine("Error, the account not active.");
            return;
        }
        if (amount <= 0)
        {
            Console.WriteLine("Error: Amount must be positive.");
            return;
        }
    Balance += amount;
    _transactionHistory.Add($"Deposited ${amount:F2}");
    }

    public bool Withdraw(double amount)
    {
        if (!IsActive)
        {
            Console.WriteLine("Error, the account not active.");
            return false;
        }

        if (amount <= 0)
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
        if (!to.IsActive)
        {
            Console.WriteLine("Error: Destination account is inactive.");
            return false;
        }
        if (from.Withdraw(amount))
        {
            to.Deposit(amount);
            return true;
        }

        return false;
    }
}

class Program
{
    public static void Main()
    {

        List<BankAccount> ListOfBankAccount = new List<BankAccount>();

        ListOfBankAccount.Add(new BankAccount(8801, "Itay Levi", 5500.0, "Savings")); 
        ListOfBankAccount.Add(new BankAccount(8802, "Noa Cohen")); 
        ListOfBankAccount.Add(new BankAccount(8803, "  ", -400, "invalid_type"));
        ListOfBankAccount.Add(new BankAccount(8804, "Asher Pirov", 14000.0, "Business"));
        ListOfBankAccount.Add(new BankAccount(8805, "Tamar Avraham", 950.0, "Savings"));

        Console.WriteLine("=== All Bank Accounts ===");
        foreach (BankAccount account in ListOfBankAccount)
        {
            Console.WriteLine(account.ToString());
        }

        Console.WriteLine("\n=== Performing Transactions ===");
        ListOfBankAccount[0].Deposit(1500);
        ListOfBankAccount[1].Deposit(3000); 
        ListOfBankAccount[0].Withdraw(700); 
        ListOfBankAccount[1].Withdraw(5000);

        Console.WriteLine("\n=== Testing Account Status ===");
        ListOfBankAccount[4].DeActivate();
        ListOfBankAccount[4].Deposit(500);
        ListOfBankAccount[4].Activate();

        Console.WriteLine("\n=== Applying Interest ===");
        foreach (BankAccount acc in ListOfBankAccount)
        {
            acc.ApplyInterest();
        }

        Console.WriteLine("\n=== Transferring Money ===");
        Console.WriteLine($"Before: {ListOfBankAccount[3]}");
        Console.WriteLine($"Before: {ListOfBankAccount[4]}");

        BankAccount.Transfer(ListOfBankAccount[3], ListOfBankAccount[4], 400);

        Console.WriteLine($"After: {ListOfBankAccount[3]}");
        Console.WriteLine($"After: {ListOfBankAccount[4]}");

        Console.WriteLine("\n=== Printing Transaction History ===");
        Console.WriteLine("-- History for Itay Levi --");
        ListOfBankAccount[0].PrintTransactionHistory();

        Console.WriteLine("\n-- History for Noa Cohen --");
        ListOfBankAccount[1].PrintTransactionHistory();

        Console.WriteLine("\n=== Final Accounts Status ===");
        foreach (BankAccount acc in ListOfBankAccount)
        {
             Console.WriteLine(acc);
        }

    }
}
