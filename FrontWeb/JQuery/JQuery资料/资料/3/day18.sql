CREATE DATABASE day18;
USE day18;

#部门表  did  dname
CREATE TABLE dept(
	did INT PRIMARY KEY ,
	dname VARCHAR(30)
);

INSERT INTO dept VALUES(1,'总裁办');
INSERT INTO dept VALUES(2,'研发部');
INSERT INTO dept VALUES(3,'财务部');

#员工表  eid  uname  sex   tel  email  address  did(外键)
CREATE TABLE emp (
	eid INT PRIMARY KEY AUTO_INCREMENT,
	ename VARCHAR(20),
	sex VARCHAR(6),
	tel VARCHAR(20),
	email VARCHAR(50),
	address VARCHAR(200),
	did INT   #外键
);

INSERT INTO emp VALUES(NULL , '刘备','男','13812341234','lb@itheima.com','北京',1);
INSERT INTO emp VALUES(NULL , '诸葛亮','男','010-111111','zg@itheima.com','北京',2);
INSERT INTO emp VALUES(NULL , '关羽','男','13800001111','gy@itheima.com','荆州',2);
INSERT INTO emp VALUES(NULL , '曹操','男','15811112222','cc@itheima.com','许昌',1);
INSERT INTO emp VALUES(NULL , '孙尚香','女','010-1234567','ssx@itheima.com','南京',3);
INSERT INTO emp VALUES(NULL , '小乔','女','010-7654321','xq@itheima.com','南京',1);
INSERT INTO emp VALUES(NULL , '貂蝉','女','13511110000','dc@itheima.com','洛阳',3);


#建立外键关联
ALTER TABLE emp ADD FOREIGN KEY (did)  REFERENCES  dept(did);

#全查询:
SELECT e.eid,e.ename,e.sex,e.tel,e.email,e.address,d.dname FROM emp e,dept d WHERE e.did = d.did;

-- 添加的sql语句
INSERT INTO emp VALUES(NULL,?,?,?,?,?,?);

-- 根据eid查询的sql语句
SELECT e.eid,e.ename,e.sex,e.tel,e.email,e.address,e.did FROM emp e WHERE e.eid = 18;

-- 根据的sql语句
UPDATE emp SET ename=?,sex=?,tel=?,email=?,address=?,did=? WHERE eid=?;

UPDATE emp SET ename='大乔',sex='女',tel='11',email='dq@itcast.cn',address='东京',did='2' WHERE eid=15;
