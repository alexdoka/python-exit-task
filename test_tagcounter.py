import unittest

import tagcounter


class TestCalc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("synonims.yaml", "a") as file_object:
            file_object.write("\ntricky: supertrickysite.com\n")

    @classmethod
    def tearDownClass(cls):
        def delete_last_strings(filename, number_last_lines):
            fd = open(filename, "r")
            d = fd.read()
            fd.close()
            m = d.split("\n")
            s = "\n".join(m[:-int(number_last_lines)])
            fd = open(filename, "w")
            for i in range(len(s)):
                fd.write(s[i])
            fd.close()

        delete_last_strings("synonims.yaml", 2)
        delete_last_strings("tags_log_file", 1)

    def test_get_url_site(self):
        self.assertEqual(tagcounter.get_url_site('google.com'), 'https://google.com/')

    def test_define_site_name(self):
        self.assertEqual(tagcounter.define_site_name('tricky'), 'supertrickysite.com')
        self.assertEqual(tagcounter.define_site_name('megasite.com'), 'megasite.com')

    def test_get_dict_tags(self):
        self.assertEqual(tagcounter.get_dict_tags('<html><a><a><a test="string"><body>'),
                         {'html': 1, 'a': 3, 'body': 1})

    def test_write_to_logfile(self):
        tagcounter.write_to_logfile("supertest.com", "tags_log_file")
        with open("tags_log_file", "r") as file_object:
            result = False
            for ln in file_object:
                if "supertest.com" in ln:
                    result = True
                    break
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
