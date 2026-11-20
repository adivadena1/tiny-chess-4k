import json,os,urllib.request as r
VL=[0,100,320,330,500,900,0];I=10**9
PM=['FFFFFKKFFKPKFPZPKU_UPZdZdnxnFFFF','(2<<2<FF<FUPAPZUFU_ZAPZU7FPK(2<<','FFKPFKPPFKPPFKPPFKPPFKPPPUZZFFFK','Z_PFUZKFFFA<AA<7<<72772-22-(22-(']
MG=[[0]*128 for _ in range(13)]
for t in range(6):
 Q=PM[(t+1)>>1];J=VL[t+1]
 for q in range(128):
  f=q&7;w=q>>4;x=min(f,7-f);i=w*4+x;j=(7-w)*4+x;MG[t+7][q]=ord(Q[i])-70+J;MG[5-t][q]=70-ord(Q[j])-J
B=[0]*128;s=1;c=0;e=-1;K=[0,0];CR={0:2,7:1,112:8,119:4};HS=set();KL=[0]*256
KN=(-33,-31,-18,-14,14,18,31,33);BI=(-17,-15,15,17);RO=(-16,-1,1,16);DS=((),(),KN,BI,RO,BI+RO,BI+RO)
def N(q):return chr(97+(q&7))+str((q>>4)+1)
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
 s=1-2*(p[1]=="b");c=sum(1<<i for i,ch in enumerate("KQkq")if ch in p[2])
 e=int(p[3][1])*16+ord(p[3][0])-113 if p[3]!="-"else-1
def A(q,y):
 for d in(15,17):
  t=q-d*y
  if not t&136 and B[t]==y:return 1
 for d in DS[2]+DS[6]:
  t=q+d
  if not t&136 and B[t]==(2+4*(d in DS[6]))*y:return 1
 for d in DS[5]:
  t=q+d
  while not t&136 and not B[t]:t+=d
  if not t&136 and(B[t]==5*y or B[t]==(3 if abs(d)in(15,17)else 4)*y):return 1
 return 0
def G(o=0):
 m=[]
 def ap(q,w):
  if w>>4 in(0,7):m.extend(q|w<<7|v<<14 for v in(5,4,3,2))
  else:m.append(q|w<<7)
 for q in range(128):
  p=B[q]
  if not p or p*s<0:continue
  t=abs(p)
  if t==1:
   d=16*s;w=q+d
   if not o and not B[w]:
    ap(q,w)
    if(q>>4)==1+5*(s<0)and not B[q+2*d]:m.append(q|(q+2*d)<<7)
   for k in(d-1,d+1):
    t2=q+k
    if t2&136:continue
    v=B[t2]
    if v and v*s<0:ap(q,t2)
    elif t2==e:m.append(q|t2<<7)
  else:
   for d in DS[t]:
    t2=q+d
    while not t2&136:
     v=B[t2]
     if v and v*s<0 or not v and not o:m.append(q|t2<<7)
     if v or t%4==2:break
     t2+=d
 if not o:
  for a,b,i in((4,6,1),(4,2,2),(116,118,4),(116,114,8)):
   d=(b-a)//2
   if c&i and not B[a+d]and not B[b]and not(A(a,-s)or A(a+d,-s)or A(b,-s))and(d>0 or not B[b+d]):m.append(a|b<<7)
 return m
def C(x,z):B[z]=B[x];B[x]=0
def D(m):
 global s,c,e;a=m&127;b=(m>>7)&127;v=(m>>14)&7;p=B[a];k=B[b];j=b
 if abs(p)==1 and b==e and not k:j=b-16*s;k=B[j];B[j]=0
 B[b]=v*s or p;B[a]=0
 if abs(p)==6:
  K[s<0]=b
  if abs(b-a)==2:C(b+1-3*(b<a),b-1+2*(b<a))
 u=(m,k,j,c,e)
 if abs(p)==6:c&=3+9*(s>0)
 for q in(a,b):c&=~CR.get(q,0)
 e=(a+b)//2 if abs(p)==1 and abs(b-a)==32 else-1;s=-s
 if A(K[s>0],s):U(u);return 0
 return u
def U(u):
 global s,c,e;m,k,j,c0,e0=u;a=m&127;b=(m>>7)&127;v=(m>>14)&7;s=-s;c=c0;e=e0;p=B[b]
 B[a]=s if v else p;B[b]=0
 if abs(p)==6:
  K[s<0]=a
  if abs(b-a)==2:C(b-1+2*(b<a),b+1-3*(b<a))
 if k:B[j]=k
def u(m):
 t=N(m&127)+N((m>>7)&127);v=(m>>14)&7
 return t+" nbrq"[v-1:v]
def V():return sum(MG[B[q]+6][q]for q in range(128)if B[q])*s
class T(Exception):pass
def O(m,y):return sorted(m,key=lambda x:(t:=B[(x>>7)&127])and 10*VL[abs(t)]-VL[abs(B[x&127])]or 50*(x==KL[y]),reverse=True)
def S(a,b,d,y):
 global n,BM;n+=1
 if n>2e5:raise T
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
 if y and tuple(B)in HS:return 0
 i=A(K[s<0],-s);m=O(G(),y);o=-I;p=0;g=a
 for mm in m:
  u2=D(mm)
  if not u2:continue
  if(t2:=-S(-b,-g,d-1,y+1))>o:o=t2;p=mm
  U(u2);g=max(g,t2)
  if g>=b:KL[y]=mm;break
 if y==0:BM=p
 return(-10**5+y if i else 0)if o==-I else o
def W(t):
 global n,BM;n=0;BM=0;F(t);HS.add(tuple(B))
 ms=[]
 for x in G():
  u2=D(x)
  if u2:ms.append(x);U(u2)
 o=ms[0];d=1
 if len(ms)>1:
  while 1:
   try:S(-I,I,d,0);o=BM
   except T:break
   d+=1
 F(t);D(o);HS.add(tuple(B))
 return o
def P(p,b):return json.load(r.urlopen(url+p,json.dumps(b).encode()))
url=os.environ["MAKEFUN_ENV_URL"];h=0
while(g2:=P("/game",{}))["status"]!="done":
 if g2["game"]!=h:HS.clear();h=g2["game"]
 while g2["status"]=="your_move":
  mv=u(W(g2["fen"]));L=g2["legal_moves"]
  g2=P("/move",{"game":g2["game"],"move":mv if mv in L else L[0]})
