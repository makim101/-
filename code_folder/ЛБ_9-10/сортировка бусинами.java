public class SimpleBeadSort {
    
    public static void beadSort(int[] numbers) {
        // Находим самое большое число
        int max = 0;
        for (int num : numbers) {
            if (num > max) {
                max = num;
            }
        }
        
        // Создаем "доску" с бусинами
        boolean[][] board = new boolean[numbers.length][max];
        
        System.out.println("Исходное расположение бусин:");
        printBoard(board, numbers);
        
        // Расставляем бусины (true - есть бусина, false - нет)
        for (int i = 0; i < numbers.length; i++) {
            for (int j = 0; j < numbers[i]; j++) {
                board[i][j] = true;
            }
        }
        
        System.out.println("\nБусины расставлены:");
        printBoard(board, numbers);
        
        // Даем бусинам упасть под действием гравитации
        for (int col = 0; col < max; col++) {
            int beadsInColumn = 0;
            
            // Считаем бусины в столбце
            for (int row = 0; row < numbers.length; row++) {
                if (board[row][col]) {
                    beadsInColumn++;
                    board[row][col] = false;
                }
            }
            
            // Бусины падают вниз
            for (int row = numbers.length - 1; row >= numbers.length - beadsInColumn; row--) {
                board[row][col] = true;
            }
        }
        
        System.out.println("\nБусины упали (отсортировались):");
        printBoard(board, numbers);
        
        // Собираем результат
        for (int i = 0; i < numbers.length; i++) {
            int count = 0;
            for (int j = 0; j < max; j++) {
                if (board[i][j]) {
                    count++;
                }
            }
            numbers[i] = count;
        }
    }
    
    // Красиво выводим доску с бусинами
    public static void printBoard(boolean[][] board, int[] numbers) {
        System.out.print("Числа: [");
        for (int i = 0; i < numbers.length; i++) {
            System.out.print(numbers[i]);
            if (i < numbers.length - 1) System.out.print(", ");
        }
        System.out.println("]");
        
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                System.out.print(board[i][j] ? "● " : "○ ");
            }
            System.out.println(" ← Строка " + i + " (" + numbers[i] + ")");
        }
    }
    
    public static void main(String[] args) {
        int[] numbers = {3, 2, 4, 1};
        
        System.out.println("ДО сортировки: " + java.util.Arrays.toString(numbers));
        System.out.println();
        
        beadSort(numbers);
        
        System.out.println();
        System.out.println("ПОСЛЕ сортировки: " + java.util.Arrays.toString(numbers));
    }
}
