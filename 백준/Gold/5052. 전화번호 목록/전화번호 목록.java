import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Stream;


public class Main {
    static class Node {
        boolean isLast;
        private Map<Character, Node> children;

        public Node() {
            children = new HashMap<>();
        }

        public Map<Character, Node> getChildren() {
            return children;
        }

        public boolean isLast() {
            return isLast;
        }

        public void setLast(boolean last) {
            isLast = last;
        }
    }

    static class Trie {
        Node root;

        public Trie() {
            root = new Node();
        }


        boolean insert(String str) {
            Node current = root;
            for (int i = 0; i < str.length(); i++) {
                char c = str.charAt(i);
                if (!current.getChildren().containsKey(c)) {
                    current.getChildren().put(c, new Node());
                }
                current = current.getChildren().get(c);
                if (current.isLast()) {
                    return false;
                }


            }
            current.setLast(true);
            return true;
        }


        boolean search(String str) {
            Node current = root;
            for (int i = 0; i < str.length(); i++) {
                char c = str.charAt(i);
                if (current.children.containsKey(c)) {
                    current = current.getChildren().get(c);
                } else {
                    return false;
                }
            }
            return current.isLast();
        }

    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            Trie trie = new Trie();
            int n = Integer.parseInt(br.readLine());
            List<String> book = new ArrayList<>();


            for (int j = 0; j < n; j++) {
                book.add(br.readLine());
            }
            book.sort((s1,s2)-> s1.length()-s2.length());

            boolean flag = true;
            for (String num:book) {
                if (!trie.insert(num)){
                    flag=false;
                };
            }

            if (flag){
                System.out.println("YES");
            }
            else{
                System.out.println("NO");
            }

        }

    }
}
