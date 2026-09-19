import numpy as np
import matplotlib.pyplot as plt

# 1. 시간 축 데이터 생성 (0초부터 25초까지 0.01초 간격)
t = np.arange(0, 25, 0.01)

# 2. BSPD 원본 입력 신호 정의 (정상 HIGH=1, 이상 감지 LOW=0)
# 초기(0~2초): 정상(1) | 2초~5초: 이상 감지(0) | 5초 이후: 정상 복구(1)
input_signal = np.ones_like(t)
input_signal[(t >= 2) & (t < 5)] = 0

# 3. LTC6994 지연 출력 신호 정의
# HIGH->LOW(2초)는 즉시 반영 | LOW->HIGH(5초)는 10초 지연되어 15초에 반영
output_signal = np.ones_like(t)
output_signal[(t >= 2) & (t < 15)] = 0

# 4. 그래프 그리기 (위/아래 2개의 Subplot 구성)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
fig.suptitle("BSPD vs LTC6994 Signal Timing Diagram", fontsize=14, fontweight='bold')

# --- 위쪽 그래프: BSPD Raw 센서 입력 ---
ax1.plot(t, input_signal, label="BSPD Raw Input", color="tab:blue", linewidth=2.5)
ax1.set_ylabel("Signal State", fontsize=11)
ax1.set_ylim(-0.2, 1.2)
ax1.set_yticks([0, 1])
ax1.set_yticklabels(["LOW (Fault)", "HIGH (Normal)"])
ax1.grid(True, linestyle="--", alpha=0.5)
ax1.legend(loc="upper right")
ax1.set_title("1. Raw Sensor Input (Instant Change)", fontsize=11, loc="left", pad=5)

# 중요 시점 수직선 표시 (이상 발생: 2초, 센서 복구: 5초)
ax1.axvline(x=2, color="crimson", linestyle=":", alpha=0.8)
ax1.axvline(x=5, color="darkorange", linestyle=":", alpha=0.8)
ax1.text(2.2, 0.5, "Fault Occurred (2s)", color="crimson", fontweight="bold")
ax1.text(5.2, 0.5, "Sensor Recovered (5s)", color="darkorange", fontweight="bold")

# --- 아래쪽 그래프: LTC6994 지연 출력 ---
ax2.plot(t, output_signal, label="LTC6994 Delayed Output", color="tab:green", linewidth=2.5)
ax2.set_xlabel("Time (Seconds)", fontsize=11)
ax2.set_ylabel("vSgnl State", fontsize=11)
ax2.set_ylim(-0.2, 1.2)
ax2.set_yticks([0, 1])
ax2.set_yticklabels(["LOW (Shutdown)", "HIGH (Run)"])
ax2.grid(True, linestyle="--", alpha=0.5)
ax2.legend(loc="upper right")
ax2.set_title("2. LTC6994 Output (10s Recovery Delay Applied)", fontsize=11, loc="left", pad=5)

# 중요 시점 및 지연 구간 표시
ax2.axvline(x=2, color="crimson", linestyle=":", alpha=0.8)   # 즉시 차단
ax2.axvline(x=5, color="darkorange", linestyle=":", alpha=0.5) # 센서는 복구되었으나 출력은 대기
ax2.axvline(x=15, color="navy", linestyle="--", alpha=0.8)     # 10초 지연 후 복구
ax2.text(2.2, 0.2, "Immediate\nShutdown", color="crimson", fontweight="bold")

# 10초 지연 구간 화살표 및 음영 표시
ax2.axvspan(5, 15, color="gold", alpha=0.15)
ax2.annotate('', xy=(15, 0.5), xytext=(5, 0.5),
             arrowprops=dict(arrowstyle="<->", color="navy", lw=1.5))
ax2.text(10, 0.55, "10-Second Delay Zone", color="navy", horizontalalignment="center", fontweight="bold")
ax2.text(15.2, 0.2, "Safe Recovery (15s)", color="navy", fontweight="bold")

# 그래프 간격 조절 및 출력
plt.tight_layout()
plt.show()
