from rest_framework.test import APITestCase
from . import models


# class TestSubjects(APITestCase):
#     NAME = "Subject Test"
#     DESC = "Subject Des"

#     def setUp(self):
#         models.Subject.objects.create(
#             name=self.NAME,
#             description=self.DESC,
#         )

#     def test_all_subjects(self):
#         response = self.client.get("/api/v1/subjects/")
#         data = response.json()

#         self.assertEqual(
#             response.status_code,
#             200,
#             "Status code isn't 200.",
#         )
#         self.assertIsInstance(
#             data,
#             list,
#         )
#         self.assertEqual(
#             len(data),
#             1,
#         )
#         self.assertEqual(
#             data[0]["name"],
#             self.NAME,
#         )
#         self.assertEqual(
#             data[0]["description"],
#             self.DESC,
#         )


from rest_framework import status


# class TestSubjects(APITestCase):
#     def test_create_subject_with_valid_data(self):
#         data = {
#             "name": "Valid Subject",
#             "description": "Valid Description",
#         }
#         response = self.client.post("/api/v1/subjects/", data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_create_subject_with_missing_data(self):
#         data = {}
#         response = self.client.post("/api/v1/subjects/", data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_create_subject_with_invalid_data(self):
#         data = {
#             "name": "",
#             "description": "Valid Description",
#         }
#         response = self.client.post("/api/v1/subjects/", data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestSubjectsValidation(APITestCase):
    def test_create_subject_with_empty_name(self):
        data = {
            "name": "",
            "description": "Vaild DESC",
        }
        response = self.client.post("/api/v1/subjects/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_subject_with_missing_description(self):
        data = {
            "name": "Valid Name",
        }
        response = self.client.post("/api/v1/subjects/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_subject_with_name_too_long(self):
        data = {
            "name": "A" * 101,
            "description": "Valid DESC",
        }
        response = self.client.post("/api/v1/subjects/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
