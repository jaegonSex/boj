import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    static class Sobang {
        int a;
        int b;


        public Sobang(int a, int b) {
            this.a = a;
            this.b = b;

        }
    }

    public static void main(String[] args) throws IOException {
        final int MOD = 40000;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<Sobang> sobangList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            sobangList.add(new Sobang(a, b));
        }
        List<Sobang> collect = sobangList.stream().sorted(new Comparator<Sobang>() {
            @Override
            public int compare(Sobang o1, Sobang o2) {
                if (o1.b * o2.a > o1.a * o2.b) {
                    return 1;
                } else if (o1.b * o2.a == o1.a * o2.b) {
                    return o2.a - o1.a;
                } else {
                    return -1;
                }
            }
        }).collect(Collectors.toList());

        int t = 0;
        for (Sobang s :
                collect) {
            t += (s.a % MOD * t % MOD) % MOD + s.b % MOD;
            t %= MOD;
        }
        System.out.println(t);


    }


}



