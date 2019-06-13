import unittest
import name_sorter


class TestSorter(unittest.TestCase):
    #1
    def test_Last_To_First_Name_1_given_name(self):
        data = "Selle Bellison"
        result = name_sorter.Last_To_First_Name(data)
        expected_result = "Bellison Selle"
        self.assertEqual(result, expected_result)
    
    #2
    def test_Last_To_First_Name_2_given_name(self):   
        data = "Orson Milka Iddins"
        result = name_sorter.Last_To_First_Name(data)
        expected_result = "Iddins Orson Milka"
        self.assertEqual(result, expected_result)

    #3
    def test_Last_To_First_Name_3_given_name(self):
        data = "Leonerd Adda Mitchell Monaghan"
        result = name_sorter.Last_To_First_Name(data)
        expected_result = "Monaghan Leonerd Adda Mitchell"
        self.assertEqual(result, expected_result)

    #4
    def test_First_To_Last_Name_1_given_name(self):
        data = "Debra Micheli"
        result = name_sorter.First_To_Last_Name(data)
        expected_result = "Micheli Debra"
        self.assertEqual(result, expected_result)

    #5
    def test_First_To_Last_Name_2_given_name(self):
        data = "Battelle Erna Dorey"
        result = name_sorter.First_To_Last_Name(data)
        expected_result = "Erna Dorey Battelle"
        self.assertEqual(result, expected_result)

    #6
    def test_First_To_Last_Name_3_given_name(self):
        data = "Dovahkiin Roy Ketti Kopfen"
        result = name_sorter.First_To_Last_Name(data)
        expected_result = "Roy Ketti Kopfen Dovahkiin"
        self.assertEqual(result, expected_result)

    #7
    def test_Sort_Name_simple(self):
        data = ["Orson Milka Iddins", "Erna Dorey Battelle", "Flori Chaunce Franzel", "Odetta Sue Kaspar", "Roy Ketti Kopfen", "Madel Bordie Mapplebeck", "Selle Bellison", "Leonerd Adda Mitchell Monaghan", "Debra Micheli", "Hailey Avie Annakin"]
        result = name_sorter.Sort_Name(data)
        expected_result = ['Hailey Avie Annakin', 'Erna Dorey Battelle', 'Selle Bellison', 'Flori Chaunce Franzel', 'Orson Milka Iddins', 'Odetta Sue Kaspar', 'Roy Ketti Kopfen', 'Madel Bordie Mapplebeck', 'Debra Micheli', 'Leonerd Adda Mitchell Monaghan']
        self.assertEqual(result, expected_result)

    #8
    def test_Sort_Name_random_shorted_name(self):
        data = ["O. Milka Iddins", "Erna D. Battelle", "Flori Chaunce F.", "O. S. Kaspar", "R. Ketti K.", "M. B. M.", "Selle Bellison", "Leonerd A. M. Monaghan", "Debra M.", "Hailey Avie Annakin"]
        result = name_sorter.Sort_Name(data)
        expected_result = ['Hailey Avie Annakin', 'Erna D. Battelle', 'Selle Bellison', 'Flori Chaunce F.', 'O. Milka Iddins', 'R. Ketti K.', 'O. S. Kaspar', 'Debra M.', 'M. B. M.', 'Leonerd A. M. Monaghan']
        self.assertEqual(result, expected_result)

    #9
    def test_Sort_Name_all_lower(self):
        data = ["orson milka iddins", "erna dorey battelle", "flori chaunce franzel", "odetta sue kaspar", "roy ketti kopfen", "madel bordie mapplebeck", "selle bellison", "leonerd adda mitchell monaghan", "debra micheli", "hailey avie annakin"]
        result = name_sorter.Sort_Name(data)
        expected_result = ['Hailey Avie Annakin', 'Erna Dorey Battelle', 'Selle Bellison', 'Flori Chaunce Franzel', 'Orson Milka Iddins', 'Odetta Sue Kaspar', 'Roy Ketti Kopfen', 'Madel Bordie Mapplebeck', 'Debra Micheli', 'Leonerd Adda Mitchell Monaghan']
        self.assertEqual(result, expected_result)

    #10
    def test_Sort_Name_all_upper(self):
        data = ['ORSON MILKA IDDINS', 'ERNA DOREY BATTELLE', 'FLORI CHAUNCE FRANZEL', 'ODETTA SUE KASPAR', 'ROY KETTI KOPFEN', 'MADEL BORDIE MAPPLEBECK', 'SELLE BELLISON', 'LEONERD ADDA MITCHELL MONAGHAN', 'DEBRA MICHELI', 'HAILEY AVIE ANNAKIN']
        result = name_sorter.Sort_Name(data)
        expected_result = ['Hailey Avie Annakin', 'Erna Dorey Battelle', 'Selle Bellison', 'Flori Chaunce Franzel', 'Orson Milka Iddins', 'Odetta Sue Kaspar', 'Roy Ketti Kopfen', 'Madel Bordie Mapplebeck', 'Debra Micheli', 'Leonerd Adda Mitchell Monaghan']
        self.assertEqual(result, expected_result)

    #11
    def test_Sort_Name_random_lower_upper(self):
        data = ["Orson milka iddins", "erna Dorey battelle", "flori chaunce Franzel", "odeTta SUe KasPar", "RoY KETTI KoPfen", "MadeL BordiE MapplebecK", "Selle bellisoN", "Leonerd adda mitcheLL monaghan", "Debra Micheli", "HAIley avie annakin"]
        result = name_sorter.Sort_Name(data)
        expected_result = ['Hailey Avie Annakin', 'Erna Dorey Battelle', 'Selle Bellison', 'Flori Chaunce Franzel', 'Orson Milka Iddins', 'Odetta Sue Kaspar', 'Roy Ketti Kopfen', 'Madel Bordie Mapplebeck', 'Debra Micheli', 'Leonerd Adda Mitchell Monaghan']
        self.assertEqual(result, expected_result)

    #12
    def test_Sort_Name_all_same_last_name(self):
        data = ["Orson Milka Iddins", "Erna Dorey Iddins", "Flori Chaunce Iddins", "Odetta Sue Iddins", "Roy Ketti Iddins", "Madel Bordie Iddins", "Selle Iddins", "Leonerd Adda Mitchell Iddins", "Debra Iddins", "Hailey Avie Iddins"]
        result = name_sorter.Sort_Name(data)
        expected_result = ['Debra Iddins', 'Erna Dorey Iddins', 'Flori Chaunce Iddins', 'Hailey Avie Iddins', 'Leonerd Adda Mitchell Iddins', 'Madel Bordie Iddins', 'Odetta Sue Iddins', 'Orson Milka Iddins', 'Roy Ketti Iddins', 'Selle Iddins']
        self.assertEqual(result, expected_result)

    #13
    def test_Sort_Name_all_same_shorted_last_name(self):
        data = ["Orson Milka I.", "Erna Dorey I.", "Flori Chaunce I.", "Odetta Sue I.", "Roy Ketti I.", "Madel Bordie I.", "Selle I.", "Leonerd Adda Mitchell I.", "Debra I.", "Hailey Avie I."]
        result = name_sorter.Sort_Name(data)
        expected_result = ['Debra I.', 'Erna Dorey I.', 'Flori Chaunce I.', 'Hailey Avie I.', 'Leonerd Adda Mitchell I.', 'Madel Bordie I.', 'Odetta Sue I.', 'Orson Milka I.', 'Roy Ketti I.', 'Selle I.']
        self.assertEqual(result, expected_result)

    #14
    def test_Sort_Name_all_same_1_given_name(self):
        data = ["Orson Iddins", "Orson Battelle", "Orson Franzel", "Orson Kaspar", "Orson Kopfen", "Orson Mapplebeck", "Orson Bellison", "Orson Monaghan", "Orson Micheli", "Orson Annakin"]
        result = name_sorter.Sort_Name(data)
        expected_result = ['Orson Annakin', 'Orson Battelle', 'Orson Bellison', 'Orson Franzel', 'Orson Iddins', 'Orson Kaspar', 'Orson Kopfen', 'Orson Mapplebeck', 'Orson Micheli', 'Orson Monaghan']
        self.assertEqual(result, expected_result)

    #15
    def test_Sort_Name_all_same_shorted_1_given_name(self):
        data = ["Orson Iddins", "Orson Battelle", "Orson Franzel", "Orson Kaspar", "Orson Kopfen", "Orson Mapplebeck", "Orson Bellison", "Orson Monaghan", "Orson Micheli", "Orson Annakin"]
        result = name_sorter.Sort_Name(data)
        expected_result = ['Orson Annakin', 'Orson Battelle', 'Orson Bellison', 'Orson Franzel', 'Orson Iddins', 'Orson Kaspar', 'Orson Kopfen', 'Orson Mapplebeck', 'Orson Micheli', 'Orson Monaghan']
        self.assertEqual(result, expected_result)

    #16
    def test_Sort_Name_all_same_2_given_name(self):
        data = ["Orson Milka Iddins", "Orson Milka Battelle", "Orson Milka Franzel", "Orson Milka Kaspar", "Orson Milka Kopfen", "Orson Milka Mapplebeck", "Orson Milka Bellison", "Orson Milka Monaghan", "Orson Milka Micheli", "Orson Milka Annakin"]
        result = name_sorter.Sort_Name(data)
        expected_result = ['Orson Milka Annakin', 'Orson Milka Battelle', 'Orson Milka Bellison', 'Orson Milka Franzel', 'Orson Milka Iddins', 'Orson Milka Kaspar', 'Orson Milka Kopfen', 'Orson Milka Mapplebeck', 'Orson Milka Micheli', 'Orson Milka Monaghan']
        self.assertEqual(result, expected_result)

    #17
    def test_Sort_Name_all_same_shorted_2_given_name(self):
        data = ["O. M. Iddins", "O. M. Battelle", "O. M. Franzel", "O. M. Kaspar", "O. M. Kopfen", "O. M. Mapplebeck", "O. M. Bellison", "O. M. Monaghan", "O. M. Micheli", "O. M. Annakin"]
        result = name_sorter.Sort_Name(data)
        expected_result = ['O. M. Annakin', 'O. M. Battelle', 'O. M. Bellison', 'O. M. Franzel', 'O. M. Iddins', 'O. M. Kaspar', 'O. M. Kopfen', 'O. M. Mapplebeck', 'O. M. Micheli', 'O. M. Monaghan']
        self.assertEqual(result, expected_result)

    #18
    def test_Sort_Name_all_same_3_given_name(self):
        data = ["Leonerd Adda Mitchell Iddins", "Leonerd Adda Mitchell Battelle", "Leonerd Adda Mitchell Franzel", "Leonerd Adda Mitchell Kaspar", "Leonerd Adda Mitchell Kopfen", "Leonerd Adda Mitchell Mapplebeck", "Leonerd Adda Mitchell Bellison", "Leonerd Adda Mitchell Monaghan", "Leonerd Adda Mitchell Micheli", "Leonerd Adda Mitchell Annakin"]
        result = name_sorter.Sort_Name(data)
        expected_result = ['Leonerd Adda Mitchell Annakin', 'Leonerd Adda Mitchell Battelle', 'Leonerd Adda Mitchell Bellison', 'Leonerd Adda Mitchell Franzel', 'Leonerd Adda Mitchell Iddins', 'Leonerd Adda Mitchell Kaspar', 'Leonerd Adda Mitchell Kopfen', 'Leonerd Adda Mitchell Mapplebeck', 'Leonerd Adda Mitchell Micheli', 'Leonerd Adda Mitchell Monaghan']
        self.assertEqual(result, expected_result)

    #19
    def test_Sort_Name_all_same_shorted_3_given_name(self):
        data = ["L. A. M. Iddins", "L. A. M. Battelle", "L. A. M. Franzel", "L. A. M. Kaspar", "L. A. M. Kopfen", "L. A. M. Mapplebeck", "L. A. M. Bellison", "L. A. M. Monaghan", "L. A. M. Micheli", "L. A. M. Annakin"]
        result = name_sorter.Sort_Name(data)
        expected_result = ['L. A. M. Annakin', 'L. A. M. Battelle', 'L. A. M. Bellison', 'L. A. M. Franzel', 'L. A. M. Iddins', 'L. A. M. Kaspar', 'L. A. M. Kopfen', 'L. A. M. Mapplebeck', 'L. A. M. Micheli', 'L. A. M. Monaghan']
        self.assertEqual(result, expected_result)

    #20
    def test_Captalize_First_Letter_In_Name_all_lower(self):
        data = ["orson milka iddins", "erna dorey battelle", "flori chaunce franzel", "odetta sue kaspar", "roy ketti kopfen", "madel bordie mapplebeck", "selle bellison", "leonerd adda mitchell monaghan", "debra micheli", "hailey avie annakin"]
        result = name_sorter.Sort_Name(data)
        expected_result = ['Hailey Avie Annakin', 'Erna Dorey Battelle', 'Selle Bellison', 'Flori Chaunce Franzel', 'Orson Milka Iddins', 'Odetta Sue Kaspar', 'Roy Ketti Kopfen', 'Madel Bordie Mapplebeck', 'Debra Micheli', 'Leonerd Adda Mitchell Monaghan']
        self.assertEqual(result, expected_result)

    #21
    def test_Captalize_First_Letter_In_Name_all_upper(self):
        data = ['ORSON MILKA IDDINS', 'ERNA DOREY BATTELLE', 'FLORI CHAUNCE FRANZEL', 'ODETTA SUE KASPAR', 'ROY KETTI KOPFEN', 'MADEL BORDIE MAPPLEBECK', 'SELLE BELLISON', 'LEONERD ADDA MITCHELL MONAGHAN', 'DEBRA MICHELI', 'HAILEY AVIE ANNAKIN']
        result = name_sorter.Sort_Name(data)
        expected_result = ['Hailey Avie Annakin', 'Erna Dorey Battelle', 'Selle Bellison', 'Flori Chaunce Franzel', 'Orson Milka Iddins', 'Odetta Sue Kaspar', 'Roy Ketti Kopfen', 'Madel Bordie Mapplebeck', 'Debra Micheli', 'Leonerd Adda Mitchell Monaghan']
        self.assertEqual(result, expected_result)

    #22
    def test_Captalize_First_Letter_In_Name_random_lower_upper(self):
        data = ["Orson milka iddins", "erna Dorey battelle", "flori chaunce Franzel", "odeTta SUe KasPar", "RoY KETTI KoPfen", "MadeL BordiE MapplebecK", "Selle bellisoN", "Leonerd adda mitcheLL monaghan", "Debra Micheli", "HAIley avie annakin"]
        result = name_sorter.Sort_Name(data)
        expected_result = ['Hailey Avie Annakin', 'Erna Dorey Battelle', 'Selle Bellison', 'Flori Chaunce Franzel', 'Orson Milka Iddins', 'Odetta Sue Kaspar', 'Roy Ketti Kopfen', 'Madel Bordie Mapplebeck', 'Debra Micheli', 'Leonerd Adda Mitchell Monaghan']
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()