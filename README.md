# 🐍 Snake.io — Multi-Round Snake Game

A feature-rich, arcade-style **Snake Game** built with **Python & Pygame**, enhanced with a **scoring system**, **multiple food types**, and **progressive difficulty** through rounds.

---

## 🎮 Game Features

- ✅ Smooth snake controls with **WASD** and **Arrow keys**
- 🍎 **Round-based gameplay** with different foods, goals, and time limits:
  - **Round 1** – Apple (5 pts) — Goal: 300 — Time: 5 min
  - **Round 2** – Banana (10 pts) — Goal: 750 — Time: 3 min
  - **Final Round** – Pizza (30 pts) — Goal: 1500 — Time: 2 min 15 sec
- 🔄 Score resets to 0 if you die — **restart from Round 1**
- 🕐 Countdown timer per round
- 🧊 Transition screens between rounds
- ❌ Game Over screen & 🎉 Victory screen
- 🎯 Snake auto-grows with food — balanced for late rounds
- 🖼️ Custom food sprites (Apple, Banana, Pizza)

---

## 🖼️ Gameplay Preview
> 💡watch the [gameplay video](media/gameplay.mp4) if you're viewing this on GitHub.

---

## 🚀 How to Run

### 🔧 Requirements:
- Python 3.x
- Pygame

### 🛠️ Install Pygame:
```bash
pip install pygame



Make sure you have the following folder structure:
Snake-Game/
│
├── assets/
│   ├── apple.png
│   ├── banana.png
│   └── pizza.png
│
├── screens.py
├── Python_Game.py
└── README.md
