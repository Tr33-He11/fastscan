# FastScan 异步网络资产发现引擎
使用python3.5 asyncio 进行网络端口扫描和服务识别以及Web服务的识别．
使用MongoDB存储结果，使用Flask对结果进行展示和搜索。
## 使用方法：
python3 fastscan -s [low,medium,high] ip range 
更多方法: python3 fastscan -h  
启动Web服务：python3 views/view.py　

## 待完成：
1. 高并发时降低漏报，进一步发挥异步威力　
2. 添加搜索引擎爬虫丰富Web资产抓取方式
3. 添加漏洞检测功能 
4. 添加分布式功能
5. 使用elasticsearch进行搜索  
6. 数据可视化
7. ...

### 总的来说，就是要一步步将其搞成一个类似zoomeye的神器，大学毕业前完成，也算是给自己的大学一个交代吧． 

![](https://github.com/BeWhoYouWantToBe/fastscan/master/1.png)
![](https://github.com/BeWhoYouWantToBe/fastscan/master/2.png) 
![](https://github.com/BeWhoYouWantToBe/fastscan/master/3.png) 
![](https://github.com/BeWhoYouWantToBe/fastscan/master/4.png) 
