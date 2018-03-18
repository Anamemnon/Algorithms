public class Fibonacci {

    private static final int MOD = (int) (1e9+7);

    private int fibonacci(int n){
        int a = 0;
        int b = 1;
        for(int i = 0; i < n; ++i){
            int c = (a + b) % MOD;
            a = b;
            b = c;
        }
        return a;
    }
    public static void main(String[] args) {
        int n = 0;
        System.out.print("Введите число: ");
        try (java.util.Scanner scanner = new java.util.Scanner(System.in)) {
            n = scanner.nextInt();
        }
        System.out.println(new Fibonacci().fibonacci(n));

//        Решение по формуле Бине
//        System.out.println(Math.round((Math.pow((1 + Math.sqrt(5)) / 2, n) - Math.pow((1 - Math.sqrt(5)) / 2, n)) / Math.sqrt(5)));

    }
}
