def reading_file (file):
    f = open(file,'r')
    lines = f.readlines()

    return lines
    f.close()


# set the parameter as the list of lines from the file, and detect the name in the list
def detecting_name (lines):
    # set the user name to the first element of the list
    # remove the leading and trailing whitespace
    user_name = lines[0].strip()

    if user_name[0].isupper() is True:
        pass
    else:
        user_name = 'Invalid Name'

    return user_name



def detecting_email(lines):

    for ele in lines:
        ele = ele.strip()
        
        if '@' in ele and ele[-4:] in ['.com','.edu']:
            has_digit = False
            for i in ele:
                if '0' <= i <= '9':
                    has_digit = True
                    break
            if has_digit is False:
                return ele

    return ''




def detecting_courses(lines):

    for ele in lines:
        ele = ele.strip()
        
        if ele[0:7] =='Courses':
            for i in range(7, len(ele)):
                if 'a' <= ele[i] <= 'z' or 'A' <= ele[i] <= 'Z':
                    course_list = ele[i:].split(',')
                    break

    for i in range(0, len(course_list)):
        
        course_list[i] = course_list[i].strip()
            
    return course_list


def detecting_projects(lines):

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()
        projects = []
        if lines[i][0:8] =='Projects':
            for j in range(i+1, len(lines)):
                lines[j] = lines[j].strip()
                if lines[j][0:9]== '----------':
                    break
                else:
                    projects.append(lines[j])
            break

    return projects
            

                    

    
    
