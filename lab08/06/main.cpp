#define forc(i, from, to) \
{ \
   int __i = from, __n = to; \
   for(const int &i = __i; i < __n; __i++) {

#define end_forc \
   } \
}

int main() {    
    forc(i, 0, 100) {
        i = 999;
    }
    end_forc;

    return 0;
}