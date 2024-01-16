
def reading_file(file):
    '''read the resume file into a list of lines'''

    f = open(file, 'r')
    lines = f.readlines()

    f.close()
    return lines




def detecting_name(lines):
    '''detect the user's name in the list of lines'''


    # remove the leading and trailing whitespace
    user_name = lines[0].strip()

    # if the first letter of name is not uppercase letter, then use 'Invalid Name' as user's name
    if user_name[0].isupper() is True:
        pass
    else:
        user_name = 'Invalid Name'

    return user_name


def detecting_email(lines):
    ''' detect the user's email in the list of lines'''

    # remove the leading and trailing whitespace
    for ele in lines:
        ele = ele.strip()

        # detect the email address using the character @
        # make sure the last four character of the email are either '.com' or '.edu'
        if '@' in ele and ele[-4:] in ['.com', '.edu']:
            has_digit = False

            # make sure there are no digits or numbers in the email address
            for i in ele:
                if '0' <= i <= '9':
                    has_digit = True
                    break
            if has_digit is False:
                return ele

    # if no email string is found then consider the email address to be missing
    # return an empty string
    return ''


def detecting_courses(lines):
    ''' detect the courses in the list of lines'''

    # remove the leading and trailing whitespace
    for ele in lines:
        ele = ele.strip()

        # detect courses by checking if the first seven character of a line is 'Courses'
        if ele[0:7] == 'Courses':

            # skip all the punctuations after 'Courses' and locate the first letter after 'Courses' in the line
            for i in range(7, len(ele)):
                if 'a' <= ele[i] <= 'z' or 'A' <= ele[i] <= 'Z':

                    # break the string after the first letter by comma, and put them into a list
                    course_list = ele[i:].split(',')
                    break

    return course_list


def detecting_projects(lines):
    ''' detect the projects in the list of lines '''

    # put the lines after the word 'Projects' into a list till hit a line that has at least 10 minus signs
    for i in range(0, len(lines)):
        project_lines = []
        lines[i] = lines[i].strip()

        if lines[i][0:8] == 'Projects':
            for j in range(i + 1, len(lines)):
                lines[j] = lines[j].strip()
                if lines[j][0:10] == '----------':
                    break
                else:
                    project_lines.append(lines[j])
            break

    # if any of the lines in project_lines are blank, then skip the line
    projects = []
    for ele in project_lines:
        if len(ele) <= 1:
            continue
        projects.append(ele)

    return projects

def surround_block(tag, text):
    """
    Surrounds the given text with the given html tag and returns the string.
    """

    # surround the given test with the given tag
    return '<{}>{}</{}>'.format(tag,text,tag)


def create_email_link(email_address):
    """
    Creates an email link with the given email_address.
    To cut down on spammers harvesting the email address from the webpage,
    displays the email address with [aT] instead of @.

    Example: Given the email address: lbrandon@wharton.upenn.edu
    Generates the email link: <a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>

    Note: If, for some reason the email address does not contain @,
    use the email address as is and don't replace anything.
    """

    # split the strings in email address before and after @ into a list
    email_list = email_address.split('@')

    # use [aT] as separator, and combine the list into a new string
    separator = '[aT]'
    new_email = separator.join(email_list)

    return '<a href="mailto:{}">{}</a>'.format(email_address, new_email)


def basic_information_section (name, email_address):
    ''' turn the user's name and email address from the text file to html'''

    # surround the basic information in html with <div>
    # surround the name in html with <h1>
    # surround the email address in html with <p>
    return surround_block('div', '\n' + surround_block('h1', name) + '\n' +
                          surround_block('p',"Email:" + create_email_link(email_address)) +'\n') + '\n'


def projects_section (projects):
    ''' turn the projects from text file to html'''

    # surround the word "Project" with <h2>
    # surround the projects in html with <li>, then <ul>
    # surround the projects section in html with <div>
    projects_list = []
    for project in projects:
        projects_list.append(surround_block('li', project))

    project_str = '\n'.join(projects_list)

    header = surround_block('h2', "Projects")
    return surround_block('div', '\n' + header + '\n' + surround_block('ul','\n'+ project_str + '\n') + '\n') + '\n'

