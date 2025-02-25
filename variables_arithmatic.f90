!Variable_airthmatic
program Variable_airthmatic
    implicit none
    
    !Declaring variables
    integer :: a, b, sum_int
    real :: x, y, product_real
    complex :: z1, z2, sum_complex
    character(len=20) :: message
    
    !Assign values
    a = 5 
    b = 3
    x = 2.5
    y = 4.0
    z1 = (1.0, 2.0)
    z2 = (3.0, 4.0)
    message = "Hello from Fortran!"

    !Performing arithmetic operations
    sum_int = a + b
    product_real = x * y
    sum_complex = z1 + z2

    !Printing the results
    print *, "Sum of integers: ", sum_int
    print *, "Product of real numbers: ", product_real
    print *, "Sum of complex numbers: ", sum_complex
    print *, message
end program Variable_airthmatic