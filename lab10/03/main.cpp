#include <iostream>

int main() {
    int a = 5, b = 3;
    
    int c = a * b;
    
    int *p = &a;
    
    *p = 10;
    
    int d = a & b;
    
    int &ref = a;
    ref = 20;
    
    std::cout << "c = " << c << std::endl;
    std::cout << "*p = " << *p << std::endl;
    std::cout << "d = " << d << std::endl;
    std::cout << "ref = " << ref << std::endl;
    
    return 0;
}