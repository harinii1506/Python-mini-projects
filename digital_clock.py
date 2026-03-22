import tkinter as tk
from time import strftime
from datetime import datetime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("550x400")
root.resizable(False, False)

themes = {
    'Dark': {'bg': '#1a1a2e', 'time': '#00ff88', 'date': '#ffd93d', 'accent': '#00d9ff'},
    'Ocean': {'bg': '#0a192f', 'time': '#64ffda', 'date': '#ccd6f6', 'accent': '#00b4d8'},
    'Sunset': {'bg': '#2d1b69', 'time': '#ff6b9d', 'date': '#feca57', 'accent': '#ff9ff3'},
    'Forest': {'bg': '#1b4332', 'time': '#95d5b2', 'date': '#d8f3dc', 'accent': '#52b788'},
    'Neon': {'bg': '#000000', 'time': '#39ff14', 'date': '#ff10f0', 'accent': '#00ffff'}
}

state = {'theme': 'Dark', '24h': False, 'seconds': True}
widgets = {}

def apply_theme():
    c = themes[state['theme']]
    for w in widgets.values():
        w.config(bg=c['bg'])
    widgets['title'].config(fg=c['accent'])
    widgets['time'].config(fg=c['time'])
    widgets['period'].config(fg=c['accent'])
    widgets['date'].config(fg=c['date'])
    widgets['day'].config(fg='#ffffff')
    for b in [widgets['theme_btn'], widgets['format_btn'], widgets['sec_btn']]:
        b.config(bg=c['accent'], fg=c['bg'])
    widgets['line'].config(bg=c['accent'])

def change_theme():
    t_list = list(themes.keys())
    state['theme'] = t_list[(t_list.index(state['theme']) + 1) % len(t_list)]
    apply_theme()

def toggle_format():
    state['24h'] = not state['24h']
    widgets['format_btn'].config(text='12H' if state['24h'] else '24H')

def toggle_seconds():
    state['seconds'] = not state['seconds']
    widgets['sec_btn'].config(text='Hide Sec' if state['seconds'] else 'Show Sec')

def get_greeting():
    h = datetime.now().hour
    return ['🌅 Good Morning!', '☀️ Good Afternoon!', '🌆 Good Evening!', '🌙 Good Night!'][3 if h >= 21 else 2 if h >= 17 else 1 if h >= 12 else 0]

def update_time():
    fmt = '%H:%M' if state['24h'] else '%I:%M'
    if state['seconds']: fmt += ':%S'
    widgets['time'].config(text=strftime(fmt))
    widgets['period'].config(text='' if state['24h'] else strftime('%p'))
    widgets['date'].config(text=strftime('%B %d, %Y'))
    widgets['day'].config(text=strftime('%A'))
    widgets['time'].after(1000, update_time)

# Create widgets
bg = tk.Frame(root, bg=themes['Dark']['bg'])
bg.pack(fill='both', expand=True)
widgets['bg'] = bg

widgets['title'] = tk.Label(bg, text=get_greeting(), font=('Arial', 16, 'bold'))
widgets['title'].pack(pady=(15, 10))

time_cont = tk.Frame(bg, bg=themes['Dark']['bg'])
time_cont.pack()
widgets['time_cont'] = time_cont

widgets['time'] = tk.Label(time_cont, font=('DS-Digital', 70, 'bold'))
widgets['time'].pack(side='left')

widgets['period'] = tk.Label(time_cont, font=('Arial', 28, 'bold'))
widgets['period'].pack(side='left', padx=(10, 0))

widgets['day'] = tk.Label(bg, font=('Arial', 18, 'bold'))
widgets['day'].pack(pady=(10, 5))

widgets['date'] = tk.Label(bg, font=('Arial', 16))
widgets['date'].pack(pady=(0, 15))

widgets['line'] = tk.Frame(bg, height=3)
widgets['line'].pack(fill='x', padx=50, pady=10)

btn_frame = tk.Frame(bg, bg=themes['Dark']['bg'])
btn_frame.pack(pady=10)
widgets['btn_frame'] = btn_frame

widgets['theme_btn'] = tk.Button(btn_frame, text='Change Theme', font=('Arial', 11, 'bold'), command=change_theme, cursor='hand2', relief='flat', padx=15, pady=8)
widgets['theme_btn'].pack(side='left', padx=5)

widgets['format_btn'] = tk.Button(btn_frame, text='24H', font=('Arial', 11, 'bold'), command=toggle_format, cursor='hand2', relief='flat', padx=15, pady=8)
widgets['format_btn'].pack(side='left', padx=5)

widgets['sec_btn'] = tk.Button(btn_frame, text='Hide Sec', font=('Arial', 11, 'bold'), command=toggle_seconds, cursor='hand2', relief='flat', padx=15, pady=8)
widgets['sec_btn'].pack(side='left', padx=5)

apply_theme()
update_time()
root.mainloop()