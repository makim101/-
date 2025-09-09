#список
import java.util.ArrayList;  				#подключение джавы
public class Main {  
public static void main(String args) {  
ArrayList<String> students = new ArrayList<String>();	#создан новый объект ArrayList с именем students  
}  
}  

#стек на основе массива
public class MyStack {
    private int[] stackArray;  							#массив для хранения элементов стека
    private int top;           							#индекс верхнего элемента
    private int capacity;      							#максимальная вместимость стека
    
public MyStack(int size) {							#создаём стек заданного размера
        stackArray = new int[size];
        capacity = size;
        top = -1; 					 			#стек пуст, поэтому верх указывает "ниже первого элемента"
    }

    										#Добавление элемента в стек
	public void push(int value) {
        if (isFull()) {
            System.out.println("Стек переполнен! Нельзя добавить " + value);
            return;
        }
        stackArray[++top] = value;						#увеличиваем top и вставляем элемент
    }

    										#Удаление и возврат верхнего элемента (операция pop)
    public int pop() {
        if (isEmpty()) {
            System.out.println("Стек пуст! Нечего удалять.");
            return -1;
        }
        return stackArray[top--]; 						#возвращаем верхний элемент и уменьшаем top
    }

    										#Просмотр верхнего элемента без удаления (операция peek)
    public int peek() {
        if (isEmpty()) {
            System.out.println("Стек пуст! Нет верхнего элемента.");
            return -1;
        }
        return stackArray[top];
    }

    										#Проверка: пуст ли стек
    public boolean isEmpty() {
        return top == -1;
    }

   										#Проверка: заполнен ли стек
    public boolean isFull() {
        return top == capacity - 1;
    }

    										#Вывод содержимого стека
    public void printStack() {
        if (isEmpty()) {
            System.out.println("Стек пуст.");
            return;
        }
        System.out.print("Элементы стека: ");
        for (int i = 0; i <= top; i++) {
            System.out.print(stackArray[i] + " ");
        }
        System.out.println();
    }