import re
line = "Jedno zdanie, drugie zdanie, trzecie; ups - nie chcialem tego robic. Ahoj!"


chunks = re.split(r'[,\s\-;.]\s*', line)

print(chunks)
