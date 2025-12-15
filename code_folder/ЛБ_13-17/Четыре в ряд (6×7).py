import numpy as np
import math
from typing import List, Tuple, Optional

class ConnectFour:
    """Класс для игры Четыре в ряд (Connect Four)."""
    
    def __init__(self, rows: int = 6, cols: int = 7):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((rows, cols), dtype=int)
        self.current_player = 1  # Игрок 1 начинает
        self.move_count = 0
        self.winning_length = 4
        
        # Предвычисленные направления для проверки победы
        self.directions = [
            (0, 1),   # горизонталь →
            (1, 0),   # вертикаль ↓
            (1, 1),   # диагональ ↘
            (1, -1)   # диагональ ↙
        ]
    
    def reset(self):
        """Сброс игры."""
        self.board.fill(0)
        self.current_player = 1
        self.move_count = 0
    
    def is_valid_move(self, col: int) -> bool:
        """Проверка, можно ли сделать ход в колонку."""
        return 0 <= col < self.cols and self.board[0, col] == 0
    
    def get_valid_moves(self) -> List[int]:
        """Получение списка всех допустимых ходов."""
        return [col for col in range(self.cols) if self.is_valid_move(col)]
    
    def make_move(self, col: int) -> bool:
        """Выполнение хода в указанную колонку."""
        if not self.is_valid_move(col):
            return False
        
        # Находим самую нижнюю свободную строку в колонке
        for row in range(self.rows - 1, -1, -1):
            if self.board[row, col] == 0:
                self.board[row, col] = self.current_player
                self.move_count += 1
                self.current_player = -self.current_player  # Смена игрока
                return True
        return False
    
    def undo_move(self, col: int) -> bool:
        """Отмена последнего хода в колонке."""
        for row in range(self.rows):
            if self.board[row, col] != 0:
                self.board[row, col] = 0
                self.move_count -= 1
                self.current_player = -self.current_player
                return True
        return False
    
    def check_winner(self) -> Optional[int]:
        """Проверка, есть ли победитель."""
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row, col] == 0:
                    continue
                
                player = self.board[row, col]
                
                for dr, dc in self.directions:
                    count = 1
                    
                    # Проверяем в одном направлении
                    for step in range(1, self.winning_length):
                        r, c = row + dr * step, col + dc * step
                        if (0 <= r < self.rows and 0 <= c < self.cols and 
                            self.board[r, c] == player):
                            count += 1
                        else:
                            break
                    
                    if count >= self.winning_length:
                        return player
        
        # Проверка на ничью
        if self.move_count == self.rows * self.cols:
            return 0  # Ничья
        
        return None  # Игра продолжается
    
    def evaluate_window(self, window: List[int], player: int) -> int:
        """Оценка окна из 4 клеток."""
        opponent = -player
        player_count = window.count(player)
        opponent_count = window.count(opponent)
        empty_count = window.count(0)
        
        # Эвристические веса
        if player_count == 4:
            return 10000  # Победа
        elif opponent_count == 4:
            return -10000  # Поражение
        elif player_count == 3 and empty_count == 1:
            return 100  # Почти выиграл
        elif opponent_count == 3 and empty_count == 1:
            return -1000  # Почти проиграл (блокировать!)
        elif player_count == 2 and empty_count == 2:
            return 10  # Хорошая позиция
        elif opponent_count == 2 and empty_count == 2:
            return -5  # Потенциальная угроза
        elif player_count == 1 and empty_count == 3:
            return 1  # Нейтрально
        else:
            return 0
    
    def evaluate_position(self, player: int) -> int:
        """Эвристическая оценка позиции для игрока."""
        score = 0
        
        # Центральные колонки ценнее
        center_array = list(self.board[:, self.cols // 2])
        center_count = center_array.count(player)
        score += center_count * 3
        
        # Оцениваем все возможные "окна" из 4 клеток
        
        # Горизонтальные окна
        for row in range(self.rows):
            for col in range(self.cols - 3):
                window = list(self.board[row, col:col+4])
                score += self.evaluate_window(window, player)
        
        # Вертикальные окна
        for col in range(self.cols):
            for row in range(self.rows - 3):
                window = list(self.board[row:row+4, col])
                score += self.evaluate_window(window, player)
        
        # Диагональные окна (↘)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                window = [self.board[row+i, col+i] for i in range(4)]
                score += self.evaluate_window(window, player)
        
        # Диагональные окна (↙)
        for row in range(self.rows - 3):
            for col in range(3, self.cols):
                window = [self.board[row+i, col-i] for i in range(4)]
                score += self.evaluate_window(window, player)
        
        return score

class ConnectFourAI:
    """ИИ для игры в Connect Four с использованием Minimax и Alpha-Beta."""
    
    def __init__(self, max_depth: int = 6):
        self.max_depth = max_depth
        self.nodes_evaluated = 0
        
        # Таблицы для быстрой сортировки ходов
        self.move_order = list(range(7))
        # Центральные колонки первыми
        self.move_order.sort(key=lambda x: abs(x - 3))
    
    def minimax(self, game: ConnectFour, depth: int, alpha: float, 
                beta: float, maximizing_player: bool) -> float:
        """Рекурсивный алгоритм Minimax с Alpha-Beta отсечением."""
        self.nodes_evaluated += 1
        
        # Проверяем терминальное состояние
        winner = game.check_winner()
        if winner is not None:
            if winner == 0:  # Ничья
                return 0
            elif winner == 1:  # Игрок 1 выиграл
                return 100000 + depth  # Чем быстрее победа, тем лучше
            else:  # Игрок -1 выиграл
                return -100000 - depth
        
        # Достигнута максимальная глубина
        if depth == 0:
            return game.evaluate_position(1)  # Оцениваем с точки зрения игрока 1
        
        valid_moves = game.get_valid_moves()
        
        # Сортировка ходов для лучшего отсечения
        valid_moves.sort(key=lambda x: abs(x - 3))  # Центр первыми
        
        if maximizing_player:
            max_eval = -math.inf
            
            for col in valid_moves:
                # Делаем ход
                game.make_move(col)
                
                # Рекурсивный вызов
                eval_score = self.minimax(game, depth - 1, alpha, beta, False)
                
                # Отменяем ход
                game.undo_move(col)
                
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                
                # Alpha-Beta отсечение
                if beta <= alpha:
                    break
            
            return max_eval
        
        else:  # minimizing player
            min_eval = math.inf
            
            for col in valid_moves:
                game.make_move(col)
                eval_score = self.minimax(game, depth - 1, alpha, beta, True)
                game.undo_move(col)
                
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                
                if beta <= alpha:
                    break
            
            return min_eval
    
    def find_best_move(self, game: ConnectFour) -> Optional[int]:
        """Нахождение лучшего хода для текущего игрока."""
        valid_moves = game.get_valid_moves()
        
        if not valid_moves:
            return None
        
        best_move = None
        self.nodes_evaluated = 0
        
        if game.current_player == 1:  # MAX игрок
            best_value = -math.inf
            
            for col in valid_moves:
                # Пробуем ход
                game.make_move(col)
                
                # Оцениваем позицию
                move_value = self.minimax(
                    game, self.max_depth - 1,
                    -math.inf, math.inf, False
                )
                
                # Отменяем ход
                game.undo_move(col)
                
                if move_value > best_value:
                    best_value = move_value
                    best_move = col
        
        else:  # MIN игрок (для симметрии, обычно ИИ играет за MAX)
            best_value = math.inf
            
            for col in valid_moves:
                game.make_move(col)
                move_value = self.minimax(
                    game, self.max_depth - 1,
                    -math.inf, math.inf, True
                )
                game.undo_move(col)
                
                if move_value < best_value:
                    best_value = move_value
                    best_move = col
        
        print(f"ИИ проанализировал {self.nodes_evaluated} позиций")
        print(f"Оценка лучшего хода: {best_value}")
        
        return best_move
    
    def iterative_deepening(self, game: ConnectFour, time_limit: float = 5.0) -> Optional[int]:
        """Итеративное углубление с ограничением по времени."""
        import time
        
        start_time = time.time()
        best_move = None
        
        for depth in range(1, self.max_depth + 1):
            if time.time() - start_time > time_limit:
                print(f"Прервано на глубине {depth-1} по времени")
                break
            
            print(f"\nАнализ на глубине {depth}...")
            current_best = self.find_best_move(game)
            
            if current_best is not None:
                best_move = current_best
            
            if abs(self.minimax(game, depth, -math.inf, math.inf, True)) > 90000:
                print(f"Найдена форсированная победа на глубине {depth}")
                break
        
        return best_move

# Визуализация доски
def print_board(board: np.ndarray):
    """Красивый вывод доски Connect Four."""
    print("\n  0 1 2 3 4 5 6")
    print("  " + "-" * 13)
    
    for row in range(board.shape[0]):
        print("|", end=" ")
        for col in range(board.shape[1]):
            cell = board[row, col]
            if cell == 1:
                print("X", end=" ")
            elif cell == -1:
                print("O", end=" ")
            else:
                print(".", end=" ")
        print("|")
    
    print("  " + "-" * 13)
    print("  0 1 2 3 4 5 6\n")

# Пример игры ИИ против ИИ
if __name__ == "__main__":
    print("=== CONNECT FOUR (Четыре в ряд) ===")
    print("ИИ с алгоритмом Minimax + Alpha-Beta Pruning")
    print("Доска: 6 строк × 7 колонок\n")
    
    # Создаём игру
    game = ConnectFour()
    ai = ConnectFourAI(max_depth=6)
    
    print("Начальная позиция:")
    print_board(game.board)
    
    # Играем несколько ходов
    for move_num in range(1, 10):
        current_player = "X" if game.current_player == 1 else "O"
        print(f"\nХод {move_num}. Ходит: {current_player}")
        
        if current_player == "X":  # ИИ за X
            print("ИИ анализирует позицию...")
            best_col = ai.find_best_move(game)
            
            if best_col is not None:
                print(f"ИИ выбирает колонку {best_col}")
                game.make_move(best_col)
            else:
                print("Нет возможных ходов!")
                break
        else:  # Человек или случайный ход за O
            valid_moves = game.get_valid_moves()
            # Для демо: выбираем случайный ход
            import random
            if valid_moves:
                random_move = random.choice(valid_moves)
                print(f"Случайный ход в колонку {random_move}")
                game.make_move(random_move)
            else:
                print("Нет возможных ходов!")
                break
        
        print_board(game.board)
        
        # Проверяем победителя
        winner = game.check_winner()
        if winner is not None:
            if winner == 1:
                print("🎉 ИГРОК X (ИИ) ВЫИГРАЛ!")
            elif winner == -1:
                print("🎉 ИГРОК O ВЫИГРАЛ!")
            else:
                print("🤝 НИЧЬЯ!")
            break
    
    print("\n" + "="*50)
    print("Статистика:")
    print(f"Всего ходов: {game.move_count}")
    print(f"Проанализировано узлов: {ai.nodes_evaluated}")
