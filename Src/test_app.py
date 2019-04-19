import unittest
import unittest.mock
from mock import patch
import Src.app
import json


with open('fixtures/documents.json', 'r', encoding='utf8') as file:
    documents = json.load(file)


class TestApp(unittest.TestCase):
    def test_document_info(self):
        document_info = Src.app.show_document_info(documents[0])
        self.assertEqual(document_info, 'passport "2207 876234" "Василий Гупкин"')

    def test_adding_a_new_shelf(self):
        Src.app.append_doc_to_shelf('2', '2')
        self.assertEqual(Src.app.directories['2'][-1], '2')

    @unittest.mock.patch('builtins.input', side_effect=['2207 876234'])
    def test_documents_shelf_numbers(self, mock):
        self.assertEqual(Src.app.get_doc_shelf(), '1')

    @unittest.mock.patch('builtins.input', side_effect=['11-2'])
    def test_deletion_of_documents(self, mock):
        Src.app.delete_doc()
        self.assertEqual(len(Src.app.documents), 2)


if __name__ == '__main__':
    unittest.main()
