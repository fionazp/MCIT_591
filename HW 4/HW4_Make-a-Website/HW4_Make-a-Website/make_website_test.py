import unittest

from make_website import *

class MakeWebsite_Test(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()
