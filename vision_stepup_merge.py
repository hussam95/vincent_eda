# Vision Scholars

## BAM
import pandas as pd
vs_bam= pd.read_excel(r"C:\\Users\\Hussam\\Desktop\\RT Fisher\\VISION SCHOLAR student list.xlsx", sheet_name="BAM")
vs_bam.head()
vs_bam_ids=vs_bam["Student ID"].tolist()
len(vs_bam_ids)
master_sheet = pd.read_excel(r"C:\\Users\\Hussam\\Desktop\\RT Fisher\\rt_fisher_data.xlsx", sheet_name="TK-5")
master_sheet.head(2)
master_sheet_ids = master_sheet["Student ID"].tolist()
len(master_sheet_ids)
counter=0
for vs_bam_id in vs_bam_ids:
    if vs_bam_id in master_sheet_ids:
        rowIndexes = master_sheet.index[master_sheet["Student ID"]==vs_bam_id]
        for rowIndex in rowIndexes:
            master_sheet.loc[rowIndex, 'Vision Scholars'] = 1
master_sheet["Vision Scholars"].value_counts()


## Malx
vs_malx= pd.read_excel(r"C:\\Users\\Hussam\\Desktop\\RT Fisher\\VISION SCHOLAR student list.xlsx", sheet_name="Malcolm X")
vs_malx_ids=vs_malx["Student ID"].tolist()
print(len(vs_malx))
counter=0
for vs_malx_id in vs_malx_ids:
    if vs_malx_id in master_sheet_ids:
        rowIndexes = master_sheet.index[master_sheet["Student ID"]==vs_malx_id]
        for rowIndex in rowIndexes:
            master_sheet.loc[rowIndex, 'Vision Scholars'] = 1
print(master_sheet["Vision Scholars"].value_counts())



## Oxford
vs_ox= pd.read_excel(r"C:\\Users\\Hussam\\Desktop\\RT Fisher\\VISION SCHOLAR student list.xlsx", sheet_name="Oxford")
vs_ox_ids=vs_ox["Student ID"].tolist()
print(len(vs_ox_ids))
counter=0
for vs_ox_id in vs_ox_ids:
    if vs_ox_id in master_sheet_ids:
        rowIndexes = master_sheet.index[master_sheet["Student ID"]==vs_ox_id]
        for rowIndex in rowIndexes:
            master_sheet.loc[rowIndex, 'Vision Scholars'] = 1
print(master_sheet["Vision Scholars"].value_counts())



## Washington
vs_wash= pd.read_excel(r"C:\\Users\\Hussam\\Desktop\\RT Fisher\\VISION SCHOLAR student list.xlsx", sheet_name="Washington")
vs_wash_ids=vs_wash["Student ID"].tolist()
print(len(vs_wash_ids))
counter=0
for vs_wash_id in vs_wash_ids:
    if vs_wash_id in master_sheet_ids:
        rowIndexes = master_sheet.index[master_sheet["Student ID"]==vs_wash_id]
        for rowIndex in rowIndexes:
            master_sheet.loc[rowIndex, 'Vision Scholars'] = 1
print(master_sheet["Vision Scholars"].value_counts())


## Longfellow 
vs_long= pd.read_excel(r"C:\\Users\\Hussam\\Desktop\\RT Fisher\\VISION SCHOLAR student list.xlsx", sheet_name="Longfellow")
vs_long_ids=vs_long["Student ID"].tolist()
print(len(vs_long_ids))
c=0
for vs_long_id in vs_long_ids:
    if vs_long_id in master_sheet_ids:
        rowIndexes = master_sheet.index[master_sheet["Student ID"]==vs_long_id]
        for rowIndex in rowIndexes:
            master_sheet.loc[rowIndex, 'Vision Scholars'] = 1
            c+=1
print(master_sheet["Vision Scholars"].value_counts())
print(c)
#699 ids where unique are 52 and longfellow data only for T1 in master sheet**


master_sheet["Vision Scholars"].value_counts()
master_sheet["Vision Scholars"]=master_sheet["Vision Scholars"].fillna(0)
master_sheet["Vision Scholars"].value_counts()
X_index= master_sheet.index[master_sheet["Vision Scholars"]=="X"]
master_sheet.loc[X_index,"Vision Scholars"]=0
master_sheet["Vision Scholars"].value_counts()
master_sheet.head(1)


