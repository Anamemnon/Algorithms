import java.math.BigInteger;

public class GCD {

    public static void main(String[] args) {
        BigInteger a;
        BigInteger b;
        try (java.util.Scanner scanner = new java.util.Scanner(System.in)) {
            a = scanner.nextBigInteger();
            b = scanner.nextBigInteger();
        }
        System.out.println(new GCD().getGCD(a,b));
    }
    //Алгоритм Евклида
    //Наибольший общий делитель
    private BigInteger getGCD(BigInteger a, BigInteger b){
        while (true){
            if (a.equals(BigInteger.ZERO)) return b;
            if (b.equals(BigInteger.ZERO)) return a;
            if (a.compareTo(b) >= 0) {
                a = a.mod(b);
            }else {
                b = b.mod(a);
            }
        }
    }
}
