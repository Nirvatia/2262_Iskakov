#include <iostream>

int main() {
    int n;
    std::cin >> n;

    bool found = false;

    for (int i = 0; i < n; i++) {
        int x;
        std::cin >> x;

        if (x < 0) {
            found = true;
            std::cout << x << std::endl;
            break;
        }
    }

    if (!found) {
        std::cout << "Отрицательных чисел нет." << std::endl;
    }

    return 0;
}