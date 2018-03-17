public class Fibonacci {

    public static void main(String[] args) {
        int n = 0;
        try (java.util.Scanner scanner = new java.util.Scanner(System.in)) {
            if (scanner.hasNextInt()) {
                n = scanner.nextInt();
            }
        }
//        Решение по формуле Бине
//        System.out.println(Math.round((Math.pow((1 + Math.sqrt(5)) / 2, n) - Math.pow((1 - Math.sqrt(5)) / 2, n)) / Math.sqrt(5)));

//        Решение "вручную"
        if (n == 0) {
            System.out.println(0);
            return;
        }else if (n == 1) {
            System.out.println(1);
            return;
        }
        int f[] = new int[n + 1];
        f[0] = 0;
        f[1] = 1;
        for (int i = 2; i <= n; ++i) {
            f[i] = f[i - 1] + f[i - 2];
        }
        System.out.println(f[n]);
        //Выполняет 2n + 2 строки кода
        //Т(100) = 202
    }
}
