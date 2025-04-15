# Colab Alarm

**Colab Alarm** is a lightweight audio notification system designed specifically for Google Colab. It helps you stay productive by alerting you when long-running code cells finish execution.

---

## Why Use Colab Alarm?

- **Stay Productive**: Work on other tabs or tasks while your code runs.
- **Audio Alerts**: Get an immediate sound notification when your cell completes.
- **Easy Integration**: Just add a single line of code at the end of any cell.
- **Fully Customizable**: Adjust duration and frequency to suit your preferences.

---

## Installation, Usage & Customization

```python
# 1. Install the package (run this once)
!pip install colab-alarm

# 2. Import the alarm function
from colab_alarm.alarm import alarm

# 3. Use it at the end of any long-running cell
alarm()  # Plays a default beep (1 second at 440 Hz)

# Optional: Customize the sound
# Play a 3-second tone at 440 Hz (standard A4 pitch)
alarm(duration=3, freq=440)

# Play a 0.5-second tone at 1000 Hz (higher pitch, quicker beep)
alarm(duration=0.5, freq=1000)
