#include <iostream>

int main() {
    int a = 10, b = 20;
    int *p = &a, *q = &b;
    
    *p = *q;
    std::cout << "*p = *q:" << std::endl;
    std::cout << "a=" << a << " b=" << b << std::endl;
    std::cout << "p=" << p << " q=" << q << std::endl;
    std::cout << "*p=" << *p << " *q=" << *q << std::endl;
    
    return 0;
}