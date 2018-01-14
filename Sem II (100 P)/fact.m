n = input('');

res = 1;
while( factorial(res) <= n )
    res = res + 1;
end

disp(factorial(res))
