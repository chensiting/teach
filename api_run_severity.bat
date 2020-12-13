cd  G:/PycharmProjects/teach/testCaseTeach
pytest -sq --alluredir=../report/tmp --allure-severities=normal,critical 
allure generate ../report/tmp -o ../report/report --clean