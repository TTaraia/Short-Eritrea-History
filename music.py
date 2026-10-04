"""Synthesises 15 s of calm classical-style piano (Pachelbel's Canon progression, public domain composition).
Put your own music.mp3 in the repo to override this."""
import math, wave, array

SR = 22050
CHORDS = [  # (bass midi, [chord tones midi])
    (50, [62, 66, 69, 74]), (45, [61, 64, 69, 73]), (47, [62, 66, 71, 74]), (42, [61, 66, 69, 73]),
    (43, [62, 67, 71, 74]), (50, [62, 66, 69, 74]), (43, [62, 67, 71, 74]), (45, [61, 64, 69, 73])]
PATTERN = [0, 1, 2, 3, 2, 1, 2, 1]

def f(m): return 440.0 * 2 ** ((m - 69) / 12)

def add(buf, start, freq, dur, amp, tau):
    n0 = int(start * SR)
    for i in range(int(dur * SR)):
        j = n0 + i
        if j >= len(buf): break
        t = i / SR
        env = min(1.0, t / 0.005) * math.exp(-t / tau)
        w = math.sin(2*math.pi*freq*t) + 0.45*math.sin(4*math.pi*freq*t) + 0.2*math.sin(6*math.pi*freq*t)
        buf[j] += amp * env * w

def make_music(path, seconds=15.0):
    buf = [0.0] * int(seconds * SR)
    step = seconds / (len(CHORDS) * 8)
    for c, (bass, tones) in enumerate(CHORDS):
        for k, idx in enumerate(PATTERN):
            t0 = (c * 8 + k) * step
            add(buf, t0, f(tones[idx]), 1.4, 0.16, 0.45)
            if k in (0, 4): add(buf, t0, f(bass), 2.0, 0.22, 0.9)
    n = len(buf)
    fi, fo = int(0.6 * SR), int(2.5 * SR)
    out = array.array("h")
    for i, v in enumerate(buf):
        g = min(1.0, i / fi) * min(1.0, (n - i) / fo)
        out.append(int(max(-1, min(1, v * g * 0.8)) * 32767))
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(out.tobytes())
