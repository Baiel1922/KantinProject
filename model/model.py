import requests

class Products:
    def __init__(self):
        self.localhost = "http://127.0.0.1:8000/"

    def add_product(self, barcode, name, price):
        data = {}
        data["barcode"] = int(barcode)
        data["name"] = name
        data["price"] = int(price)
        url_products = self.localhost + "products/"
        responce = requests.post(url_products, data)
        if responce:
            answer = True
        else:
            answer = False
        return answer


    def get_all_products(self):
        url_products = self.localhost + "products/"
        responce = requests.get(url_products)
        json_data = responce.json()
        return json_data

    def get_product(self, barcode):
        if barcode:
            url_product = self.localhost + "products/" + barcode
            responce = requests.get(url_product)
            json_data = responce.json()
            return json_data
        else:
            return

    def delete_product(self, barcode):
        print(barcode)
        url_product = self.localhost + "products/" + barcode
        responce = requests.delete(url_product,)
        # print(responce)
        if responce:
            answer = True
        else:
            answer = False
        return answer



class Students():
    def __int__(self):
        pass

    def get_student(self, id_student):
        url_student = "http://127.0.0.1:8000/" + "students/" + id_student + "/"
        responce = requests.get(url_student)
        json_data = responce.json()
        return json_data

    def substract_cash(self, id_student, money):
        url_student = "http://127.0.0.1:8000/" + "students/" + id_student + "/"
        try:
            responce = requests.get(url_student)
            json_data = responce.json()
            old_amount = json_data["cash"]

            new_amount = old_amount - int(money)
            if new_amount > 0:
                json_data["cash"] = new_amount
                print(json_data)
                responce2 = requests.patch(url_student, data=json_data)
                print(responce2)
                if responce2:
                    answer = "Success!"
                else:
                    answer = "Something went wrong!"
            else:
                answer = "Not enough money!"
        except:
            answer = "Student's id not found!"

        return answer


obj = Students()
# print(obj.substract_cash("208715002", 50))



















