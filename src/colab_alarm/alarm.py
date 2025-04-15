from IPython.display import Audio, display
import numpy as np

def create_alarm(duration=1, freq=440, sampling_rate=44100):
    """
    Generate and play a simple alarm sound in Google Colab.
    
    Parameters:
    -----------
    duration : float
        Duration of the sound in seconds
    freq : int
        Frequency of the sound in Hz
    sampling_rate : int
        Audio sampling rate
        
    Returns:
    --------
    IPython.display.Audio
        Audio object that will play when displayed
    """
    t = np.linspace(0, duration, int(sampling_rate * duration), False)
    tone = np.sin(2 * np.pi * freq * t)
    return Audio(tone, rate=sampling_rate, autoplay=True)

def alarm(duration=1, freq=880):
    """
    Play an alarm sound immediately.
    
    A convenience function that creates and displays the alarm.
    
    Parameters:
    -----------
    duration : float
        Duration of the sound in seconds
    freq : int
        Frequency of the sound in Hz
    """
    display(create_alarm(duration=duration, freq=freq))