# xpath定位详解

## **1.xpath高级用法基础格式**
* **格式**  
/轴方法::标签名[标签属性]
* **实例**  
//div/parent::span[@name=‘interName’]
* **实例解释：**  
定位span标签，span标签是div标签的父级，且span标签的name属性值为：interlNmae  
         
## **2.基础格式详解**
* **层级**

| 表达式 | 描述 |
| :------| :------: |
| / | 从根节点选取(绝对路径) |
| // | 选取匹配的节点 |
| . | 选取当前节点 |
| .. | 选取当前节点的上级节点 |
| &#124; | 并且 |
| ----------------- | ------------------------- |

* 路径实例

| 表达式 | 描述 |
| :------| :------: |
| /div | 从根节点选取div标签 |
| //div | 选取所有div标签 |
| //div/.. | 选取div标签的上级标签 |
| list/tr | 选取所有父级为list的tr标签 |
| list//tr | 选取list标签节点内的所有tr标签 |
| /div/span &#124; /div/input | 选取div标签下的span和div标签下的input |

* **标签位置以及标签属性方法**

| 表达式 | 描述 |
| :------| :------: |
| * | 选取任意的节点 |
| @ | 选取标签本身的属性 |
| @* | 选取带有任何属性的节点 |
| last() | 选取当前层级的最后一个标签 |
| position() | 选取当前层级中标签的具体位置定位 |
| contains(text(),'') | 选取标签内容包含匹配文本的节点 |
| starts-with() | 选取标签属性值开始字段匹配 |
| ~~ends-with()~~ | ~~选取标签属性值结束字段匹配~~ |
| ----------------- | ------------------------- |
| attribute | 等同于@，属于xpath方法 |

* 标签位置及属性方法实例

| 表达式 | 描述 |
| :------| :------: |
| /div/span[2] | 选取div标签下第二个span标签 |
| /table/* | 选取table标签下所有子节点 |
| /input[@id='userName'] | 选取所有id属性值为：userName的input标签 |
| /list[@*] | 选取所有带属性的list标签 |
| /span[last()-1] | 选取当前层级的倒数第二个span标签 |
| /li/div[position()<3] | 选取li标签下前两个div元素 |
| /input[contains(text(),'密码')] | 选取节点中内容包含：密码的input标签 |
| //input[contains(@id,'Name')] | 选取标签中id属性包含Name的input的标签 |
| /div[starts-with(@*,'na')] | 选取标签中任意属性值以na开始的div标签 |
| /div[ends-with(text(),'名')] | ~~选取节点中内容以‘名’结尾的div标签~~ |

* **xpath轴方法**

| 表达式 | 描述 |
| :------| :------: |
| parent | 选取当前节点的父节点。 |
| **ancestor** | 选取当前节点的所有前辈 |
| child | 选取当前节点内的所有子标签 |
| descendant | 选取当前节点内的所有后代 |
| **following** | 选取当前html页面，这个节点结束标签之后的所有节点 |
| **preceding** | 选取当前html页面，这个节点结束标签之前的所有节点 |
| **following-sibling** | 选取当前节点之后的所有同级节点 |
| **preceding-sibling** | 选取当前节点之前的所有同级节点 |

* xpath轴方法的实例

| 表达式 | 描述 |
| :------| :------: |
| /parent::div | 选取当前节点的div父标签。 |
| /ancestor::div | 选取当前节点之上的所有div标签(父、祖父节点) |
| /td/child::tr | 选取td标签下的所有tr子标签 |
| /td/descendant::tr | 选取td标签内的所有tr标签(不限层级) |
| /table/following::* | 选取当前html页面，table标签结束之后的所有标签(无视层级) |
| /table/preceding ::*| 选取当前html页面，table标签之前的所有标签(无视层级) |
| /div/following-sibling::div | 选取div标签之后的所有同级div标签 |
| /div/preceding-sibling::div | 选取当前节点之前的所有同级div标签 |

* **常用运算符**

| 表达式 | 示例 |
| :------| :------: |
| and | /input[@id='name' and @weight='10'] |
| or | /input[@id='name' or @weight='10'] |
| = | /input[@name='test'] |
| != | /ipnut[@name!='test'] |

* 附录：一些等价的写法

| 建议书写表达式 | 等价表达式 |
| :------| :------: |
| /input[@name='test'] | /input[attribute::name='text'] |
| /a[5] | /a[position()=5] |
| div/.. | div/parent::span |
| /table//tr | /table//descendant::tr |
| /tr/td | tr/child::td |


## **3.实例演示以及问题总结**

* 常见试用方法：  
* 1.输入框常用定位：  
  
     有时候经常遇到输入框很多，也没有唯一标识例如id等，chrome复制的xpath非常的长，而且容易失效，但是如果根据输入框前的字段名称来作为标识，那定位就比较稳定了。  
        
     例如：商品挂牌页面，船名输入框，通过字段名称：船名来匹配查找对应的输入框。  
xpath=//label[contains(text(),'船名')]/following-sibling::div/span/div/input  

     例如：商品挂牌页面，大类单选项。  
xpath=//span[contains(text(),'铁矿')]/preceding-sibling::span/input

* 2.常见问题：  
  * parent定位父級，还是包含父级、伯父級等    
    parent只定位到父级  

  *  符合xpath路径的元素有多个，此时driver如何判断对哪一个元素进行操作呢    
    find_element方法中，如果符合路径的元素有多个，默认取第一个元素    
  
  * contains(text(),''要查找的文字')，定位时只能定位当前层级中的文本  
  
  * Unable to locate element  
    方法1：加入time.sleep() （ui自动化中操作过快会多导致无法定位到元素） 
    方法2：加入显示等待：WebDriverWait、expected_conditions  
    方法3：可能是由于操作导致层级结构改变，重新排查定位元素路径  
    方法4：可能是页面中包含frame嵌套，加入switch_to.frame    
    
  * Element is not currently visible and may not be manipulated exception
    方法1：下拉框没有成功选择数据，此时对于下拉框的定位取消显式等待  
   
  * unexpected EOF while parsing  
    方法1：运行报错，检查是否是class中函数格式是否正确  
    
    













