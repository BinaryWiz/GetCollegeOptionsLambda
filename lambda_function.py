from webdriver_wrapper import WebDriverWrapper


def lambda_handler(event, context):
    driver = WebDriverWrapper()
    colleges = driver.get_niche_data(event['search'])
    driver.close()
    return {'messages': colleges}
