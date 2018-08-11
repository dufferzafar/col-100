clc
clear

function [approx, terms] = approxSine(x, threshold)
    exponent = 3; approx = x; koef = -1; m = 2; terms = 1;
    while abs((sin(x) - approx)) > threshold
        %computes approx until the abs((sin(x) - approx)/sin(x)) is greater
        %than the threshold entered by the user.
        approx = approx + ((koef)^(m+1)) * x^exponent/factorial(exponent);
        exponent = exponent + 2;
        m = m+1;
        terms = terms + 1;
    end
end

x=input('');
[approx, terms] = approxSine(x, 0.00000001);

fprintf('%d\n', terms);
