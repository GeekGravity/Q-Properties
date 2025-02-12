create database project1;
use project1;


create table properties
(
Nam char(100),
Address char(100),
Area char(100),
Type0 Char(100),
Price char(100),
Contact integer(100),
pict varchar(100)
);
insert into properties values
("VOCO DOHA","Doha,West Bay,ZigZag Tower","872 sq.ft","Bed:1 , Bath:1","13,500QAR/mo","44955000",'image1.jpeg');
insert into properties values
("FLORESTA GARDENS","Doha,The Pearl,Floresta Gardens","4,811sq.ft","Bed:7 , Bath:7","26,000QAR/mo","44627829",'image2.jpeg');
insert into properties values
("LES ROSES 3","Doha,Al Waab,Les Roses Compound","3,961 sq.ft","Bed:6 , Bath:6","18,857QAR/mo","44627904",'image3.jpeg');
insert into properties values
("LES ROSES COMPOUND 1","Doha,Al Waab,Les Roses Compound","3,401sq.ft","Bed:5 , Bath:6","15,000QAR/mo","44627904",'image4.jpeg');
insert into properties values
("GIARDINO APARTMENTS","Doha,The Pearl,Medina Centrale","872 sq.ft","Bed:1 , Bath:2","10,000QAR/mo","44627946",'image5.jpeg');
insert into properties values
("AL DANA VILLA","Doha,Al Sadd,Al Muraikh","4,424 sq.ft","Bed:3 , Bath:3","18,000QAR/mo","44627878",'image6.jpeg');
insert into properties values
("EAST PORTO VILLA","Doha,The Pearl,Porto Arabia","3,552 sq.ft","Bed:3 , Bath:4","17,000QAR/mo","44627878",'image7.jpeg');
insert into properties values
("AL SADD VILLA","Doha,Al Sadd,C-ring road","753 sq.ft","Bed:1 , Bath:1","11,000QAR/mo","44627879",'image8.jpeg');
insert into properties values
("VIVA BAHRIYA VILLA","Doha,The Pearl,Viva Bahriya ","2,690 sq.ft","Bed:4 , Bath:3","21,000QAR/mo","30500770",'image9.jpeg');
insert into properties values
("PORTO ARABIA","Doha,The Pearl,Medina Centrale","2,822 sq.ft","Bed:3 , Bath:4","40,000QAR/mo'","77886900",'image10.jpeg');
insert into properties values
("WATERFRONT","Doha,Lusail city,Waterfront District","1,528 sq.ft","Bed:2 , Bath:2","50000QAR/mo","77551977",'image11.jpeg');
insert into properties values
("QANAT QUARTIER","Doha,The Pearl,Qanat Quartier ","1,367 sq.ft","Bed:2 , Bath:3","47,000QAR/mo","31319601",'image12.jpeg');
insert into properties values
("STANDALONE VILLA ","Doha,West Bay,Standalone Villa","12,916 sq.ft","Bed:10 , Bath:8","70,000QAR/mo","77987797",'image13.jpeg');
insert into properties values
("AL ERKYAH","Doha,Lusail City,Al Erkyah ","914 sq.ft","Bed:1 , Bath:2","27,000QAR/mo","77551977",'image14.jpeg');
insert into properties values
("AL SADD VILLA 2","Doha,Al Sadd,Al Sadd road","9,364 sq.ft","Bed:6 , Bath:6","90,000QAR/mo","30074740",'image15.jpeg');
insert into properties values
("FOX HILLS APARTMENT","Doha,Lusail,Fox Hills","1,463 sq.ft","Bed:2 , Bath:2","32,000QAR/mo","77551977",'image16.jpeg');
insert into properties values
("LEJBAILAT VILLA ","Doha,Al Sadd,Lejbailat","8,072 sq.ft","Bed:7 , Bath:9","40,000QAR/mo","30074740",'image17.jpeg');
insert into properties values
("WEST BAY LAGOON VILLA","Doha,West bay,Legtaifiya","4,628 sq.ft","Bed:5 , Bath:5","23,000QAR/mo","30500770",'image18.jpeg');
insert into properties values
("PORTO ARABIA PENTHOUSE","Doha,The Pearl,Porto Arabia","9,579 sq.ft","Bed:6 , Bath:5","100,000QAR/mo","30451451",'image19.jpeg');
insert into properties values
("THE PEARL PENTHOUSE","Doha,The Pearl,Qanat Quartier","3,573 sq.ft","Bed:5 , Bath:5","163,000QAR/mo","31319601",'image20.jpeg');
select*from properties;





drop table properties;

