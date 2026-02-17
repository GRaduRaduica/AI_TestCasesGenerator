from helpers.excelreader import ExcelReader
from helpers.json_helper import JsonWorker
from static_data import Constants_API
from helpers.file_dir_finder import *
from helpers.prompts import *
from helpers.LogHandler import LogStorageHandler, LogLevel
from json import loads

EXCEL_PATH = find_file("dummy_sample.xlsx")
JSON_PATH = find_dir('json_output') / "tcs.json"
LOG_FILE = find_dir('logs') / 'main_logs.log'


# TODO: add guardrails for model responses
class MainController:
    """
    Main controlling point for collecting all information and sending it to AI
    Make sure that \\AI_TestCasesGenerator\\excel_input\\.xlsx file is filled in with your tc requirements
    """

    def __init__(self, excelobj=None):
        self.logging = LogStorageHandler(logfile=LOG_FILE, maxBytes=4096)
        self.excel_obj = excelobj
        self.json_obj = None
        self.api_key = Constants_API.api_key
        self.client = self.__choose_available_interface()
        if not self.excel_obj:
            self.excel_obj = ExcelReader(EXCEL_PATH)
        self.message: str = self.excel_obj.remove_duplicates()

    def __choose_available_interface(self):
        """
        :return: returns the chosen interface
        """
        for model_options in Constants_API.list_of_interfaces:
            try:
                result = model_options.chat.completions.create(
                    messages=[{"role": "user", "content": prompt_test()}]
                )

                if result.choices[0].message.content:
                    return model_options

            except Exception as e:
                self.logging.set_level(LogLevel.ERROR)
                self.logging.error(f"Model failed with error message: {e}")
                print(f"Model failed with error message: {e}")
        return None

    def __ai_request(self, msg: str) -> str | None:
        """
        Requiring AI to respond to the enquiry
        :return: AI response (str) or None
        """
        try:
            result = self.client.chat.completions.create(
                messages=prompt_tcs_expert(msg)
            )

            response = result.choices[0].message.content

            if response:
                return response

        except Exception as e:
            self.logging.set_level(LogLevel.ERROR)
            self.logging.error(f"Model failed with error message: {e}")
            print(f"Model failed with error message: {e}")
        return None

    def write_json(self):
        """
        TODO : make json file names unique / avoid overwriting
        """
        self.json_obj = JsonWorker(JSON_PATH)
        self.logging.set_level(LogLevel.INFO)
        self.logging.info("Writing json file...")
        refined_response = loads(self.__ai_request(self.message))
        self.json_obj.write_json(refined_response)


if __name__ == '__main__':
    # test_proxy()
    ai_obj = MainController()
    ai_obj.write_json()
