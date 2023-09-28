package com.itheima.domain;

public class EmpDept {
    private int eid;
    private String ename;
    private String sex;
    private String tel;
    private String email;
    private String address;
    private int did;
    private String dname;

    public EmpDept() {
    }

    public EmpDept(int eid, String ename, String sex, String tel, String email, String address, int did, String dname) {
        this.eid = eid;
        this.ename = ename;
        this.sex = sex;
        this.tel = tel;
        this.email = email;
        this.address = address;
        this.did = did;
        this.dname = dname;
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

    public String getDname() {
        return dname;
    }

    public void setDname(String dname) {
        this.dname = dname;
    }

    @Override
    public String toString() {
        return "EmpDept{" +
                "eid=" + eid +
                ", ename='" + ename + '\'' +
                ", sex='" + sex + '\'' +
                ", tel='" + tel + '\'' +
                ", email='" + email + '\'' +
                ", address='" + address + '\'' +
                ", did=" + did +
                ", dname='" + dname + '\'' +
                '}';
    }
}
