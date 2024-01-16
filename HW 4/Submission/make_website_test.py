import unittest

from make_website import *

class MakeWebsite_Test(unittest.TestCase):

    def test_reading_file(self):
        # check if the return value of reading_file is a list
        self.assertTrue(type(reading_file('resume.txt')) is list )



    def test_detecting_name(self):

        # compares the name detected from the given list with expectation
        self.assertTrue(detecting_name(['Fan Zhang\n', 'Courses :- CIT591, Investment banking, '
                                                       'Intermediate Accounting\n', 'Projects\n',
                                        'SOX audit - Conduct SOX compliance audit, '
                                        'including entity level controls and operational level control cycles such '
                                        'as Treasury, Human Resources, Asset Management, and Financial Reporting\n'])
                        == 'Fan Zhang')
        self.assertTrue(detecting_name(['fan Zhang\n', 'Courses :- CIT591, Investment banking, '
                                                       'Intermediate Accounting\n', 'Projects\n',
                                        'SOX audit - Conduct SOX compliance audit, '
                                        'including entity level controls and operational level control cycles such '
                                        'as Treasury, Human Resources, Asset Management, and Financial Reporting\n'])
                        == 'Invalid Name')


    def test_detecting_email(self):

        # compares the email detected from the given list with expectation
        self.assertTrue(detecting_email(['Fan Zhang\n', 'Courses :- CIT591, Investment banking, '
                                                       'Intermediate Accounting\n', 'Projects\n',
                                        'SOX audit - Conduct SOX compliance audit, '
                                        'including entity level controls and operational level control cycles such '
                                        'as Treasury, Human Resources, Asset Management, and Financial Reporting\n'])
                        == '')
        self.assertTrue(detecting_email(['Fan Zhang\n', 'Courses :- CIT591, Investment banking, '
                                                       'Intermediate Accounting\n', 'Projects\n',
                                        'fanzp@seas.upenn.edu']) == 'fanzp@seas.upenn.edu')
        self.assertTrue(detecting_email(['Fan Zhang\n', 'Courses :- CIT591, Investment banking, '
                                                       'Intermediate Accounting\n', 'Projects\n',
                                        'fanzp@seas.upenn.com']) == 'fanzp@seas.upenn.com')
        self.assertTrue(detecting_email(['Fan Zhang\n', 'Courses :- CIT591, Investment banking, '
                                                       'Intermediate Accounting\n', 'Projects\n',
                                        'fanzp7@seas.upenn.com']) == '')
        self.assertTrue(detecting_email(['Fan Zhang\n', 'Courses :- CIT591, Investment banking, '
                                                       'Intermediate Accounting\n', 'Projects\n',
                                        'fanzp7@seas7.upenn.com']) == '')

    def test_detecting_courses(self):

        # compares the courses detected from the given list with expectation
        self.assertEqual(False,'-' in detecting_courses(['Courses :- CIT591, Investment banking, '
                                                         'Intermediate Accounting']))
        self.assertEqual(False,',' in detecting_courses(['Courses :- CIT591, Investment banking, '
                                                         'Intermediate Accounting']))
        self.assertEqual(False,':' in detecting_courses(['Courses :- CIT591, Investment banking, '
                                                         'Intermediate Accounting']))
        self.assertTrue(type(detecting_courses(['Courses :- CIT591, Investment banking, '
                                                         'Intermediate Accounting'])) is list)

    def test_detecting_projects(self):

        # compares the projects detected from the given list with expectation
        self.assertListEqual(['project A - content A', 'project B - content B', 'project C - content C'],
                             detecting_projects(['Fan Zhang\n', 'Courses :- CIT591, Investment banking, '
                                                                'Intermediate Accounting\n', 'Projects\n', '\n',
                                                 'project A - content A\n', '\n', 'project B - content B\n', '\n',
                                                 'project C - content C\n', '\n', '------------------------------\n',
                                                 'fanzp@seas.upenn.edu\n']))
        self.assertListEqual(['project A - content A', 'project B - content B'],
                             detecting_projects(['Fan Zhang\n', 'Courses :- CIT591, Investment banking, '
                                                                'Intermediate Accounting\n', 'Projects\n', '\n',
                                                 'project A - content A\n', '\n', 'project B - content B\n', '\n',
                                                  '------------------------------\n', 'project C - content C\n', '\n',
                                                 'fanzp@seas.upenn.edu\n']))



    def test_surround_block(self):

        # test surrounding html
        self.assertEqual(surround_block('h1', 'Eagles'), "<h1>Eagles</h1>")

        # test surrounding html
        self.assertEqual(surround_block('p', 'Lorem ipsum dolor sit amet, consectetur ' +
                                        'adipiscing elit. Sed ac felis sit amet ante porta ' +
                                        'hendrerit at at urna. Donec in vehicula ex. Aenean ' +
                                        'scelerisque accumsan augue, vitae cursus sapien venenatis ' +
                                        'ac. Quisque dui tellus, rutrum hendrerit nisl vitae, ' +
                                        'pretium mollis lorem. Pellentesque eget quam a justo ' +
                                        'egestas vehicula in eu justo. Nulla cursus, metus vitae ' +
                                        'tincidunt luctus, turpis lectus bibendum purus, eget ' +
                                        'consequat est lacus ac nibh. In interdum metus vel est ' +
                                        'posuere aliquet. Maecenas et euismod arcu, eu auctor ' +
                                        'libero. Phasellus lectus magna, auctor ac auctor in, ' +
                                        'suscipit id turpis. Maecenas dignissim enim ac justo ' +
                                        'tincidunt viverra. Sed interdum molestie tincidunt. Etiam ' +
                                        'vitae justo tincidunt, blandit augue id, volutpat ligula. ' +
                                        'Aenean ut aliquet mi. Suspendisse consequat blandit posuere.'),
                                        '<p>Lorem ipsum dolor sit amet, consectetur ' +
                                        'adipiscing elit. Sed ac felis sit amet ante porta ' +
                                        'hendrerit at at urna. Donec in vehicula ex. Aenean ' +
                                        'scelerisque accumsan augue, vitae cursus sapien venenatis ' +
                                        'ac. Quisque dui tellus, rutrum hendrerit nisl vitae, ' +
                                        'pretium mollis lorem. Pellentesque eget quam a justo ' +
                                        'egestas vehicula in eu justo. Nulla cursus, metus vitae ' +
                                        'tincidunt luctus, turpis lectus bibendum purus, eget ' +
                                        'consequat est lacus ac nibh. In interdum metus vel est ' +
                                        'posuere aliquet. Maecenas et euismod arcu, eu auctor ' +
                                        'libero. Phasellus lectus magna, auctor ac auctor in, ' +
                                        'suscipit id turpis. Maecenas dignissim enim ac justo ' +
                                        'tincidunt viverra. Sed interdum molestie tincidunt. Etiam ' +
                                        'vitae justo tincidunt, blandit augue id, volutpat ligula. ' +
                                        'Aenean ut aliquet mi. Suspendisse consequat blandit posuere.</p>')

    def test_create_email_link(self):

        # test created email
        self.assertEqual(
            create_email_link('lbrandon@wharton.upenn.edu'),
            '<a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>')

        # test created email
        self.assertEqual(
            create_email_link('lbrandon.at.wharton.upenn.edu'),
            '<a href="mailto:lbrandon.at.wharton.upenn.edu">lbrandon.at.wharton.upenn.edu</a>')


    def test_basic_information_section(self):

        # compares the result with expectation
        self.assertTrue(
            basic_information_section('Fiona', 'fanzp@seas.upenn.edu') == '''<div>
<h1>Fiona</h1>
<p>Email:<a href="mailto:fanzp@seas.upenn.edu">fanzp[aT]seas.upenn.edu</a></p>
</div>
''')

    def test_projects_section(self):

        # compares the result with expectation
        self.assertEqual(projects_section(['project A - content A', 'project B - content B', 'project C - content C']),
                         '<div>\n<h2>Projects</h2>\n<ul>\n<li>project A - content A</li>\n'
                         '<li>project B - content B</li>\n<li>project C - content C</li>\n</ul>\n</div>\n')


    def test_courses_section(self):
        # compares the result with expectation
        self.assertEqual(courses_section(['Courses :- CIT591, Investment banking, Intermediate Accounting']),
                        '<div>\n<h3>Courses</h3>\n<span>Courses :- CIT591, Investment banking, '
                        'Intermediate Accounting</span>\n</div>\n' )


if __name__ == '__main__':
    unittest.main()



