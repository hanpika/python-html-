def find(self,name):
    for s in self:
        if s[0] == name:
            return s[1];

#示例.hpknb

a=""
txt=[]
yf = []
file_name = "语法库_勿动.nb"
with open(file_name) as file_object:
    for line in file_object:
        line = line.strip('\n')
        yf.append(line.split(":"))
        
file_name = input("请输入此后缀的文件.hpknb  >>")
with open(file_name) as file_object:
    for line in file_object:
        txt.append(line.strip('\n'))

html=[]
head=[]
for yg in txt:
    x = yg.split()
    s = find(yf,x[0])
    s = s.split("TextTx")
    s.insert(1,x[1])
    html.append(a.join(s))

def fz():#激动人心的封装环节，好耶，终于写到这了!
    h = "<!DOCTYPE html><html lang='zh'><head><meta charset='UTF-8'>TextTx</head><body>TextTx</body></html>"#便于你修改底层模板
    ha = h.split("TextTx")
    num = 2
    for i in html:
        ha.insert(num,i)
        num = num+1
    
    f = open("封装完成.html", "w", encoding='utf-8')
    f.write(a.join(ha))
    f.close()
    
def xunwen():
    if(input("可进行编译，确定执行吗?(yes or no)")=="yes"):
        fz()
    else:
        print("或许你还没准备好,我们会多给你一些时间思考的")
        xunwen()
        
xunwen()