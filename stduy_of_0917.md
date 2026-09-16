# 09.19 스터디

## AIR(HV 릴레이) 및 관련 규정

![alt text](image.png)

* Kilovac EV200 AIR

---
기본적으로 배터리 팩과 구동 시스템 사이의 절연을 담당 (대형 릴레이)

Aux 리드 동작 방식에 따라 NO 및 NC 타입이 있음

코일을 이용해서 작동

---

관련 규정

SDC가 열리거나 중단된 경우 AIR가 개방되어야 함.

![alt text](image-1.png)

* 인터락 배선

![alt text](image-2.png)

* SDC 회로

SDC는 인터락, 비상정지버튼, IMD, BSPD 등 안전장치들이 직렬로 연결된 회로임.
이 회로는 전원이 없으면 기본적으로 열려서(NO) AIR 코일에 전류가 흐르지 않음.

AIR은 축전지 박스에 두 개 이상 장착되어야 함

AIR 및 초기 충전 릴레이는 기구적인 상태를 감지해야 함. 릴레이 제어신호를 이용할 수 없음. (Aux 리드를 사용하면 될 듯)

AIR 닫힌 상태에서 구동계 전압 60V DC 이상이면 적색 LED 점등

## Pre-Charge Circuit 및 관련 규정

![alt text](image-3.png)
돌입 전류