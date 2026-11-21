import json,os,urllib.request as r
VL=[0,100,320,330,500,900,0];I=10**9
PM=['FFFFFKKFFKPKFPZPKU_UPZdZdnxnFFFF','(2<<2<FF<FUPAPZUFU_ZAPZU7FPK(2<<','FFKPFKPPFKPPFKPPFKPPFKPPPUZZFFFK']
MG=[[0]*128 for _ in[0]*13]
for t in range(5):
 Q=PM[(t+1)>>1];J=VL[t+1]
 for q in range(128):
  f=q&7;w=q>>4;x=min(f,7-f);i=w*4+x;MG[t+7][q]=ord(Q[i])-70+J;MG[5-t][q]=70-ord(Q[28-i+2*x])-J
B=[0]*128;s=1;c=0;e=-1;K=[0,0];CR={0:2,7:1,112:8,119:4};HS=set();KL=[0]*256;TT=[0]*65536
KN=(-33,-31,-18,-14,14,18,31,33);BI=(-17,-15,15,17);RO=(-16,-1,1,16);DS=(KN,BI,RO,BI+RO,BI+RO)
def N(q):return chr(97+(q&7))+str(q//16+1)
def F(t):
 global B,s,c,e,K;B=[0]*128;p=t.split();q=112
 for ch in p[0]:
  if ch=="/":q-=24
  elif ch.isdigit():q+=int(ch)
  else:
   d=" PNBRQK".index(ch.upper())*(1-2*(ch>"Z"))
   B[q]=d
   if abs(d)==6:K[d<0]=q
   q+=1
 s=1-2*(p[1]=="b");c=sum(1<<"KQkq".find(ch)for ch in p[2]if ch!="-")
 e=p[3]!="-"and(int(p[3][1])-1)*16+ord(p[3][0])-97 or-1
def A(q,y):
 for d in(15,17):
  t=q-d*y
  if t&136<1 and B[t]==y:return 1
 for d in KN+BI+RO:
  t=q+d
  if t&136<1 and B[t]==(2+4*(d in DS[4]))*y:return 1
 for d in DS[3]:
  t=q+d
  while t&136<1 and not B[t]:t+=d
  if t&136<1 and(B[t]==5*y or B[t]==(3+(d*d in(1,256)))*y):return 1
 return 0
def G(o=0):
 m=[]
 def ap(q,w):
  if w<8 or w>111:m.extend(q|w<<7|v<<14 for v in(5,4,3,2))
  else:m.append(q|w<<7)
 for q in range(128):
  p=B[q]
  if p*s<=0:continue
  t=abs(p)
  if t==1:
   d=16*s;w=q+d
   if not(o or B[w]):
    ap(q,w)
    if(q>>4)==1+5*(s<0)and not B[q+2*d]:m.append(q|q+2*d<<7)
   for k in(d-1,d+1):
    t2=q+k
    if t2&136:continue
    v=B[t2]
    if v*s<0:ap(q,t2)
    elif t2==e:m.append(q|t2<<7)
  else:
   for d in DS[t-2]:
    t2=q+d
    while t2&136<1:
     v=B[t2]
     if v*s<0 or not(v or o):m.append(q|t2<<7)
     if v or t%4==2:break
     t2+=d
 if not o:
  for a,b,i in((4,6,1),(4,2,2),(116,118,4),(116,114,8)):
   d=(b-a)//2
   if c&i and not(B[a+d]or B[b])and not any(A(x,-s)for x in(a,a+d,b))and(d>0 or not B[b+d])and B[b+1-3*(b<a)]==4*s:m.append(a|b<<7)
 return m
def C(x,z):B[z]=B[x];B[x]=0
def D(m):
 global s,c,e;a=m&127;b=m>>7&127;v=m>>14&7;p=B[a];k=B[b];j=b
 if abs(p)==1 and b==e and not k:j=b-16*s;k=B[j];B[j]=0
 B[b]=v*s or p;B[a]=0;u=(m,k,j,c,e)
 if abs(p)==6:
  K[s<0]=b
  if abs(b-a)==2:C(b+1-3*(b<a),b-1+2*(b<a))
  c&=3+9*(s>0)
 c&=~CR.get(a,0)&~CR.get(b,0)
 e=(a+b)//2 if abs(p)==1 and abs(b-a)==32 else-1;s=-s
 if A(K[s>0],s):U(u);return 0
 return u
def U(u):
 global s,c,e;m,k,j,c0,e0=u;a=m&127;b=m>>7&127;v=m>>14&7;s=-s;c=c0;e=e0;p=B[b]
 B[a]=s if v else p;B[b]=0
 if abs(p)==6:
  K[s<0]=a
  if abs(b-a)==2:C(b-1+2*(b<a),b+1-3*(b<a))
 B[j]=k
def u(m):
 t=N(m&127)+N(m>>7&127);v=(m>>14)&7
 return t+" nbrq"[v-1:v]
def V():return sum(MG[p+6][q]for q,p in enumerate(B)if p)*s
def O(m,y):return sorted(m,key=lambda x:(t:=B[x>>7&127])and 10*VL[abs(t)]-VL[abs(B[x&127])]or 50*(x==KL[y]),reverse=True)
def S(a,b,d,y):
 global n,BM;n+=1
 if n>2e5:raise Exception
 if d<=0:
  a=max(a,V())
  if a>=b:return b
  i=A(K[s<0],-s)
  for m in O(G(not i),y):
   u2=D(m)
   if not u2:continue
   a=max(a,-S(-b,-a,0,y+1));U(u2)
   if a>=b:return b
  return a
 tB=tuple(B);k=hash(tB)&65535
 if y and tB in HS:return 0
 KL[y]=TT[k]or KL[y]
 i=A(K[s<0],-s);m=O(G(),y);o=-I;p=0;g=a
 for z,mm in enumerate(m):
  u2=D(mm)
  if not u2:continue
  t2=-S(-b if not z else -g-1,-g,d-1,y+1)
  if z and g<t2<b:t2=-S(-b,-g,d-1,y+1)
  if t2>o:o=t2;p=mm
  U(u2);g=max(g,t2)
  if g>=b:KL[y]=mm;break
 if y==0:BM=p
 TT[k]=p
 return(-10**5+y if i else 0)if o==-I else o
def W(t):
 global n,BM;n=0;BM=0;F(t);HS.add(tuple(B))
 ms=[x for x in G()if(z:=D(x))and not U(z)]
 o=ms[0];d=1
 if ms[1:]:
  while 1:
   try:S(-I,I,d,0);o=BM
   except Exception:break
   d+=1
 F(t);D(o);HS.add(tuple(B))
 return o
def P(p,b):return json.load(r.urlopen(url+p,json.dumps(b).encode()))
url=os.environ["MAKEFUN_ENV_URL"];h=0
while(g:=P("/game",{}))["status"]!="done":
 if g["game"]!=h:HS.clear();h=g["game"]
 while g["status"]=="your_move":
  mv=u(W(g["fen"]))
  g=P("/move",{"game":g["game"],"move":mv if mv in g["legal_moves"]else g["legal_moves"][0]})
