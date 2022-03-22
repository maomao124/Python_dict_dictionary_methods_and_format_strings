"""
 * Project name(项目名称)：Python_dict字典方法和格式化字符串
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/22 
 * Time(创建时间)： 19:34
 * Version(版本): 1.0
 * Description(描述)： 格式化字符串
 """

if __name__ == '__main__':
    d = {"1": "hello", "2": 23, "3": 5.698}
    print("字符串：%(1)s,  int型：%(2)d,  float型：%(3)f " % d)

    input()
