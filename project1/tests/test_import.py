from package.unittest import *

class TestImport(TestCase):
    def test_import(self):
        import project1

        self.assertTrue(True, 'project1 module imported cleanly')

if __name__ == '__main__':
    main()
