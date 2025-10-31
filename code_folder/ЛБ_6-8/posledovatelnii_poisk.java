public class LinearSearch {
    
    // Функция линейного поиска
    public static int linearSearch(int[] arr, int target) {
        // Проходим по всем элементам массива
        for (int i = 0; i < arr.length; i++) {
            // Если нашли искомый элемент
            if (arr[i] == target) {
                return i; // Возвращаем индекс найденного элемента
            }
        }
        return -1; // Возвращаем -1, если элемент не найден
    }
    
    public static void main(String[] args) {
        // Создаем массив
        int[] array = {3, 5, 2, 7, 9, 1, 4};
        
        int target = 7; // Искомое значение
        
        // Вызываем функцию поиска
        int result = linearSearch(array, target);
        
        // Выводим результат
        if (result != -1) {
            System.out.println("Элемент найден на позиции: " + result);
        } else {
            System.out.println("Элемент не найден");
        }
    }
}
