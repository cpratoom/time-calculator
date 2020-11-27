def add_time(start, duration, startday=None):
    one, two = start.split(":")

    g1 = "{}:{}".format(one[:2],two[:2])
    g2 = two[-2:]
    
    # convert tin to 24HR format
    pm = (1 if "pm" in start.lower() else 0)
    
    one, two = g1.split(':')
    tin = {"hh": int(one) + 12*pm, "mm": int(two)}
    
    # duration
    one, two = duration.split(':')
    dt = {"hh": int(one), "mm": int(two)} 
    
    # rounding up tout=tin+dt xtra mins to the hour, and xtra hours to the day
    xhours, mins = divmod(tin["mm"]+dt["mm"], 60)
    xdays, hours = divmod(tin["hh"]+dt["hh"]+xhours, 24)

    # format tout in 12HR format + day
    apidx, hh12 = divmod(hours, 12)
    ap = ["AM", "PM"]
    dayofweek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    #reformatting midnight from 00:mm --> 12:mm
    term1 = (str(12) if hh12==0 else str(hh12) )
    term2 = str(mins).rjust(2, '0')
    term3 = ap[apidx]
    
    if startday == None:
        if xdays==0:
            new_time = "{}:{} {}".format(term1, term2, term3)
        else:
            xdays_label = ("(next day)" if xdays==1 else "({} days later)".format(xdays))
            new_time = "{}:{} {} {}".format(term1, term2, term3, xdays_label)
    else:
        a, idxw = divmod(dayofweek.index(startday.lower())+xdays, 7)
        term4 = dayofweek[idxw].capitalize()
        
        if xdays==0:
            new_time = "{}:{} {}, {}".format(term1, term2, term3, term4)
        else:
            xdays_label = ("(next day)" if xdays==1 else "({} days later)".format(xdays))            
            new_time = "{}:{} {}, {} {}".format(term1, term2, term3, term4, xdays_label)

    return new_time