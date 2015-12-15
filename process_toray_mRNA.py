import os
import sys
import math

target=open(sys.argv[1])
infoDict={}
dataDict={}
fileDict={}

for info in target:
    info=info.strip("\n")
    infoTab=info.split("\t")
    key=infoTab[0]+"_"+infoTab[1]
    infoDict[key]=infoTab[2]

controls=["Positive Control 1","Positive Control 2_n","Positive Control 2","Positive control 2", "Positive control 3", "Negative control 1", "Negative control 2", "Negative control 3", "Negative control 4", "BLANK", "No probe", "S-Probe 3", "S-Probe 2", "S-Probe 4", "S-Probe 5", "S-Probe 6", "S-Probe 7", "S-Probe 1", "Negative Control 1", "Negative Control 2", "Negative Control 3", "Negative Control 4", "Negative Control 2_n", "Negative Control 4_n", "Negative Control 1_n", "Negative Control 3_n"]
first_first=1
for filename in os.listdir("."):
     splitFile = filename.split("_")
     if len(splitFile)>3:
         chip=splitFile[0]
         cell=splitFile[1]
         key=chip+"_"+cell[4]
         if key in infoDict:
            chipData = open(filename)
            first=1
            for data in chipData:
                 data=data.strip("\n")
                 dataTab=data.split("\t")
                 if first==1:
                     if first_first==1:
                         dataDict[dataTab[0]]=dataTab[0]+"\t"+dataTab[1]+"\t"+dataTab[2]+"\t"+dataTab[3]+"\t"+dataTab[4]+"\t"+dataTab[5]+"\t"+dataTab[6]+"\t"+dataTab[7]+"\t"+dataTab[8]+"\t"+dataTab[9]+"\t"+infoDict[key]+"\t"
                         first_first=0
                     else:
                         dataDict[dataTab[0]]=dataDict[dataTab[0]]+infoDict[key]+"\t"

                     first=0
                 else:
                     if not dataTab[0] in controls:

                        if not dataTab[0] in dataDict:
                            fileDict[dataTab[0]]=filename
                            if not dataTab[12]=="":
                                 dataLog2_cy5=math.log(float(dataTab[12]), 2)
                            else:
                                 dataLog2_cy5="NA"

                            #if not dataTab[15]=="":
                            #     dataLog2_cy3=math.log(float(dataTab[15]), 2)
                            #else:
                            #     dataLog2_cy3="NA"

                            dataDict[dataTab[0]]=dataTab[0]+"\t"+dataTab[1]+"\t"+dataTab[2]+"\t"+dataTab[3]+"\t"+dataTab[4]+"\t"+dataTab[5]+"\t"+dataTab[6]+"\t"+dataTab[7]+"\t"+dataTab[8]+"\t"+dataTab[9]+"\t"+str(dataLog2_cy5)+"\t"
                        else:
                            if not dataTab[12]=="":
                                 dataLog2_cy5=math.log(float(dataTab[12]), 2)
                            else:
                                 dataLog2_cy5="NA"

                            #if not dataTab[15]=="":
                            #     dataLog2_cy3=math.log(float(dataTab[15]), 2)
                            #else:
                            #     dataLog2_cy3="NA"

                            n=2
                            if fileDict[dataTab[0]]==filename:
                                if not dataTab[0]+"_n" in dataDict:
                                    dataDict[dataTab[0]+"_n"]=dataTab[0]+"_n"+"\t"+dataTab[1]+"\t"+dataTab[2]+"\t"+dataTab[3]+"\t"+dataTab[4]+"\t"+dataTab[5]+"\t"+dataTab[6]+"\t"+dataTab[7]+"\t"+dataTab[8]+"\t"+dataTab[9]+"\t"+str(dataLog2_cy5)+"\t"
                                else:
                                    dataDict[dataTab[0]+"_n"]=dataDict[dataTab[0]+"_n"]+str(dataLog2_cy5)+"\t"
                            else:
                                dataDict[dataTab[0]]=dataDict[dataTab[0]]+str(dataLog2_cy5)+"\t"
                                fileDict[dataTab[0]]=filename

merged=open("merged_data.txt", "w")

merged.write(dataDict["Name"]+"\n")
for mRNA in dataDict:
    if not mRNA =="Name":
        merged.write(dataDict[mRNA]+"\n")


