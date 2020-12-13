cd  G:/PycharmProjects/teach/testCaseTeach
pytest -sq --alluredir=../report/tmp
allure generate ../report/tmp -o ../report/report --clean