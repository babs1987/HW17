def make_readable(seconds):
    HH=seconds//3600
    MM=seconds%3600//60
    SS=seconds-((MM*60)+(HH*3600))
    return f"{HH:02d}:{MM:02d}:{SS:02d}"
print(make_readable(4))
