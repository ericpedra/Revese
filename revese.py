import time
import sys

def xtime():
    t = time.localtime()
    hr = t.tm_hour
    mn = t.tm_min
    sc = t.tm_sec
    return '[{}:{}:{}] '.format(hr, mn, sc)

def logo():
    print "|create by     : Eric Pedra"
    print "|contact person: erikpedraz10@gmail.com"
    print "|date created  : 29 desember 2018"
    print "|tools for     : Reverse Email, from Pass|Email ->to-> Email|Pass"

logo()
time.sleep(0.5)
print ""
print "\t\t\t==--+ [Selamat Datang Pak...] +--==\n"
nm_f = raw_input(xtime()+"[+]File Name root@evolution: ")
d_lm = raw_input(xtime()+"[+]Delimeter pada daftar Anda, mis: '|' root@evolution: ")
op_f = open(nm_f, "r")
rln = op_f.readlines()
pjg = len(rln)
print xtime()+"[+]==--+ ["+str(pjg)+"%] +--=="
print xtime()+"[+]==--+ [Tunggu..] +--=="
refl = open("result.txt", "w")
#idx = 0 menghasilkan UnboundLocalError: local variable 'idx' referenced before assignment
def reverse():
    idx = 0
    for i in rln:
        try:
            idx += 1
            sys.stdout.write("\r"+xtime()+"[*]==--+ [%d%%] +--==" % idx)
            sys.stdout.flush()  # use to clear unknown char in this line, so it can make neat
            sp = i.strip().split(d_lm)
            refl.write(sp[1] + "|" + sp[0] + "\n")
        except IndexError:
            print "[!]Check line:"+str(idx)+" maybe delim not sure"

reverse()
print ""
print ""
print xtime()+"[+]Selesai"
print xtime()+"[+]Hasil disimpan keSelesai 'resutl.txt' "
print "\n\t\t\t==--+ [Finished..!!] +--=="
print "==--+ [Terima Kasih Telah Menggunakan Tools ./evolution] +--=="
print ""
print "note: jika Anda memiliki pertanyaan, Anda dapat menghubungi saya"
print "erikpedraz10@gmail.com"
