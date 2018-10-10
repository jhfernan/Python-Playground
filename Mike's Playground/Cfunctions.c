int main() 
{ 

    // fun_ptr is a pointer to function fun()  

    void (*fun_ptr)(int) = &fun; 

  

    /* 
    
       The above line is equivalent of following two 

       void (*fun_ptr)(int); 

       fun_ptr = &fun;  

    */

  

    // Invoking fun() using fun_ptr 

    (*fun_ptr)(10); 

  

    return 0; 
}

// So it's not going to be first class supported, it will be a pointer like everything else in C.


#include <stdio.h> 
// A normal function with an int parameter 
// and void return type 

void fun(int a) 
{ 
    printf("Value of a is %d\n", a);
}
