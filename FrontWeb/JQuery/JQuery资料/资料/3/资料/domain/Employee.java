package com.itheima.domain;

public class Employee {
       private int eid;
       private String ename;
       private String sex;
       private String tel;
       private String email;
       private String address;
       private int did;   // 即便是数据库没有 可以在pojo中添加
       private String photo;

    public Employee() {
    }

    public Employee(int eid, String ename, String sex, String tel, String email, String address, int did, String dname, String photo) {
        this.eid = eid;
        this.ename = ename;
        this.sex = sex;
        this.tel = tel;
        this.email = email;
        this.address = address;
        this.did = did;
        this.photo = photo;
    }

    public int getEid() {
        return eid;
    }

    public void setEid(int eid) {
        this.eid = eid;
    }

    public String getEname() {
        return ename;
    }

    public void setEname(String ename) {
        this.ename = ename;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public String getTel() {
        return tel;
    }

    public void setTel(String tel) {
        this.tel = tel;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public int getDid() {
        return did;
    }

    public void setDid(int did) {
        this.did = did;
    }


    public String getPhoto() {
        return photo;
    }

    public void setPhoto(String photo) {
        this.photo = photo;
    }

    @Override
    public String toString() {
        return "Employee{" +
                "eid=" + eid +
                ", ename='" + ename + '\'' +
                ", sex='" + sex + '\'' +
                ", tel='" + tel + '\'' +
                ", email='" + email + '\'' +
                ", address='" + address + '\'' +
                ", did=" + did +
                ", photo='" + photo + '\'' +
                '}';
    }
}
