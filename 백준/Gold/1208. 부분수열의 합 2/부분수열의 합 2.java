import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.IntStream;

public class Main {
    static long[] getSubsequences(int[] arr, int startIndex, int endIndex) {
        int size = endIndex - startIndex + 1;
        long[] result = new long[1 << size];
        for (int i = 0; i < (1 << size); i++) {
            long tmp = 0;
            for (int j = 0; j < size; j++) {
                if ((i | 1 << j) == i) {
                    tmp += arr[startIndex + j];
                }
            }
            result[i] = tmp;
        }

        return result;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        int[] A = new int[n];
        for (int i = 0; i < n; i++) {
            A[i] = Integer.parseInt(st2.nextToken());
        }
        long[] left = getSubsequences(A, 0, n / 2);
        long[] right = getSubsequences(A, n / 2 + 1, n - 1);
        Arrays.sort(left);
        Arrays.sort(right);

        int l = 0;
        int r = right.length - 1;
        long count = 0;
        while (l < left.length && r >= 0) {

            long sum = left[l] + right[r];

            if (sum < s) {
                l++;
            } else if (sum > s) {
                r--;
            } else {

                long cntL = 1;
                long cntR = 1;

                while (l+1 < left.length && left[l + 1] == left[l]) {
                    l++;
                    cntL++;
                }
                while (r -1 >= 0 &&  right[r-1] == right[r] ) {
                    r--;
                    cntR++;
                }
                l++;
                r--;

                count += (cntL * cntR);
            }
        }
        if (s == 0) {
            count--;
        }
        System.out.println(count);
    }
}