## Reading Level Data 
vs_rld= pd.read_excel(r"C:\\Users\\Hussam\\Desktop\\RT Fisher\\VISION SCHOLAR student list.xlsx", sheet_name="Reading level data")
vs_rld_first=vs_rld["First "].tolist()
vs_rld_last = vs_rld["Student (K-3) Last "].tolist()
print(len(vs_rld_first))
print(len(vs_rld_last))
c=0
for vs_rld_name in zip(vs_rld_first,vs_rld_last):
    if vs_rld_name in zip(master_sheet["First Name"].tolist(),master_sheet["Last Name"].tolist()):
        rowIndexes = master_sheet.index[master_sheet["First Name"]==vs_rld_name]
        for rowIndex in rowIndexes:
            master_sheet.loc[rowIndex, 'Vision Scholars'] = 1
        c+=1
print(master_sheet["Vision Scholars"].value_counts())
print(c)
data=pd.read_excel(r"C:\\Users\\Hussam\Desktop\\RT Fisher\\vision_implemented_tk_5.xlsx")
data["Vision Scholars"].value_counts()
data["First Name"].value_counts(dropna=False)
data["First Name"]=data["First Name"].fillna(" ")
data["First Name"].value_counts()
data["First Name"]=data["First Name"].astype(object)
data["First Name"].info
data["Last Name"]=data["Last Name"].fillna(" ")
data["Last Name"].value_counts()
vs_rld= pd.read_excel(r"C:\\Users\\Hussam\\Desktop\\RT Fisher\\VISION SCHOLAR student list.xlsx", sheet_name="Reading level data")
vs_rld_first=vs_rld["First "].tolist()
vs_rld_last = vs_rld["Student (K-3) Last "].tolist()
vs_rld_names=[f+" "+l for f,l in zip(vs_rld_first,vs_rld_last)]
c=0

for index,row in data.iterrows():
    name=(row["First Name"])+" " +(row["Last Name"])
    data.loc[index,"full name"]=name
    if name in vs_rld_names:
        rowIndexes = data.index[data["full name"]==name]
        for rowIndex in rowIndexes:
            data.loc[rowIndex, 'Vision Scholars'] = 1
        c+=1
print(data["Vision Scholars"].value_counts())
print(c)

vs_rld_names
data["name"].value_counts()
data




# Step UP

## Export 1

import pandas as pd
step_up_ex1= pd.read_excel(r"C:\Users\Hussam\Desktop\RT Fisher\STEP UP Academy student list.xlsx", sheet_name="Export 5.17.22")
step_up_ex1.head(1)
master_sheet = pd.read_excel(r"C:\Users\Hussam\Desktop\RT Fisher\vision_implemented_tk_5.xlsx")
master_sheet.head(1)
master_sheet["Vision Scholars"].value_counts()
step_up_ex1["STUDENT FIRST NAME"].head()
step_up_ex1["STUDENT LAST NAME"].head()
len(step_up_ex1)
f_name=step_up_ex1["STUDENT FIRST NAME"]
counter={}
for name in f_name:
    if name in counter:
        counter[name]+=1
    else:
        counter[name]=1
c=0
for value in counter.values():
    if value==2:
        c+=1
print(c)
len(step_up_ex1)-c
#**41 unique names in step up export 1**

#  Work on Export 1 Here
master_sheet = pd.read_excel(r"C:\Users\Hussam\Desktop\RT Fisher\vision_implemented_tk_5.xlsx")
master_sheet[["First Name", "Last Name"]].info()
master_sheet["First Name"]=master_sheet["First Name"].fillna(" ")
master_sheet["First Name"]=master_sheet["First Name"].astype(str)
master_sheet["First Name"].info()
master_sheet["Last Name"]=master_sheet["Last Name"].fillna(" ")
master_sheet["Last Name"]=master_sheet["Last Name"].astype(str)
master_sheet["Last Name"]
master_sheet[["First Name", "Last Name"]].info()
step_up_ex1= pd.read_excel(r"C:\\Users\\Hussam\Desktop\\RT Fisher\\STEP UP Academy student list.xlsx", sheet_name="Export 5.17.22")
step_up_ex1_first=step_up_ex1["STUDENT FIRST NAME"].tolist()
step_up_ex1_last = step_up_ex1["STUDENT LAST NAME"].tolist()
step_up_ex1_names=[f+" "+l for f,l in zip(step_up_ex1_first,step_up_ex1_last)]
c=0

