# KSOA-SQL-INJECT
Unauthenticated attackers can use this vulnerability to obtain sensitive database information and credentials, ultimately leading to server crashes.

用友时空KSOA是建立在SOA理念指导下研发的新一代产品，是根据流通企业最前沿的I需求推出的统一的IT基础架构，它可以让流通企业各个时期建立的IT系统之间彼此轻松对话，帮助流通企业保护原有的IT投资，简化IT管理，提升竞争能力，确保企业整体的战略目标以及创新活动的实现

用友时空KSOA /servlet/com.sksoft.v8.trans.servlet.TaskRequestServlet接口和/servlet/imagefield接口处存在sql注入漏洞，未经身份认证的攻击者可通过该漏洞获取数据库敏感信息及凭证，最终可能导致服务器失陷。


python3 KSOA_SQL.py -h   --help

python3 KSOA_SQL.py -u url   --single one

python3 KSOA_SQL.py -f urls.txt  --multiple targets

![image](https://github.com/Despacito01/KSOA-SQL-INJECT/blob/main/start.png?raw=true)
![image](https://github.com/Despacito01/KSOA-SQL-INJECT/blob/main/img_1.png?raw=true)
![image](https://github.com/Despacito01/KSOA-SQL-INJECT/blob/main/img.png?raw=true)
