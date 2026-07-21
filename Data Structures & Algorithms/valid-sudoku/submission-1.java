class Solution {
    public boolean isValidSudoku(char[][] board) {
        List<HashSet<Character>> boxesOfRules = new ArrayList<>();

        for (int i = 0; i < 9; i++) {
            HashSet<Character> row = new HashSet<>(); 
            HashSet<Character> column = new HashSet<>(); 
            for (int j = 0; j < 9; j++) {
                char rowEl = board[i][j];
                char colEl = board[j][i];
                if (row.contains(rowEl)) return false;
                if (column.contains(colEl)) return false;
                if (rowEl != '.') row.add(rowEl);
                if (colEl != '.') column.add(colEl);
            } 
        }

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                HashSet<Character> box = new HashSet<>();
                for (int x = 0; x < 3; x++) {
                    for (int y = 0; y < 3; y++) {
                        char el = board[i * 3 + x][j * 3 + y];
                        if (box.contains(el)) return false;
                        if (el != '.') box.add(el);
                    }
                }
            }
        }

        return true;
    }
}
