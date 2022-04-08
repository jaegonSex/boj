import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static class Canvas {
        char[][] canvas;
        final char SPACE = ' ';
        final char POINT = 'o';
        final char DASH = '-';
        final char PIPE = '|';
        final char SLASH = '/';
        final char BACKSLASH = '\\';
        final char PLUS = '+';
        final char X = 'x';
        final char ASTERISK = '*';


        void makeCanvas(int x, int y) {
            canvas = new char[y + 2][x + 2];
            for (int i = 0; i < canvas.length; i++) {
                Arrays.fill(canvas[i], SPACE);
            }


        }

        void draw(int x, int y, char character) {
            if (character == SPACE) {
                canvas[x][y] = character;
            } else if (canvas[x][y] == SPACE || canvas[x][y] == character) {
                canvas[x][y] = character;
            } else if (character == PIPE && (canvas[x][y] == DASH || canvas[x][y] == PLUS)) {
                canvas[x][y] = PLUS;
            } else if (character == DASH && (canvas[x][y] == PIPE || canvas[x][y] == PLUS)) {
                canvas[x][y] = PLUS;
            } else if (character == SLASH && (canvas[x][y] == BACKSLASH || canvas[x][y] == X)) {
                canvas[x][y] = X;
            } else if (character == BACKSLASH && (canvas[x][y] == SLASH || canvas[x][y] == X)) {
                canvas[x][y] = X;
            } else {
                canvas[x][y] = ASTERISK;
            }

        }

        void point(int x, int y) {
            draw(y, x, POINT);
        }

        void line(int startX, int startY, int endX, int endY) {
            if (startY > endY) {
                int tmp = startY;
                startY = endY;
                endY = tmp;
                int tmp2 = startX;
                startX = endX;
                endX = tmp2;
            }


            if (startY == endY) {
                if (startX > endX) {
                    int tmp2 = startX;
                    startX = endX;
                    endX = tmp2;
                }
                for (int j = startX; j <= endX; j++) {
                    draw(startY, j, DASH);
                }


            } else if (startX == endX) {
                if (startY > endY) {
                    int tmp = startY;
                    startY = endY;
                    endY = tmp;
                }
                for (int i = startY; i <= endY; i++) {
                    draw(i, startX, PIPE);
                }

            } else if ((endY - startY) * (endX - startX) > 0) {
                int t = endY - startY;

                for (int i = 0; i <= t; i++) {

                    draw(startY + i, startX + i, BACKSLASH);
                }
            } else {
                int t = endY - startY;
                for (int i = 0; i <= t; i++) {
                    draw(startY + i, startX - i, SLASH);
                }
            }

        }

        void clear(int startX, int startY, int endX, int endY) {
            if (startY > endY) {
                int tmp = startY;
                startY = endY;
                endY = tmp;
                int tmp2 = startX;
                startX = endX;
                endX = tmp2;
            }
            if (endX > startX) {
                for (int i = startY; i <= endY; i++) {
                    for (int j = startX; j <= endX; j++) {
                        draw(i, j, SPACE);
                    }
                }
            } else {
                for (int i = startY; i <= endY; i++) {
                    for (int j = endX; j <= startX; j++) {
                        draw(i, j, SPACE);
                    }
                }
            }
        }

        void text(int x, int y, String str) {
            for (int i = 0; i < str.length(); i++) {
                if (i + x > canvas[0].length - 2) {
                    break;
                }
                draw(y, x + i, str.charAt(i));
            }
        }

        void print() {
            int y = canvas.length - 1;
            int x = canvas[0].length - 1;
            line(0, 0, x, 0);
            line(0, 0, 0, y);
            line(x, 0, x, y);
            line(0, y, x, y);


            for (int i = 0; i < canvas.length; i++) {

                for (int j = 0; j < canvas[i].length; j++) {
                    System.out.print(canvas[i][j]);
                }
                System.out.println();

            }
            System.out.println();

        }

    }

    static int num(String num) {
        return Integer.parseInt(num);
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Canvas canvas = new Canvas();
        while (true) {
            String[] com = br.readLine().split(" ");
            String command = com[0];
            if (command.chars().allMatch(Character::isDigit)) {
                if (num(command) == 0) {
                    break;
                } else {
                    canvas.makeCanvas(num(com[0]), num(com[1]));
                }
            } else {
                if (command.equals("LINE")) {
                    canvas.line(num(com[1]), num(com[2]), num(com[3]), num(com[4]));

                }
                if (command.equals("TEXT")) {
                    canvas.text(num(com[1]), num(com[2]), com[3]);

                }
                if (command.equals("CLEAR")) {
                    canvas.clear(num(com[1]), num(com[2]), num(com[3]), num(com[4]));

                }
                if (command.equals("POINT")) {
                    canvas.point(num(com[1]), num(com[2]));

                }
                if (command.equals("PRINT")) {
                    canvas.print();
                }

            }

        }


    }


}
