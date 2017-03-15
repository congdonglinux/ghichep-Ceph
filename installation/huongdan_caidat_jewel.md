# Hướng dẫn cài đặt CEPH JEWEL trên Ubuntu 14.04
Mục lục:

[1. Mô hình Lab](#1)

[2. Cấu hình Node-I (Mon+Osd+Mds)](#2)

[3. Cấu hình Note-II (Osd)](#3)

[4. Cấu hình Node-III (Mon+Osd)](#4)
========================

<a name="1"></a>
### Mô hình và các yêu cầu về OS

- Mô hình

![CEPH JEWEL](../images/mohinh-ceph-jewel.png)

- Cấu hình các máy

```sh
- OS: Ubuntu Server 14.04 64bit
- RAM: thấp nhất 04 GB
- Máy có 03 NICs: 
-- eth0: sử dụng để quản trị các máy chủ CEPH (dùng chế độ hostonly -vmnet10 của Vmware workstation)
-- eth1: sử dụng để tải gói cài đặt từ internet (dụng NAT hoặc Bridge của Vmware workstation)
-- eth2: sử dụng để cho các máy chủ CEPH Replicate dữ liệu (dùng chế độ hostonly - vmnet12- của Vmware workstation)

- Sử dụng 05 ổ cứng
-- HDD1: Cài OS Ubuntu Server 14.04 64bit
-- HDD2 đến HDD5: Cung cấp các OSD cho CEPH.
```

Chú ý: Số Node (Mon+Osd) nên cấu hình là 3 node để số lượng Object đc replicate đúng. Có thể cấu hình 1 node, dùng bình thường nhưng check ceph status sẽ báo pgs degrate.

**THỰC HIỆN TRÊN CÁC SERVER CEPH**