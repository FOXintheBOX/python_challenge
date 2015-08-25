import png, numpy as np

image = png.Reader('oxygen.png')

data = image.read()
lines = data[2]

message = [chr(x) for x in np.array(lines[43])]

msg_filt1 = [x for i,x in enumerate(message) if (i-1) % 4 ==0]
msg_filt2 = [x for i,x in enumerate(msg_filt1) if i % 7 ==0]
print ''.join(msg_filt2)

next = [105, 110, 116, 101, 103, 114, 105, 116, 121]

out_str = "".join([chr(x) for i, x in enumerate(next)])
print out_str
