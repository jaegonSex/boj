import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] count = new int[2][3];

        for (int i = 0; i < n; i++) {
            int leftMin = Math.min(count[0][0],count[0][1]);
            int midMin = Math.min(Math.min(count[0][0],count[0][1]),count[0][2]);
            int rightMin = Math.min(count[0][1],count[0][2]);
            int leftMax = Math.max(count[1][0],count[1][1]);
            int midMax = Math.max(Math.max(count[1][0],count[1][1]),count[1][2]);
            int rightMax = Math.max(count[1][1],count[1][2]);
            int left = sc.nextInt();
            int mid = sc.nextInt();
            int right = sc.nextInt();
            count[0][0] = leftMin + left;
            count[0][1] = midMin + mid;
            count[0][2] = rightMin +right;
            count[1][0] = leftMax + left;
            count[1][1] = midMax+ mid;
            count[1][2] = rightMax +right;
        }
        System.out.println(Arrays.stream(count[1]).max().getAsInt() + " " + Arrays.stream(count[0]).min().getAsInt());

    }


}
