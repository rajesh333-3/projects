#give the base path in the script and give the target variable name to edited

import glob
basepath='G:\Series'
target_file_name=input('Enter the extension or target file name to locate..! -->  ')
relative_paths=glob.glob(basepath+"/**/*{}".format(target_file_name),recursive=True)
#print((relative_paths))
n=int(input('Enter number of target variables to be edited/updated ?  '))
target_variable=[]
insert_value=[]
#################################
for y in range(n):
    target_variable.append(input('Enter Target Variable {} -->  '.format(y)))
    value=   input('Enter Value to Assign {} -->  '.format(y))
    insert_value.append(value+'\n')
################################
for i in range(len(target_variable)):
    print('*'*50)
    print('Parent Folder:',basepath)
    print('Edit Attempt :',target_variable[i],'=',insert_value[i])
    print('*'*50)
    confirmation=input('!! Confirm to continue !! : Y/N -->  ')
    if confirmation in ['Y','y']:
        for path in relative_paths:
            f=open(path,'r')
            lines_list=f.readlines()
            f.close()
            edited=0
            for lineno in range(len(lines_list)):
                if target_variable[i]+'=' in lines_list[lineno]:
                    lines_list[lineno]=target_variable[i]+'='+insert_value[i]
                    print('value edited in:',path)
                    edited=1
            if edited==0:
                lines_list.append(target_variable[i]+'='+insert_value[i])
                print('value Inserted to file:',path)  
            f=open(path,'w')
            # lines_list=list(set(lines_list))
            seen=set()
            lines_list=[x for x in lines_list if not( x in seen or seen.add(x))]
            if '\n' in lines_list:    
                lines_list.remove('\n')
            if '' in lines_list:
                lines_list.remove('')
            edited_data=''.join(lines_list)
            f.write(edited_data)
            f.close()
        print('JOB COMPLETE...!')
    else:
        print('JOB ABORTED...!')
  