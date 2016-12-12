import os
import re
import shutil
import fnmatch

file = []
for dirpath, dirs, files in os.walk("."):
    for name in files:
        if fnmatch.fnmatch(name,'stress_strain'):
            full_path=os.path.join(dirpath,name)
            if "ack" not in full_path:
                if "300K" not in full_path:
                    if "r250" in full_path:
                        parse=full_path.split('\\')
                        print parse
                        for i in range(len(parse)):
                            if parse[i]=="single":
                                twin=parse[i]
                            if "twin" in parse[i]:
                                twin=parse[i]
                            r_match=re.search('r[0-9]{1,3}',parse[i])
                            if r_match:
                                radius=parse[i]
                        new_name= "stress_strain_"+str(twin)+"_"+str(radius)+"_F_MAR_T"
                        destination="C:/Users/Thomas/Documents/Code/Test/Tension/tension/" + new_name
                        shutil.copyfile(full_path,destination)
                    
                                
                        
                    
