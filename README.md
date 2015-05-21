# stock_package
Model to store package/tracking numbers. base data model for mage2odoo and omniship
连接器本身依赖 

payment_method

https://github.com/aliomattux/payment_method

stock_package

https://github.com/aliomattux/stock_package

需安装python的magento模块

pip install magento
magento端配置

Openobject_OpenobjectConnector

https://github.com/aliomattux/Openobject_OpenobjectConnector

将Openobject移动到

/var/www/html/magentocn/app/code/community

将Openobject_OpenobjectConnector.xml移动到

/var/www/html/magentocn/app/etc/modules

重启apache

/etc/init.d/httpd restart

注：php需要安装soap extension

总结：odoo8.0本身已经支持部分电商功能，前后台集成良好。magento是更加专业的电商平台，使用mage2odoo连接后端odoo服务作为erp管理平台，也是一种解决方案，但需通过连接器周期的从magento导入订单、客户、库存等信息。

OCA社区提供的连接器目前未移植到8.0版本，需关注后期进展

https://github.com/OCA/connector-magento
