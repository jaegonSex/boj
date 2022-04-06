import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class Main {
    static class Member{
        int number;
        String name;
        public Member(int number, String name) {
            this.number = number;
            this.name = name;
        }
        @Override
        public String toString() {
            return  number + " " + name;

        }
    }
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int n = sc.nextInt();
        List<Member> memberList= new ArrayList<>();
        for (int i= 0; i <n; i++){
            int number = sc.nextInt();
            String name = sc.next();
            memberList.add(new Member(number, name));
        }
        memberList.sort(Comparator.comparingInt(m -> m.number));

        for (Member m:memberList
             ) {
            System.out.println(m.toString());
        }
        
    }
}
