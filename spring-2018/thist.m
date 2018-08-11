p='TTCGGGAGCCTGGGCGTTACGTTAATGAAAGATGAAATATGTACCAACGACAATGACATTGAAAACTATG';

% Build histogram data
nAA= 4; % Number of amino acids
count= zeros(nAA, 1);
for k= 1:1:length(p)
    % codon= p(k); % length 3 subvector
    % ind= getAAIndex(getMnemonic(codon));
    if (p(k) == 'A')
        ind = 1;
    elseif (p(k) == 'C')
        ind = 2;
    elseif (p(k) == 'T')
        ind = 3;
    elseif (p(k) == 'G')
        ind = 4;
    end

    count(ind)= count(ind) + 1;
end

%   Draw    bar graph
bar(1:nAA, count);
title('Tally of characters in string', 'FontSize', 14);
axis tight;
set(gca,'xTick',1:20);
set(gca,'xTickLabel', {'A', 'C', 'T', 'G'}, 'FontSize',14,'FontWeight','Bold');
shg;
