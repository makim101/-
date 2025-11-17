def solve_sudoku(board):
    def print_board_with_highlight(row, col, num):
        """Вспомогательная функция для визуализации процесса"""
        print(f"Пробуем поставить {num} в клетку ({row}, {col})")
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            row_str = ""
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    row_str += "| "
                if i == row and j == col:
                    row_str += f"*{num}* "
                else:
                    row_str += f"{board[i][j] if board[i][j] != 0 else '.'} "
            print(row_str)
        print()
    
    def is_valid(row, col, num):
        """Проверка, можно ли поставить число в клетку"""
        # Проверка строки
        for j in range(9):
            if board[row][j] == num:
                return False
        
        # Проверка столбца
        for i in range(9):
            if board[i][col] == num:
                return False
        
        # Проверка квадрата 3x3
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        
        return True
    
    def find_empty():
        """Поиск следующей пустой клетки"""
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None
    
    def backtrack():
        """Основная рекурсивная функция backtracking"""
        empty_cell = find_empty()
        
        # Базовый случай: нет пустых клеток - решение найдено
        if not empty_cell:
            return True
        
        row, col = empty_cell
        
        # Пробуем числа от 1 до 9
        for num in range(1, 10):
            if is_valid(row, col, num):
                # Делаем ход
                board[row][col] = num
                print_board_with_highlight(row, col, num)
                
                # Рекурсивно решаем остальную часть
                if backtrack():
                    return True
                
                # Откат (backtrack)
                print(f"Откат: убираем {num} из клетки ({row}, {col})")
                board[row][col] = 0
        
        return False
    
    print("Начальная доска судоку:")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        row_str = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row_str += "| "
            row_str += f"{board[i][j] if board[i][j] != 0 else '.'} "
        print(row_str)
    print()
    
    return backtrack()

# Пример использования
if __name__ == "__main__":
    # Пример доски судоку (0 - пустые клетки)
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print("=== Решение судоку ===")
    if solve_sudoku(sudoku_board):
        print("\nРешение найдено!")
        print("Финальная доска:")
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            row_str = ""
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    row_str += "| "
                row_str += f"{sudoku_board[i][j]} "
            print(row_str)
    else:
        print("Решение не найдено!")
