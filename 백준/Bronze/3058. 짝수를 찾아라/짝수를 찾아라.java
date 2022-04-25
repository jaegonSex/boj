import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.OptionalInt;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
        List<Integer> collect = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).collect(Collectors.toList());
            int minVal = collect.stream().mapToInt(c -> c).filter(c -> (c & 1) == 0).min().getAsInt();
            int sum = collect.stream().mapToInt(c -> c).filter(c -> (c & 1) == 0).sum();
            System.out.println(sum + " " + minVal);
        }


    }
}



