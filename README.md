# Vision_based_LabyrinthGame

연세대학교 로봇동아리 로보인 프로젝트: Labyrinth Game using Vision and RL

### Protocol Prototype

![crc](https://user-images.githubusercontent.com/68832065/224462272-75dc1f4a-ed3d-4447-bb47-38aac84fa0fb.JPG)

### Jetson Config
- ubuntu 기초 setting

```shell
sudo apt update
sudo apt upgrade
sudo apt install i2ctools
```

- I2C 접근 허가

```shell
sudo usermod -aG i2c <username>
groupadd -f -r gpio
sudo usermod -a -G gpio <username>
```

- 아두이노 포트 접근 허가

```shell
dmesg | grep tty
sudo chmod a+rw /dev/ttyACM0
```

- Docker 사용하는 경우

이미지 빌드
```shell
docker build -t myimage .
```

i2c 활성화하면서 컨테이너 실행
```shell
docker run --privileged myimage
```

---
# Contributors

[Seoyeon Choi](https://github.com/n00Nspr1ng), [Minjun Chang](https://github.com/wkdalswns0427), [Namhoon Kim](https://github.com/etoilekim), [Seunghyun Roh](https://github.com/seunghyun1130), [Jiyoung Chae](https://github.com/zzero1224)
![image](https://user-images.githubusercontent.com/97090402/222885665-9824e687-1dd2-46f7-aefa-0ac921711ab8.png)
