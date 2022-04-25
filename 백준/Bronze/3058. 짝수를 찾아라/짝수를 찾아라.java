import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;
public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            IntSummaryStatistics collect = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt)
                    .filter(c->(c&1) ==0).collect(Collectors.summarizingInt(c -> c));
            System.out.println(collect.getSum() + " " + collect.getMin());
        }
    }
}