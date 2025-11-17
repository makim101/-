class TreeNode:
    """Класс узла бинарного дерева"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

def count_leaves(root, depth=0):

    indent = "  " * depth
    print(f"{indent}Узел: {root.data if root else 'None'}, глубина: {depth}")
    
    # Базовый случай: пустое дерево
    if root is None:
        print(f"{indent}Пустой узел - возвращаем 0")
        return 0
    
    # Базовый случай: лист (нет потомков)
    if root.left is None and root.right is None:
        print(f"{indent}Найден лист: {root.data}")
        return 1
    
    print(f"{indent}Узел {root.data} не является листом, проверяем потомков")
    
    # Рекурсивный случай: сумма листьев в левом и правом поддеревьях
    left_count = count_leaves(root.left, depth + 1)
    right_count = count_leaves(root.right, depth + 1)
    
    total = left_count + right_count
    print(f"{indent}Узел {root.data}: левых листьев={left_count}, правых листьев={right_count}, всего={total}")
    
    return total

def print_tree(root, depth=0):
    """Вспомогательная функция для визуализации дерева"""
    if root is None:
        return
    
    indent = "  " * depth
    print(f"{indent}{root.data}")
    
    if root.left or root.right:
        if root.left:
            print_tree(root.left, depth + 1)
        else:
            print(f"{indent}  None")
        
        if root.right:
            print_tree(root.right, depth + 1)
        else:
            print(f"{indent}  None")

# Пример использования
if __name__ == "__main__":
    # Создаем тестовое дерево
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    #      /
    #     7
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.right.left = TreeNode(7)
    
    print("Структура дерева:")
    print_tree(root)
    print("\n=== Подсчет листьев ===")
    
    leaves_count = count_leaves(root)
    print(f"\nОбщее количество листьев: {leaves_count}")
    
    # Проверка: листья должны быть 4, 7, 6
    expected_leaves = [4, 7, 6]
    print(f"Ожидаемые листья: {expected_leaves}")