for index,row in master_sheet.iterrows():
    name=(row["First Name"]) + " " + (row["Last Name"])
    master_sheet.loc[index,"full name"]=name
    if name in step_up_ex1_names:
        rowIndexes = master_sheet.index[master_sheet["full name"]==name]
        for rowIndex in rowIndexes:
            if master_sheet.loc[rowIndex, "Vision Scholars"]==0:
                master_sheet.loc[rowIndex, 'Vision Scholars'] = 5
            if master_sheet.loc[rowIndex, "Vision Scholars"]==1:
                master_sheet.loc[rowIndex, 'Vision Scholars'] = 6
        c+=1
print(master_sheet["Vision Scholars"].value_counts())
print(c)


## Export 2
step_up_ex2= pd.read_excel(r"C:\\Users\\Hussam\Desktop\\RT Fisher\\STEP UP Academy student list.xlsx", sheet_name="Export 5.24.22")
step_up_ex2_first=step_up_ex2["Student 1 Name:"].tolist()
step_up_ex2_last = step_up_ex2["Student Last"].tolist()
step_up_ex2_names=[f+" "+l for f,l in zip(step_up_ex2_first,step_up_ex2_last)]
c=0

for index,row in master_sheet.iterrows():
    name=(row["First Name"]) + " " + (row["Last Name"])
    master_sheet.loc[index,"full name"]=name
    if name in step_up_ex2_names:
        rowIndexes = master_sheet.index[master_sheet["full name"]==name]
        for rowIndex in rowIndexes:
            if master_sheet.loc[rowIndex, "Vision Scholars"]==0:
                master_sheet.loc[rowIndex, 'Vision Scholars'] = 5
            if master_sheet.loc[rowIndex, "Vision Scholars"]==1:
                master_sheet.loc[rowIndex, 'Vision Scholars'] = 6
        c+=1
print(master_sheet["Vision Scholars"].value_counts())
print(c)


## Export 3
step_up_ex3= pd.read_excel(r"C:\\Users\\Hussam\Desktop\\RT Fisher\\STEP UP Academy student list.xlsx", sheet_name="Export 6.03.22")
step_up_ex3_first=step_up_ex3["Student 1 Name:"].tolist()
step_up_ex3_last = step_up_ex3["Student Last"].tolist()
step_up_ex3_names=[f+" "+l for f,l in zip(step_up_ex3_first,step_up_ex3_last)]
c=0

for index,row in master_sheet.iterrows():
    name=(row["First Name"]) + " " + (row["Last Name"])
    master_sheet.loc[index,"full name"]=name
    if name in step_up_ex3_names:
        rowIndexes = master_sheet.index[master_sheet["full name"]==name]
        for rowIndex in rowIndexes:
            if master_sheet.loc[rowIndex, "Vision Scholars"]==0:
                master_sheet.loc[rowIndex, 'Vision Scholars'] = 5
            if master_sheet.loc[rowIndex, "Vision Scholars"]==1:
                master_sheet.loc[rowIndex, 'Vision Scholars'] = 6
        c+=1
print(master_sheet["Vision Scholars"].value_counts())
print(c)


## Export 4
step_up_ex4= pd.read_excel(r"C:\\Users\\Hussam\Desktop\\RT Fisher\\STEP UP Academy student list.xlsx", sheet_name="School Sort")
step_up_ex4_first=step_up_ex4["STUDENT FIRST NAME"].tolist()
step_up_ex4_last = step_up_ex4["STUDENT LAST NAME"].tolist()
step_up_ex4_names=[f+" "+l for f,l in zip(step_up_ex4_first,step_up_ex4_last)]
c=0

for index,row in master_sheet.iterrows():
    name=(row["First Name"]) + " " + (row["Last Name"])
    master_sheet.loc[index,"full name"]=name
    if name in step_up_ex4_names:
        rowIndexes = master_sheet.index[master_sheet["full name"]==name]
        for rowIndex in rowIndexes:
            if master_sheet.loc[rowIndex, "Vision Scholars"]==0:
                master_sheet.loc[rowIndex, 'Vision Scholars'] = 5
            if master_sheet.loc[rowIndex, "Vision Scholars"]==1:
                master_sheet.loc[rowIndex, 'Vision Scholars'] = 6
        c+=1
print(master_sheet["Vision Scholars"].value_counts())
print(c)
master_sheet.to_excel("vision_step_implemented.xlsx")