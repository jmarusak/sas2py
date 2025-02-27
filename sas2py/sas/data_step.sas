data cars_new;
    set sashelp.cars;
    where Origin="Europe";
    KmH_Highway=MPG_Highway*1.609344;
    KmH_City=MPG_City*1.609344;
    KmH_Average=mean(KmH_Highway, KmH_City);
    format KmH: 4.1;
    keep Make Model Type KmH:;
run;
