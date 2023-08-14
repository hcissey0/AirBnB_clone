#!/usr/bin/python3
"""This is the test cases for the base model"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import re
import json
import os
import uuid


class TestBaseModel_Instantiation(unittest.TestCase):
    """This is the unittest TestCase class for the BaseModel class"""

    def test_Instance(self):
        mod = BaseModel()
        self.assertIsInstance(mod, BaseModel)

    def test_two_objs(self):
        bm1 = BaseModel()

        bm2 = BaseModel(**bm1.to_dict())
        self.assertDictEqual(bm1.to_dict(), bm2.to_dict())

    def test_with_one_args(self):
        bm = BaseModel(23)
        self.assertEqual(str(type(bm)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertTrue(issubclass(type(bm), BaseModel))
        self.assertIsInstance(bm, BaseModel)

    def test_with_two_args(self):
        bm = BaseModel(23, "hllo")
        self.assertIsInstance(bm, BaseModel)

    def test_many_args(self):
        arguments = [i for i in range(2000)]
        bm = BaseModel(*arguments)

    def test_with_one_kwargs(self):
        bm = BaseModel(id="hello")
        self.assertIsInstance(bm, BaseModel)

    def test_with_more_kwargs(self):
        bm = BaseModel(name="Hello", id="re",
                       created_at="2017-09-28T21:03:54.052302",
                       updated_at="2018-09-28T21:03:54.052302")
        self.assertIsInstance(bm, BaseModel)

    def test_with_args_and_kwargs(self):
        bm = BaseModel(45, id="34")
        self.assertIsInstance(bm, BaseModel)
        self.assertEqual(bm.id, "34")

    def test_no_args(self):
        bm = BaseModel()
        self.assertEqual(type(bm), BaseModel)

    # Testing the id
    def test_id_is_string(self):
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_id_is_unique(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

        lis = [BaseModel().id for i in range(2000)]
        self.assertEqual(len(lis), len(set(lis)))

    def test_id_list(self):
        bm = BaseModel(id=[])
        self.assertIsInstance(bm.id, list)

    def test_id_int(self):
        bm = BaseModel(id=45)
        self.assertEqual(bm.id, 45)

    def test_id_dictionary(self):
        self.assertEqual(BaseModel(id={"hi": 2}).id, {"hi": 2})

    def test_id_tuple(self):
        self.assertEqual(BaseModel(id=(2, 3)).id, (2, 3))

    def test_id_set(self):
        self.assertEqual(BaseModel(id={2, 3}).id, {2, 3})

    def test_id_float(self):
        self.assertEqual(BaseModel(id=3.3).id, 3.3)

    def test_id_complex(self):
        self.assertEqual(BaseModel(id=complex(2)).id, complex(2))

    def test_id_nan(self):
        import math
        self.assertTrue(math.isnan(BaseModel(id=float('nan')).id))

    def test_id_infinity(self):
        self.assertEqual(BaseModel(id=float('inf')).id, float('inf'))

    def test_id_bool(self):
        self.assertEqual(BaseModel(id=True).id, True)

    def test_id_byte(self):
        self.assertEqual(BaseModel(id=b"hello").id, b"hello")

    def test_id_negative(self):
        self.assertEqual(BaseModel(id=-3).id, -3)

    def test_id_zero(self):
        self.assertEqual(BaseModel(id=0).id, 0)

    def test_id_None(self):
        self.assertEqual(BaseModel(id=None).id, None)

    # Testing the created_at
    def test_created_at_normal_time(self):
        bm = BaseModel(created_at="2017-09-28T21:03:54.052302")
        self.assertIsInstance(bm.created_at, datetime)

    def test_created_at_wrong_wrong_year(self):
        with self.assertRaises(ValueError):
            bm = BaseModel(created_at="0000-09-28T21:03:54.052302")

    def test_created_at_wrong_month(self):
        with self.assertRaises(ValueError):
            bm = BaseModel(created_at="2023-23-28T21:03:54.052302")

    def test_created_at_wrong_day(self):
        with self.assertRaises(ValueError):
            bm = BaseModel(created_at="2020-09-89T21:03:54.052302")

    def test_created_at_wrong_hour(self):
        with self.assertRaises(ValueError):
            bm = BaseModel(created_at="2020-09-23T45:03:54.052302")

    def test_created_at_wrong_minute(self):
        with self.assertRaises(ValueError):
            bm = BaseModel(created_at="2020-09-23T21:78:54.052302")

    def test_created_at_wrong_seconds(self):
        with self.assertRaises(ValueError):
            bm = BaseModel(created_at="2020-09-12T21:03:99.052302")

    def test_created_at_invalid_format(self):
        with self.assertRaises(ValueError):
            bm = BaseModel(created_at="2020 09 23T21:03:54.9")

    def test_created_at_int(self):
        with self.assertRaises(TypeError):
            BaseModel(created_at=8)

    def test_created_at_float(self):
        with self.assertRaises(TypeError):
            BaseModel(created_at=1.1)

    def test_created_at_list(self):
        with self.assertRaises(TypeError):
            BaseModel(created_at=[2])

    def test_created_at_set(self):
        with self.assertRaises(TypeError):
            BaseModel(created_at={3})

    def test_created_at_dictionary(self):
        with self.assertRaises(TypeError):
            BaseModel(created_at={"u": 43})

    def test_created_at_complex(self):
        with self.assertRaises(TypeError):
            BaseModel(created_at=complex(45))

    def test_created_at_nan(self):
        with self.assertRaises(TypeError):
            BaseModel(created_at=float('nan'))

    def test_created_at_innfinity(self):
        with self.assertRaises(TypeError):
            BaseModel(created_at=float('inf'))

    def test_created_at_tuple(self):
        with self.assertRaises(TypeError):
            BaseModel(created_at=(2, 4))

    def test_created_at_bool(self):
        with self.assertRaises(TypeError):
            BaseModel(created_at=True)

    def test_created_at_byte(self):
        with self.assertRaises(TypeError):
            BaseModel(created_at=b"hello")

    def test_created_at_negative(self):
        with self.assertRaises(TypeError):
            BaseModel(created_at=-34)

    def test_created_at_zero(self):
        with self.assertRaises(TypeError):
            BaseModel(created_at=0)

    def test_created_at_None(self):
        with self.assertRaises(TypeError):
            BaseModel(created_at=None)

    # Testing the updated_at
    def test_updated_at_normal_time(self):
        bm = BaseModel(updated_at="2017-09-28T21:03:54.052302")
        self.assertIsInstance(bm.updated_at, datetime)

    def test_updated_at_wrong_wrong_year(self):
        with self.assertRaises(ValueError):
            bm = BaseModel(updated_at="0000-09-28T21:03:54.052302")

    def test_updated_at_wrong_month(self):
        with self.assertRaises(ValueError):
            bm = BaseModel(updated_at="2023-23-28T21:03:54.052302")

    def test_updated_at_wrong_day(self):
        with self.assertRaises(ValueError):
            bm = BaseModel(updated_at="2020-09-89T21:03:54.052302")

    def test_updated_at_wrong_hour(self):
        with self.assertRaises(ValueError):
            bm = BaseModel(updated_at="2020-09-23T45:03:54.052302")

    def test_updated_at_wrong_minute(self):
        with self.assertRaises(ValueError):
            bm = BaseModel(updated_at="2020-09-23T21:78:54.052302")

    def test_updated_at_wrong_seconds(self):
        with self.assertRaises(ValueError):
            bm = BaseModel(updated_at="2020-09-12T21:03:99.052302")

    def test_updated_at_invalid_format(self):
        with self.assertRaises(ValueError):
            bm = BaseModel(updated_at="2020 09 23T21:03:54.9")

    def test_updated_at_int(self):
        with self.assertRaises(TypeError):
            BaseModel(updated_at=8)

    def test_updated_at_float(self):
        with self.assertRaises(TypeError):
            BaseModel(updated_at=1.1)

    def test_updated_at_list(self):
        with self.assertRaises(TypeError):
            BaseModel(updated_at=[2])

    def test_updated_at_set(self):
        with self.assertRaises(TypeError):
            BaseModel(updated_at={3})

    def test_updated_at_dictionary(self):
        with self.assertRaises(TypeError):
            BaseModel(updated_at={"u": 43})

    def test_updated_at_complex(self):
        with self.assertRaises(TypeError):
            BaseModel(updated_at=complex(45))

    def test_updated_at_nan(self):
        with self.assertRaises(TypeError):
            BaseModel(updated_at=float('nan'))

    def test_updated_at_innfinity(self):
        with self.assertRaises(TypeError):
            BaseModel(updated_at=float('inf'))

    def test_updated_at_tuple(self):
        with self.assertRaises(TypeError):
            BaseModel(updated_at=(2, 4))

    def test_updated_at_bool(self):
        with self.assertRaises(TypeError):
            BaseModel(updated_at=True)

    def test_updated_at_byte(self):
        with self.assertRaises(TypeError):
            BaseModel(updated_at=b"hello")

    def test_updated_at_negative(self):
        with self.assertRaises(TypeError):
            BaseModel(updated_at=-34)

    def test_updated_at_zero(self):
        with self.assertRaises(TypeError):
            BaseModel(updated_at=0)

    def test_updated_at_None(self):
        with self.assertRaises(TypeError):
            BaseModel(updated_at=None)


class TestBaseModel_Save(unittest.TestCase):
    """This is the test case for the save function"""

    def setUp(self):
        self.bm = BaseModel()

    def clear_storage(self):
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        self.clear_storage()

    def test_no_args(self):
        self.bm.save()
        with self.assertRaises(TypeError):
            BaseModel.save()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            self.bm.save(34)

    def test_updated_time(self):
        self.bm.save()
        prev_time = datetime.now()
        new_time = self.bm.updated_at
        self.bm.save()
        diff = self.bm.updated_at - datetime.now()
        self.assertTrue(all(isinstance(k, datetime)
                            for k in [prev_time, new_time]))
        self.assertNotEqual(prev_time, new_time)

        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_file_storage(self):
        self.clear_storage()
        bm = BaseModel()
        dictrep = {f"{type(bm).__name__}.{bm.id}":
                   bm.to_dict()}
        bm.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path) as file:
            self.assertEqual(len(json.JSONEncoder().encode(dictrep)),
                             len(file.read()))
            file.seek(0)
            self.assertEqual(len(json.JSONDecoder().decode(file.read())),
                             len(dictrep))


class TestBaseModel_ToDict(unittest.TestCase):
    """This is the test case for the to_dict() function"""

    def test_return_type(self):
        self.assertIsInstance(BaseModel().to_dict(), dict)

    def test_no_args(self):
        bm = BaseModel()
        dic = {"id": f"{bm.id}", "created_at": f"{bm.created_at.isoformat()}",
               "__class__": "BaseModel", "updated_at":
               f"{bm.updated_at.isoformat()}"}
        self.assertDictEqual(dic, bm.to_dict())

    def test_two_objs(self):
        dict1 = BaseModel().to_dict()
        dict2 = BaseModel().to_dict()
        self.assertNotEqual(dict1, dict2)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            BaseModel().to_dict(78)

    def test_dict(self):
        bm = BaseModel()
        bm.first_name = "hello"
        dictrep = bm.to_dict()

        self.assertEqual(dictrep["id"], bm.id)
        self.assertEqual(dictrep["first_name"], bm.first_name)
        self.assertEqual(dictrep["created_at"], bm.created_at.isoformat())
        self.assertEqual(dictrep["updated_at"], bm.updated_at.isoformat())
        self.assertEqual(dictrep["__class__"], type(bm).__name__)

    def test_n_args(self):
        with self.assertRaises(TypeError):
            BaseModel.to_dict()

    def test_create(self):
        dic = {"id": uuid.uuid4,
               "__class__": "BaseModel",
               "updated_at": datetime.now().isoformat(),
               "created_at": datetime.now().isoformat(),
               "name": "kofi",
               "age": 56}
        bm = BaseModel(**dic)
        self.assertDictEqual(dic, bm.to_dict())


class TestBaseModel_Str(unittest.TestCase):
    """This is the test case for the __str__ method"""

    def test_len(self):
        bm = BaseModel()
        self.assertTrue(len(str(bm)) > 1)

    def test_attrs(self):
        import datetime
        bm = BaseModel()
        bm.first_name = "hello"
        strrep = str(bm)
        regex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = regex.match(strrep)
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), bm.id)
        dictrep = dict(eval(str(res.group(3))))
        bmdict = bm.to_dict()

        self.assertEqual(dictrep["created_at"].isoformat(),
                         bmdict["created_at"])
        self.assertEqual(dictrep["updated_at"].isoformat(),
                         bmdict["updated_at"])
        self.assertEqual(dictrep["first_name"],
                         bmdict["first_name"])
        self.assertEqual(dictrep["id"], bmdict["id"])


if __name__ == "__main__":
    unittest.main()