def courses_section (courses):
    ''' turn the courses from text file to html'''

    # surround the word "Courses" with <h3>
    # surround the list of courses in html with <span>
    # surround the courses section in html with <div>
    courses_str = surround_block('span',','.join(courses))
    header = surround_block('h3', "Courses")
    return surround_block('div', '\n' + header + '\n' + courses_str + '\n') + '\n'


def generate_html(txt_input_file, html_output_file):
    """
    Loads given txt_input_file,
    gets the name, email address, list of projects, and list of courses,
    then writes the info to the given html_output_file.

    # Hint(s):
    # call function(s) to load given txt_input_file
    # call function(s) to get name
    # call function(s) to get email address
    # call function(s) to get list of projects
    # call function(s) to get list of courses
    # call function(s) to write the name, email address, list of projects, and list of courses to the given html_output_file
    """

    # call the functions created before for name, email, project and courses
    # cast all the content from the text resume into new variables
    resume_lines = reading_file(txt_input_file)

    txt_name = detecting_name(resume_lines)

    txt_email = detecting_email(resume_lines)

    txt_projects = detecting_projects(resume_lines)

    txt_courses = detecting_courses(resume_lines)

    # open the html_output_file into a new file in write mode
    html_resume = open(html_output_file, "w")

    # open the resume_template.html into a new file in read mode
    resume_template = open('resume_template.html', 'r')

    # read the new file into a list
    lines_template = resume_template.readlines()

    # close the file
    resume_template.close()

    # write line #1 to line #31 in the resume_template file into html_resume file
    html_resume.writelines(lines_template [:-2])

    # add tag <div id="page-wrap"> before adding the contect of resume into html_resume
    html_resume.writelines('<div id="page-wrap">\n')

    #add the content of the resume into html_resume
    html_resume.writelines(basic_information_section (txt_name, txt_email))
    html_resume.writelines(projects_section (txt_projects))
    html_resume.writelines(courses_section (txt_courses))

    # add tag </div>, </body>, </html> below the content of reseume into html_resume
    html_resume.writelines('</div>')
    html_resume.writelines(lines_template [-2:])

    # close the file
    html_resume.close()



def main():

    # DO NOT REMOVE OR UPDATE THIS CODE
    # generate resume.html file from provided sample resume.txt
    generate_html('resume.txt', 'resume.html')
    generate_html('resume_FZ.txt', 'resume_FZ.html')

    # DO NOT REMOVE OR UPDATE THIS CODE.
    # Uncomment each call to the generate_html function when you’re ready
    # to test how your program handles each additional test resume.txt file
    generate_html('TestResumes/resume_bad_name_lowercase/resume.txt', 'TestResumes/resume_bad_name_lowercase/resume.html')
    generate_html('TestResumes/resume_courses_w_whitespace/resume.txt', 'TestResumes/resume_courses_w_whitespace/resume.html')
    generate_html('TestResumes/resume_courses_weird_punc/resume.txt', 'TestResumes/resume_courses_weird_punc/resume.html')
    generate_html('TestResumes/resume_projects_w_whitespace/resume.txt', 'TestResumes/resume_projects_w_whitespace/resume.html')
    generate_html('TestResumes/resume_projects_with_blanks/resume.txt', 'TestResumes/resume_projects_with_blanks/resume.html')
    generate_html('TestResumes/resume_template_email_w_whitespace/resume.txt', 'TestResumes/resume_template_email_w_whitespace/resume.html')
    generate_html('TestResumes/resume_wrong_email/resume.txt', 'TestResumes/resume_wrong_email/resume.html')

    # If you want to test additional resume files, call the generate_html function with the given .txt file
    # and desired name of output .html file

if __name__ == '__main__':
    main()