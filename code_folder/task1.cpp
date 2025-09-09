#cписок
list<int> listData											#создание пустого списка
listData.push_back(10), listData.push_back(20), listData.push_back(30), listData.push_back(40)		#добавление элементов
cout << "List elements:"; for (int num : listData) { cout << " " << num; } cout << endl; return 0;	#печать элементов


#стек
int main() {
    stack<int> st;	
    st.push(10);	#кладем значения в стек
    st.push(20);
    st.push(30);
    st.push(40);

    cout << st.top();	#достаем верхний элемент
    return 0;
}			#он выведет чилсло 40