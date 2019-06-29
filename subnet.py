#only class c subnetting

print("NOTICE :- ipaddress should be of combination of 4 8-octate for eg (8octate.8octate.8octate.8octate) , full 8 bit =255 ip address shoild not be more than 255 and cidr not more than 32")

def rec(x):
    if x==8:
        return 0
    else:
        return 2**x + rec(x+1)







ipt=input("enter ip with cidr eg: 192.169.0.0/25: ")
print("\n")

ip1=ipt.split("/")
cidr=int(ip1[1])
ip=[0,0,0,0]
org=ip1[0]
org1=org.split(".")
for i in range(4):
    ip[i]=int(org1[i])


#print("ip= ", org)
#print("cidr= ", cidr)
#print(ip)

mask=rec(32-cidr)
#print(mask)
net=2**(cidr-24)
val=2**(32-cidr) - 2
if val==-1:
    val=0

jmp=256-mask
tmp=0
brl=0
a=ip[3]
b=0
c=0
d=0
#print ("\n")
#print (mask,cidr,net,val,jmp)
while(a < mask):
    a=a+tmp
    print("network id :       ", ip[0],".",ip[1],".",ip[2],".",a)
    b=a+1
    print("first valid host : ", ip[0],'.',ip[1],'.',ip[2],'.',b)
    c=b-1+val
    print("last valid host :  ",ip[0],'.',ip[1],'.',ip[2],'.',c)
    d=c+1
    print("broadcaste id :    ",ip[0],'.',ip[1],'.',ip[2],'.',d)
    print("\n")
    tmp=jmp


