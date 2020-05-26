QA自动化

### 安装依赖库：
在当前项目目录下，运行命令：  
pip install -r requirements.txt

### 更新依赖库：
1. 首先安装pipreqs库：  
pip install pipreqs
2. 在当前项目目录下运行  
pipreqs ./ --encoding=utf-8  
成功会显示：INFO: Successfully saved requirements file in ./requirements.txt


### 层级结构
* **common**：存储一些封装起来的基础方法，以供随时调用，比如日志模块（log.py）、读取数据模块（loadExcel.py、loadyaml.py）、发送邮件模块（sendmail）等
* **config**：存储一些基础的配置参数，比如邮件联系人等
* **data**：        存储测试数据，以excel文件等形式保存
* **run_all**：  运行测试用例的入口，通过这个入口配置运行哪些case
* **test_case**：存储测试用例集
* **log**：存储测试日志，运行程序后自动生成
* **report**： 存储测试报告，运行程序后自动生成

### 框架介绍
本框架运用requests+unittest框架，搭建的接口测试平台，实现了底层方法模块化、运行用例流程化、数据代码分离化、测试报告可视化的构想。通过这套框架可以轻松的编写接口用例并执行，你只需要将测试数据写入excel表格，并在用例中：取值-发送接口请求-断言判断即可，随后的测试结果可以参看测试报告以及日志文件。

### 运行所需package
##### 添加方法：pycharm-setting-project Interpreter，点击+号搜索package名称后添加库
* pyyaml 读取yaml文件
* ddt 循环遍历测试数据
* xlrd 读取excel
* selenium 调用控制浏览器和网页
* pymysql 链接数据库
* pillow 支持python3的图片截图库

### 获取webdriver
http://chromedriver.storage.googleapis.com/index.html

## Google Python命名规范
module_name,  模块
package_name,  包
ClassName,  类
method_name,  方法
ExceptionName,   异常
function_name,  函数
GLOBAL_VAR_NAME, 全局变量
instance_var_name,  实例
function_parameter_name,   参数
local_var_name.  本变量

