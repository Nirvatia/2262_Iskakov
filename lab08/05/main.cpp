#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> v(n);

    for (int& i : v) {
        std::cin >> i;
    }

    int positive_nums_count = 0;
    int negative_nums_count = 0;
    int last = v.back();

    for (int& i : v) {
        i += last;  
        if (i < 0) negative_nums_count++;
        if (i > 0) positive_nums_count++;
    }

    std::cout << "Положительных чисел: " << positive_nums_count << "\n" << "Отрицательных чисел: " << negative_nums_count << "\n";

    return 0;
}