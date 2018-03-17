
public class GCD {

    public static void main(String[] args) {
        long a = 0;
        long b = 0;
        try (java.util.Scanner scanner = new java.util.Scanner(System.in)) {
            a = scanner.nextLong();
            b = scanner.nextLong();
        }
        System.out.println(getGCD(a,b));
    }
    //Алгоритм Евклида
    //Наибольший общий делитель
    private static long getGCD(long a, long b){
        if (a == 0) return b;
        if (b == 0) return a;
        if (a >= b) return getGCD(a % b, b);
        if (b >= a) return getGCD(a, b % a);
        return -1;
    }
}
