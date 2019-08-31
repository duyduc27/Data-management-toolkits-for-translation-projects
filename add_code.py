import time
from langdetect import detect

para = "Trong một vụ việc riêng rẽ, Andy Chan, người đứng đầu đảng đòi độc lập đã bị bắt tại sân bay quốc tế Hong Kong, Guardian dẫn lại Hong Kong Free Press. Chan nói rằng anh bị giữ lại khi sắp đáp máy bay đến Nhật. Chan bị cáo buộc bạo động và tấn công một cảnh sát."

def add_code(maxlen, text):
    "Add code for a sentence"
    n = text[:maxlen].rfind(' ') # find index of the last space character
    lis = list(text)
    lis[n] = "<line>\n"
    line_code = 1
    while len(text[n:]) > maxlen:
        if line_code < 1:
            m = text[n: n+ maxlen].rfind(' ')
            n += m
            lis[n] = "<line>\n"
            line_code +=1
        else:
            m = text[n: n+maxlen].rfind(' ')
            n += m
            lis[n] = "<new>\n"
            line_code = 0
    txt = "".join(lis)            
    return txt

## test
#print(add_code(26, para))

t0 = time.perf_counter()
input_file = open("Yu-Gi-Oh! The Sacred Cards.txt", "r", encoding="utf8")
output_file = open("output.txt", "w", encoding="utf8")
maxlen = 26

while True:
    theline = input_file.readline() # read a line each time
    if len(theline) == 0: # we read all the lines of the input text
        break
    else:
        if len(theline) > maxlen:
            try:
                if detect(theline) == "vi":
                    processed_line= add_code(maxlen, theline)
                    output_file.write(processed_line)
                else:
                    output_file.write(theline)
            except:
                #print("This line couldn't handle: \n", theline) # print log
                pass
        else:
            output_file.write(theline)
    

input_file.close()
output_file.close()
t1 = time.perf_counter()
print("Time elapsed: {}".format(t1-t0 ))