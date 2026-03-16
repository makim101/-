#include <iostream>
#include <string>
using namespace std;

class Animal {
    private:
        string name;
        string type;
        int age;
        string status;

    public:
        Animal(string nameVal, string typeVal, int ageVal, string statusVal) {
            setName(nameVal);
            setType(typeVal);
            setAge(ageVal);
            setStatus(statusVal);
        }

        //геттеры
        string getName() const { return name; }
        string getType() const { return type; }
        int getAge() const { return age; }
        string getStatus() const { return status; }

        //сеттеры
        void setName(const string& newName) {
            if (!newName.empty()) {
                name = newName;
            } 
            else {
                cout << "Кличка не может быть пустой." << endl;
            }
        }

        void setType(const string& newType) {
            if (newType == "кошка" || newType == "собака") {
                type = newType;
            } 
            else {
                cout << "Вид должен быть 'кошка' или 'собака'. Установлено 'Не указан'." << endl;
                type = "Не указан";
            }
        }

        void setAge(int newAge) {
            if (newAge >= 0 && newAge <= 30) {
                age = newAge;
            } 
            else {
                cout << "Возраст должен быть от 0 до 30." << endl;
            }
        }

        void setStatus(const string& newStatus) {
            if (newStatus == "в приюте" || newStatus == "пристроен") {
                status = newStatus;
            } 
            else {
                cout << "Статус должен быть 'в приюте' или 'пристроен'." << endl;
            }
        }

        //обновление возраста и статуса
        void updateAge(int newAge) {
            setAge(newAge);
            if (age == newAge) {
                cout << "Возраст животного " << name << " обновлён на " << age << endl;
            }
        }
        void updateStatus() {
        if (status == "в приюте") {
            status = "пристроен";
            cout << "Статус животного " << name << " обновлён на 'пристроен'" << endl;
        } 
        else {
            cout << "Животное " << name << " уже пристроено" << endl;
        }
        }

        void printInfo() const {
            cout << "=========================" << endl;
            cout << "Информация о животном" << endl;
            cout << "Кличка:  " << name << endl;
            cout << "Вид:     " << type << endl;
            cout << "Возраст: " << age << " лет(года)" << endl;
            cout << "Статус:  " << status << endl;
            cout << "=========================" << endl;
        }
};

int main() {
    setlocale(LC_ALL, "Russian");

    Animal animal("Барсик", "кошка", 3, "в приюте");
    
    animal.printInfo();
    animal.updateAge(6);
    animal.updateStatus();
    animal.printInfo();
    return 0;
}
