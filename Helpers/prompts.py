
def prompt_tcs_expert(excel_req: str) -> list:

    message = [
        {
            "role": "system",
            "content": "You are a veteran well seasoned test case creator expert"
        },
        {
            "role": "user",
            "content":     f"""    
        You have been given a set of requirements from a client to create concrete well refined test cases 
        ready for execution. You will be provided with the requirement in this message content found under Requirements.
        Format of each received requirements is dictionary like format like a:1, b:2, c:3 and so on.
        
        Prioritize accuracy, clear test case visibility and testing practicability as these test cases will go straight 
        to a tester for minimal interaction.
        These test cases will be going under production and will be executed on a regular basis and your response is very
        important in this regard. Your response might also be reviewed by our clients and that implies your higher consideration.
        
        
        Requirements: {excel_req}
        
        TBFBT = TO BE FILLED BY TESTER - leave it empty and specify in the field that requires tester interaction
        
        Your output format should look like easy to read list exactly ordered as it is listed and fill every sections where 
        TBFBT is not present: 
        Test Case ID, Test Case Title, Test Case Description, Module/Component, Release Version, 
        Complexity Level, Project Name, Priority (TBFBT), Severity, Risk Level, 
        Test Case Automation Percentage(100% = totally automated process) (TBFBT), Test Case Automation Description (TBFBT)
        Testing Environment, Test Case Precondition, Test Case Assumptions, Test Case Required Tools
        Test Case Required Licenses (TBFBT), Test Case Steps to Perform, Test Case Postcondition Steps, 
        Test Case Cleanup Steps, Test Case Before Run Exceptions (TBFBT), Test Case After Run Exceptions (TBFBT), 
        Test Case Expected Result,  Test Case Actual Result (TBFBT), Pass/Fail Status (TBFBT), 
        Validation Method (CI/CD, Manual, Unittests), Test Case Related Defect ID (TBFBT),
        
        Mandatory for task completion would be the following: Your response should consist only of a python like format
        dictionary with the above mentioned fields. Make sure no other extra introduction or explanation is added. 
        It is also mandatory to remove emojis and any special characters that are against UTF-8

        Your task is finished when you have completed all the fields for each requirement enquired and made sure 
        that TBFBT tag fields have the note 'Field requires tester interaction'. 
        Set your own numbering for Test Case ID field.
        """
        }
    ]

    return message


def prompt_test() -> str:
    return f"""
    This is a test to check if the model responds back, my query is hello and you should 
    respond back with hello optimizing performance aiming to respond ASAP with no emoji, 
    no special characters just plain text.
    """
