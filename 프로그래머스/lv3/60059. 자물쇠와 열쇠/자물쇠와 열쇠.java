import java.util.Arrays;

class Solution {

    public boolean solution(int[][] key, int[][] lock) {
        int emptyCount = (int) Arrays.stream(lock).flatMapToInt(Arrays::stream).filter(val -> val == 0).count();
        int n = lock.length;
        int m = key.length;
        int[][][] keys = new int[4][m][m];
        keys[0] = key;
        for (int i = 1; i < 4; i++) keys[i] = getRotatedKey(keys[i - 1]);

        for (int i = -m + 1; i < n; i++) {
            for (int j = -m + 1; j < n; j++) {
                for (int k = 0; k < 4; k++) {
                    if (matchCount(i, j, keys[k], lock) == emptyCount) return true;
                }
            }
        }
        return false;
    }

    private int[][] getRotatedKey(int[][] key) {

        int n = key.length;
        int[][] newKey = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                newKey[j][n - 1 - i] = key[i][j];
            }
        }
        return newKey;
    }

    private int matchCount(int x, int y, int[][] key, int[][] lock) {
        int count = 0;
        int sx = Math.max(0, x);
        int sy = Math.max(0, y);
        int ex = Math.min(x + key.length, lock.length);
        int ey = Math.min(y + key.length, lock[0].length);

        for (int i = sx; i < ex; i++) {
            for (int j = sy; j < ey; j++) {
                if (key[i - x][j - y] == 1 && lock[i][j] == 1) return -1;
                if (key[i - x][j - y] == 1 && lock[i][j] == 0) ++count;
            }
        }

        return count;
    }
}