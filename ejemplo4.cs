int n = 0;
while (n < 5)
{
    Console.WriteLine(n);
    n++;
    bool condition = true;
    if (n == 3){
        condition = false;
    }

    if (condition)
    {
        Console.WriteLine("The variable is set to true.");
    }
    else
    {
        Console.WriteLine("The variable is set to false.");
    }
}