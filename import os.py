from filecmp import dircmp
import os
import shutil
import csv


# shutil.copyfile('D:/SAV', 'D:/django')


# def print_diff_files(dcmp):
#     for name in dcmp.diff_files:
#         print("diff_file %s found in %s and %s" % (name, dcmp.left,
#               dcmp.right))

# for sub_dcmp in dcmp.subdirs.values():
#         print_diff_files(sub_dcmp)

# dcmp = dircmp('D:/SAV', 'D:/django') 
# print_diff_files(dcmp) 
# print('FF',dcmp) 
Sr = '//sagex3//FRA3'
Des='D:/django'
Src = os.listdir(Sr)
# for entry in Src:
#      print(entry)
#      print(os.path.join('D:/SAV'))
#      shutil.copy('D:/SAV'+'/'+entry, 'D:/django')

# open the file in the write mode
f = open('D:/csv_file', 'w')

# create the csv writer
writer = csv.writer(f,)
Dest = os.listdir(Des)
x=0
for src in Src:
    if src not in Dest:
     x=x+1
     print('diferrencr',src,x)
     shutil.copy(Sr+'/'+src, Des)
     writer.writerow([src])
     # write a row to the csv file
#writer.writerows(Src)
     
    




# close the file
f.close()