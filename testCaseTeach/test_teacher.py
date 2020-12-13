#time:2020-11-28
from Lib.ApiLogin import LoginClass
from Lib.ApiLesson import LessonClass
import json,pytest,allure
from Lib.GetExcelData import get_excelData

class TestLesson: #测试用例类
    def test_add_lesson(self,inData,repsData):
        res = LessonClass().addcourse(self.session,inData)
        assert json.loads(res)["retcode"] == json.loads(repsData)["retcode"]
