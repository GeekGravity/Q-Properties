use project1;
create table accounts
(
 UserID char(100) not null,
 Pass char(100) not null
);
insert into accounts values
("1","2"),
("hisham","alen");
select * from accounts;
drop table accounts;