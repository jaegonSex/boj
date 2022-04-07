import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static long[][] matrixProduct(long[][] m1, long[][] m2) {
        int a = m1.length;
        int b = m2[0].length;
        int c = m2.length;

        long[][] result = new long[a][b];
        for (int i = 0; i < a; i++) {
            for (int j = 0; j < b; j++) {
                for (int k = 0; k < c; k++) {
                    result[i][j] += ((m1[i][k] % 1000000007) * (m2[k][j] % 1000000007)) % 1000000007 ;
                    result[i][j] = result[i][j] % 1000000007;
                }

            }
        }
        return result;
    }

    static long[][] matrixPower(long[][] m, long power) {
        if (power == 1) {
            return m;
        }
        long[][] half = matrixPower(m, power / 2);
        if ((power & 1) == 0) {
            return matrixProduct(half, half);
        }
        return matrixProduct(matrixProduct(half, half), m);
    }


    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        long n = sc.nextLong();
        long[][] arr = {{1,1},{1,0}};
        long[][] tmp = matrixPower(arr, n);

        System.out.println(tmp[1][0]);

    }


}
