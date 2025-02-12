use project1;
create table properties1
(
Nam char(100),
Address1 char(100),
Area1 char(100),
Type1 Char(100),
Price1 char(100),
Contact1 integer(100),
pict1 varchar(100)
);
insert into properties1 values
("VOCO DOHA","West Bay","872","Bedroom:1 , Bathroom:1","13500","44955000",'image1.jpeg');
insert into properties1 values
("FLORESTA GARDENS","The Pearl","4811","Bedroom:7 , Bathroom:7","26000","44627829",'image2.jpeg');
insert into properties1 values
("LES ROSES 3","Al Waab","3961","Bedroom:6 , Bathroom:6","18857","44627904",'image3.jpeg');
insert into properties1 values
("LES ROSES COMPOUND 1","Al Waab","3401","Bedroom:5 , Bathroom:6","15000","44627904",'image4.jpeg');
insert into properties1 values
("GIARDINO APARTMENTS","The Pearl","872","Bedroom:1 , Bathroom:2","10000","44627946",'image5.jpeg');
insert into properties1 values
("AL DANA VILLA","Al Sadd","4424","Bedroom:3 , Bathroom:3","18000","44627878",'image6.jpeg');
insert into properties1 values
("EAST PORTO VILLA","The Pearl","3552","Bedroom:3 , Bathroom:4","17000","44627878",'image7.jpeg');
insert into properties1 values
("AL SADD VILLA","Al Sadd","753","Bedroom:1 , Bathroom:1","11000","44627879",'image8.jpeg');
insert into properties1 values
("VIVA BAHRIYA VILLA","The Pearl","2690","Bedroom:4 , Bathroom:3","21000","30500770",'image9.jpeg');
insert into properties1 values
("PORTO ARABIA","The Pearl","2822","Bedroom:3 , Bathroom:4","40000","77886900",'image10.jpeg');
insert into properties1 values
("WATERFRONT","Lusail","1528","Bedroom:2 , Bathroom:2","50000","77551977",'image11.jpeg');
insert into properties1 values
("QANAT QUARTIER","The Pearl","1367","Bedroom:2 , Bathroom:3","47000","31319601",'image12.jpeg');
insert into properties1 values
("STANDALONE VILLA ","West Bay","12916","Bedroom:10 , Bathroom:8","70000","77987797",'image13.jpeg');
insert into properties1 values
("AL ERKYAH","Lusail ","914","Bedroom:1 , Bathroom:2","27000","77551977",'image14.jpeg');
insert into properties1 values
("AL SADD VILLA 2","Al Sadd","9364","Bedroom:6 , Bathroom:6","90000","30074740",'image15.jpeg');
insert into properties1 values
("FOX HILLS APARTMENT","Lusail","1463","Bedroom:2 , Bathroom:2","32000","77551977",'image16.jpeg');
insert into properties1 values
("LEJBAILAT VILLA ","Al Sadd","8072","Bedroom:7 , Bathroom:9","40000","30074740",'image17.jpeg');
insert into properties1 values
("WEST BAY LAGOON VILLA","West bay","4628","Bedroom:5 , Bathroom:5","23000","30500770",'image18.jpeg');
insert into properties1 values
("PORTO ARABIA PENTHOUSE","The Pearl","9579","Bedroom:6 , Bathroom:5","100000","30451451",'image19.jpeg');
insert into properties1 values
("THE PEARL PENTHOUSE","The Pearl","3573","Bedroom:5 , Bathroom:5","163000","31319601",'image20.jpeg');
select*from properties1;


drop table properties1;