###############################################################################
##Afvinkopdracht 3, Blok 3, Richard Jansen HAN University Of Applied Sciences##
##17-03-2015###################################################################
###############################################################################

from tkinter import *
from tkinter import filedialog
writefile = open("rawseq.txt", "w")
niets=Tk()
file = filedialog.askopenfile()
niets.destroy()
niets.mainloop()
seq = []
lijst = []
lijst2 = []
codons = []
codonfreq = []
from collections import Counter

def main():
    x = startread(file)
    startindex = gimmeinfo(x)
    freq = {}
    freq = Counter(lijst)
    dictmod(freq)
    translation(x, startindex)
   
def startread(seq):
    raw_data = ""
    startReading = False
    for regel in seq:
        if startReading:
            raw_data += regel[10:]
        if "ORIGIN" in regel:
            startReading = True
    sequence = raw_data.replace(' ','').replace('\n','').replace('\r','')
    return sequence
    

def gimmeinfo(seq):
    z, s = 0, 3
    codonseq = ""
    startindex = seq.index("atg")
    print('Startcodon on location: ' +str(startindex))
    for z in range (startindex, (len(seq)-startindex)):
        vanafstart = seq[startindex:]        
        codon = vanafstart[s-3:s]
        codonseq += codon
        if codon in ('taa', 'tga', 'tag'):
            print('Stopcodon on location: ' +str(z//3+startindex))
            break
        else:
            s += 3
    for i in range(0, len(codonseq),3):
        lijst.append(codonseq[i:i+3])
    return startindex
def dictmod(freq):
    lijst2.append(freq.keys())
    for x in freq:
        codons.append(x)
        codonfreq.append(freq[x])
        
def translation(x,start):
    data= x
    map = {"ttt":"F", "ttc":"F", "tta":"L", "ttg":"L",
           "tct":"S", "tcc":"S", "tca":"S", "tcg":"S",
           "tat":"Y", "tac":"Y", "taa":"STOP", "tag":"STOP",
           "tgt":"C", "tgc":"C", "tga":"STOP", "tgg":"W",
           "ctt":"L", "ctc":"L", "cta":"L", "ctg":"L",
           "cct":"P", "ccc":"P", "cca":"P", "ccg":"P",
           "cat":"H", "cac":"H", "caa":"Q", "cag":"Q",
           "cgt":"R", "cgc":"R", "cga":"R", "cgg":"R",
           "att":"I", "atc":"I", "ata":"I", "atg":"M/START",
           "act":"T", "acc":"T", "aca":"T", "acg":"T",
           "aat":"N", "aac":"N", "aaa":"K", "aag":"K",
           "agt":"S", "agc":"S", "aga":"R", "agg":"R",
           "gtt":"V", "gtc":"V", "gta":"V", "gtg":"V",
           "gct":"A", "gcc":"A", "gca":"A", "gcg":"A",
           "gat":"D", "gac":"D", "gaa":"E", "gag":"E",
           "ggt":"G", "ggc":"G", "gga":"G", "ggg":"G",}

    aa = []    
    DNA=data
    while start+2 < len(DNA):
        codon = DNA[start:start+3]
        if codon == "tag": break;
        aa.append(map[codon])               
        start+=3
    print (aa)

main()