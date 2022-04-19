import javax.swing.plaf.IconUIResource;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    static int seq =0;
    static class Computer {
        int id;
        int startTime;
        int endTime;
        int used;

        public Computer(int startTime, int endTime) {
            this.id = ++seq;
            this.startTime = startTime;
            this.endTime = endTime;
            this.used = 1;
        }

        boolean canUse(int time) {
            if (time < this.endTime) {
                return false;
            }
            return true;
        }

        void changeUser(int startTime, int endTime) {
            this.startTime = startTime;
            this.endTime = endTime;
            this.used++;
        }

    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        PriorityQueue<int[]> heabyong = new PriorityQueue<>(Comparator.comparingInt(c -> c[0]));

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int[] times = new int[2];
            times[0] = Integer.parseInt(st.nextToken());
            times[1] = Integer.parseInt(st.nextToken());
            heabyong.add(times);
        }
        List<Computer> result = new LinkedList<>();

        PriorityQueue<Computer> computers = new PriorityQueue<>(Comparator.comparingInt(c -> c.endTime));
        PriorityQueue<Computer> availableComputers = new PriorityQueue<>(Comparator.comparingInt(c-> c.id));

        while (!heabyong.isEmpty()){
            int[] times = heabyong.poll();
            while (!computers.isEmpty() && computers.peek().canUse(times[0])){
                availableComputers.add(computers.poll());
            }
            if (availableComputers.isEmpty()){
                Computer computer = new Computer(times[0],times[1]);
                computers.add(computer);
                result.add(computer);
            }
            else{
                Computer computer = availableComputers.poll();
                computer.changeUser(times[0],times[1]);
                computers.add(computer);
            }



        }
        System.out.println(result.size());
        result.stream().forEach(computer -> System.out.print(computer.used + " "));
    }
}
