namespace AtCorder
{
    class AtCorder001
    {
        static void Main(string[] args)
        {
            string length = System.Console.ReadLine();
            string[] lineA = System.Console.ReadLine().Trim().Split(' ');
            string[] lineB = System.Console.ReadLine().Trim().Split(' ');

            int result = 0;
            for (int i = 0; i < int.Parse(length); i++)
            {
                result += int.Parse(lineB[i + 1]) - int.Parse(lineA[i + 1]) + 1; 
             
            }

            Console.WriteLine(result);

        }
    }

}
