#1. create table student(Roll_No INT,Name VARCHAR(16),Course VARCHAR(16));

#2. insert into student values(4,'Anjali Mishra','BOOTCAMP'),(5,'Satish Kushwaha','WEB'),(6,'imran','FULL STACK'),(6,'Naziya Begum','PYTHON');

#3. select * from student;

#4. update student set name='XYZ' where roll_no = 3;

#5. delete from student where roll_no=3;

#6. delete from student;

#7. drop table student;

"""8.     create table student(rollno int primary key,name VARCHAR(16),cid int,constraint fk_cid foreign key(cid)      
          references courses(cid));"""

"""9. insert into student values(4,'Aman',2);
      insert into courses values(6,'Video Editing')"""

#10. select * from student where cid = (select cid from courses where cname='C++'); 