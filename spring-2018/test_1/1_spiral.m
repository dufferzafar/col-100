clc
clear

function sum=spiralDiaSum(n)

    if (mod(n,2)==0)
        sum=-1;
    elseif n == 1
        sum=1;
    else
        sum=4*n*n - 6*n + 6 + spiralDiaSum(n-2);
    end
end

n=input('')
sum=spiralDiaSum(n);
fprintf('%d\n',sum);
