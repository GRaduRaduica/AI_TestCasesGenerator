from Helpers.excel_reader import Excel_Reader
from Helpers.json_helper import Json_Worker
from network_sanity_test_requests import *
from Constants import Constants_API
from file_dir_finder import *

excel_location = find_file("dummy_sample.xlsx")
json_saving_path = find_dir('json_saves')


class MainController:
    """
    Main controlling point for collecting all information and sending it to CoPilot AI
    """
    def __init__(self):
        self.api_key = Constants_API.api_key

        # self.proxies = proxies

        self.client = Constants_API.list_of_interfaces[4]
        if excel_location is not None:
            self.excel_obj = Excel_Reader(excel_location)
        if json_saving_path is not None:
            self.json_obj = Json_Worker(save_loc='', dict_data=self.convert_to_dict())
        self.message = self.excel_obj.remove_duplicates()


    def chat_with_ai(self):
        """
        Requiring AI to respond to the enquiry
        :return: AI response (str) or None
        """
        result = self.client.chat.completions.create(
        # model="deepseek-ai/DeepSeek-R1-0528",
        messages=[
            {
                "role": "user",
                "content": f"{self.message}"
            }
        ]
        )

        response = result.choices[0].message.content
        if response and len(response) > 0:
            return response
        return None

    def convert_to_dict(self) -> dict:
        """
        :return: converts the extracted data from excel to dictionary type
        """
        pass


if __name__ == '__main__':
    # test_proxy()
    ai_obj = MainController()
    print(ai_obj.chat_with_ai())
    # ai_obj.json_obj.write_json()