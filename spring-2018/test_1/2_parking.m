clc
clear


lot = input('');

if lot == 1
    weeks = input('');
    days = input('');
    hours = input('');

    hour_cost = 2 + ceil((hours-1)*1);

    if hour_cost >9
        hour_cost = 9;
    end

    day_cost = days *9;

    if day_cost>60
        day_cost = 60;
    end

    total = weeks*60 + day_cost + hour_cost;
else
    days = input('');
    hours = input('');
    minutes = input('');

    day_cost = days*32;
    minutes = hours*60+minutes;

    minute_cost = 2 + (ceil((minutes-30)/20)*1);

    if minute_cost<2
        minute_cost=2;
    elseif minute_cost>32
        minute_cost = 32;
    else
        minute_cost = minute_cost;
    end

    total = day_cost+minute_cost;
end

fprintf('%d', total);
