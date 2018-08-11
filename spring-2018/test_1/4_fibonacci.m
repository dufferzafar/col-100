clc
clear

function is =isPerfectSquare(x)
    s = fix(sqrt(x));
    is= (s*s == x);
end

function s=isFibonacci(n)
    s=isPerfectSquare(5*n*n + 4) || isPerfectSquare(5*n*n - 4);
end

% for i=1:1000
%     fibotest=isFibonacci(i);

n=input('')
fibotest=isFibonacci(n);

if (fibotest==1)
    fprintf('Yes');
else
    fprintf('No');
end
