import json,os,urllib.request as U
L=100000
I=30000
D={'N':(-21,-19,-12,-8,8,12,19,21),'B':(-11,-9,9,11),'R':(-10,-1,1,10)}
D['Q']=D['K']=D['B']+D['R']
V=dict(P=100,N=320,B=330,R=500,Q=900,K=10000)
def pt(p,f):
 t=[0]*120
 for s in range(21,99):
  r=9-s//10;c=s%10-1;m=min(r,7-r)+min(c,7-c)
  x=dict(P=(0,0,3,9,21,42,80,0)[r]+(2<c<5)*(r>1)*6,N=12*m-36,B=6*m-18,R=(r==6)*20+m,Q=2*m,K=6*abs(2*c-7)-24*r)[p]
  t[s]=V[p]+(x*f+dict(P=x+r*r,K=10*m-30).get(p,x)*(8-f))//8
 return t
PS={}
def gen(b,cr,ep,q):
 M=[]
 for i in range(21,99):
  p=b[i]
  if not p.isupper():continue
  T=PS[p]
  if p=='P':
   for j in(i-10,i-20):
    if b[j]!='.'or j<i-10 and(i<81 or b[i-10]!='.'):break
    if not q or j<30:M+=[(T[j]-T[i]+(PS['Q'][j]-T[j])*(j<30),i,j)]
   for j in(i-11,i-9):
    c=b[j]
    if c.islower()or j==ep:M+=[(T[j]-T[i]+PS[c.upper()if c!='.'else'P'][119-j-10*(c=='.')]+(PS['Q'][j]-T[j])*(j<30),i,j)]
  else:
   for d in D[p]:
    j=i
    while 1:
     j+=d;c=b[j]
     if c==' 'or c.isupper():break
     if c!='.'or not q:M+=[(T[j]-T[i]+(PS[c.upper()][119-j]if c!='.'else 0),i,j)]
     if c!='.'or p in'NK':break
 if not q:
  for c in(91,98):
   if c in cr and b[c]=='R':
    d=1 if c==91 else-1;s=c+d
    while b[s]=='.':s+=d
    if b[s]=='K':K=PS['K'];R=PS['R'];M+=[(K[s-2*d]-K[s]+R[s-d]-R[c],s,s-2*d)]
 return M
def mk(b,cr,ep,i,j):
 p=b[i];t=list(b);t[i]='.'
 if p=='P':
  if j<30:p='Q'
  if j==ep:t[j+10]='.'
 t[j]=p
 if p=='K':
  cr=cr-{91,98}
  if abs(j-i)==2:
   d=(j-i)//2;s=j+d
   while t[s]=='.':s+=d
   t[s]='.';t[i+d]='R'
 return''.join(t[::-1]).swapcase(),frozenset(119-c for c in cr if c!=i and c!=j),129-i if p=='P'and i-j==20 else 0
E=Exception
def S(b,sc,cr,ep,d,a,bt,pl):
 global N,BM
 N+=1
 if N>L:raise E
 if sc<-5000:return-I
 k=b,cr
 if pl and k in P:return 0
 e=T.get(k);tm=0
 if e:
  tm=e[3]
  if e[0]>=d and pl and(e[2]==0 or e[2]>0 and e[1]>=bt or e[2]<0 and e[1]<=a):return e[1]
 q=d<=0;bs=-I
 if q:
  if sc>=bt:return sc
  a=max(a,sc);bs=sc
 if d>2 and pl and sc>=bt:
  v=-S(b[::-1].swapcase(),-sc,frozenset(119-c for c in cr),0,d-3,-bt,1-bt,pl+1)
  if v>=bt:return v
 ms=gen(b,cr,ep,q)
 ms.sort(key=lambda m:-m[0]-99999*(m[1:]==tm)-Y.get(m[1:],0))
 a0=a;bm=0;P.add(k)
 for g,i,j in ms:
  if pl==0 and(i,j)not in R:continue
  nb,c2,e2=mk(b,cr,ep,i,j)
  v=-S(nb,-sc-g,c2,e2,d-1,-bt,-a,pl+1)
  if v>bs:bs=v;bm=i,j
  if v>a:
   a=v
   if a>=bt:
    if b[j]=='.':Y[i,j]=min(Y.get((i,j),0)+d*d,90)
    break
 P.discard(k)
 if pl==0 and bs>=bt:BM=bm
 if bs==-I and not q:
  bs=-29000-d if any(m[0]>5000 for m in gen(b[::-1].swapcase(),(),0,1))else 0
 if not q:T[k]=d,bs,(bs>=bt)-(bs<=a0),bm
 return bs
def sq(s):return'abcdefgh'[s%10-1]+str(10-s//10)
def fs(x):return 21+(8-int(x[1]))*10+'abcdefgh'.find(x[0])
T={}
Y={}
def think(b,cr,ep,r,H):
 global T,Y,P,N,BM,R
 R=r
 if len(T)>400000:T={}
 f=min(8,(sum(V[c]for c in b.upper()if c in"NBRQ")-1000)//500)
 for p in V:PS[p]=pt(p,f)
 Y={};P=set(H);N=0;BM=next(iter(R));sv=0
 try:
  for d in range(1,30):
   lo,hi=-3000,3000;z=sv;s=12
   while lo<hi-4:
    v=S(b,0,cr,ep,d,z-1,z,0)
    if v<z:hi=v
    else:lo=v
    s*=2;z=(lo+hi+1)//2 if lo>-3000 and hi<3000 else max(lo+1,hi-s)if lo<=-3000 else min(hi,lo+s)
   sv=lo
   if lo>5000:break
 except E:pass
 H.add((b,cr));H.add(mk(b,cr,ep,*BM)[:2])
 return BM
def Z(p,o):return json.load(U.urlopen(U.Request(os.environ["MAKEFUN_ENV_URL"]+p,json.dumps(o).encode(),{"content-type":"application/json"})))
H=set()
while 1:
 g=Z("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":
  f=g["fen"].split()
  b=' '*20
  for r in f[0].split('/'):b+=' '+''.join(c if c>'9'else'.'*int(c)for c in r)+' '
  b+=' '*20
  w=f[1]=='w'
  cr=frozenset((98,91,28,21)['KQkq'.find(c)]for c in f[2]if c!='-')
  ep=fs(f[3])if f[3]!='-'else 0
  R=set()
  for m in g["legal_moves"]:
   x=fs(m[:2]);y=fs(m[2:4]);R|={(x,y)if w else(119-x,119-y)}
  if not w:b=b[::-1].swapcase();cr=frozenset(119-c for c in cr);ep=119-ep if ep else 0
  i,j=think(b,cr,ep,R,H)
  u='q'if b[i]=='P'and j<30 else''
  if not w:i=119-i;j=119-j
  g=Z("/move",{"game":g["game"],"move":sq(i)+sq(j)+u})
 H=set()
