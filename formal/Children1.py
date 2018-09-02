# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWebEngineWidgets
from qtpy import QtWidgets
from PyQt5.QtWebEngineWidgets import *
"""
ewfefef
"""


class MainWindow2(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle('打开外部网页例子')
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()
        self.browser.setHtml('''
        		<html>
<head>
    <!--meta http-equiv="refresh"content="10"-->
    <meta charset="utf-8">
    <title>思维导图</title>
    <!--//CSS attributtes-->
    <style color=red type="text/css">
        /*节点圆圈*/
        .node circle {
            cursor: pointer;
            fill: #fff;
            stroke: steelblue;
            stroke-width: 2px;
            width:150px;
            border:1px solid #ddd;
            overflow: hidden;
            white-space: nowrap;
            text-overflow: ellipsis;
        }
        .circle:hover {height: auto;white-space: normal;}

        /*节点内容*/
        .node text {
            font-size: 15px;
            fill: #000000;
        }
        .text:hover {height: auto;white-space: normal;}

        /*节点线条*/
        .link {
            fill: none;
            stroke: #ccc;
            stroke-width: 1.5px;
            width:150px;
            border:1px solid #ddd;
            overflow: hidden;
            white-space: nowrap;
            text-overflow: ellipsis;
        }
        .div{
            width: auto;
            height: auto;
            margin: auto;
            align:center;
            background-color: rgba(221, 41, 40, 0.43);

        }
        .photo{
            float: right;
            border: 1px;
            width: 200px;
            height: 200px;
        }
        .photo1{
            float: right;
            border: 1px;
            width: 400px;
            height: 400px;
        }
        #div1{
            width:1300px;
            height:30px;
            background-color: #dddddd;
        }

            .li{
                color: blue;
                float:left;
                width:27%;
                height:30px;
                border-right:1px solid;
        }
        .footer{
            /*float:left;*/
            width:100%;
            height:100%;
            border-right:1px solid;
        }
            .svg{
                float:left;
                width: 65%;
                height: 1500px;
                border: #dddddd 1px solid;
                }
            .imageShow{
                float: right;
                width: 32%;
                height: 100%;
                border: #dddddd 1px solid;
            }
                .imageShowfooter{
                float:right;
                width: 100%;
                height: 50%;
                border: #dddddd 1px solid;
            }
    </style>
</head>
<body >
<div id="image">
    <div id='div1'>
        <div>
            <div id="mess1" class="li">节点信息</div>
        </div>
        <div>
            <div id="mess2" class="li">跳转动作</div>
            <!--<div class="li"> </div>-->
        </div><br>
    </div>
    <div class="footer">
        <div class="svg"></div>
        <div class="imageShow">
            <div id="randimgF" class="imageShowfooter"><img id="randimg" class="photo" ></div>
            <div id="app" class="imageShowfooter">
            </div>
        </div>
    </div>
</div>
<!--<div id="mess" class="div" align="center" style="position: absolute;z-index:90"></div>-->
<!-- 开发环境版本，包含了用帮助的命令行警告 -->
<script src="http://d3js.org/d3.v3.min.js"></script>
# <script src="d3.min.js"></script>
<script>
    var width = 480;//设置高度
    var height = 800;//设置宽度
    var num = 0;//查询节点数
    var depth1 = 180;
    var circleWidth = 7;
    console.log("app=");
    console.log(depth1);

    //边界空白
    var padding = {left: 250, right:50, top: 20, bottom: 20 };

    // svg = 宽 * 高
    var svg = d3.select("body")
        .select(".svg")
        .append("svg")
        // .attr("preserveAspectRatio", "xMidYMid meet")
        // .attr("viewBox", "0 0 400 400")
        .attr("width", 600 + width + padding.left + padding.right)
        .attr("height", 600 + height + padding.top + padding.bottom)
        .append("g")
        .attr("transform","translate("+ padding.left + "," + padding.top + ")");

    //树状图布局
    var tree = d3.layout.tree()
        .size([600 + height + padding.top + padding.bottom, width + padding.left + padding.right]);

    //对角线生成器
    var diagonal = d3.svg.diagonal()
        .projection(function(d) { return [d.y, d.x]; });

    // 加载数据
    d3.json("./neo4j/data1.json",function(error,root){
        //根节点信息
        root.x0 = height / 2;
        root.y0 = 0;

        //以第一个节点为起始节点，重绘
        redraw(root);
        d3.select("#app")
            .append("p")
            .text("层级宽度:");
        d3.select("#app").select("p")//添加输入框表示层级宽度
            .append("input")
            .attr("id","NodeWidth")
            .attr("value",depth1);
        d3.select("#app").select("p")
            .append("button")
            .text("+")
            .on("click",function () {
                depth1 = depth1 + 10;
                document.getElementById("NodeWidth").value = depth1;
                redraw(root);
            });
        d3.select("#app").select("p")
            .append("button")
            .text("-")
            .on("click",function () {
                depth1 = depth1 - 10;
                document.getElementById("NodeWidth").value = depth1;
                redraw(root);
            });

        d3.select("#app")
            .append("p")
            .attr("id","circleWidth")
            .text("节点半径:");
        d3.select("#app").select("#circleWidth")//添加输入框表示节点圆圈半径
            .append("input")
            .attr("id","circleInput")
            .attr("value",circleWidth);
        d3.select("#app").select("#circleWidth")
            .append("button")
            .text("+")
            .on("click",function () {
                if(circleWidth < 18){
                    circleWidth = circleWidth + 2;
                }
                document.getElementById("circleInput").value = circleWidth;
                redraw(root);
            });
        d3.select("#app").select("#circleWidth")
            .append("button")
            .text("-")
            .on("click",function () {
                if(circleWidth > 2){
                    circleWidth = circleWidth - 2;
                }
                document.getElementById("circleInput").value = circleWidth;
                redraw(root);
            });
        //重绘函数
        function redraw(source){

            /*
            （1） 计算节点和连线的位置
            */

            //应用布局，计算节点和连线
            var nodes = tree.nodes(root);
            var links = tree.links(nodes);
            // console.log("节点信息nodes");
            // console.log(nodes);
            //重新计算节点的y坐标   180可以做成交互型数据：表示层级宽度
            nodes.forEach(function(d) {
                d.y = d.depth * depth1;
            });

            /*
            （2） 节点的处理
            */

            //获取节点的update部分  数据绑定
            var nodeUpdate = svg.selectAll(".node")
                .data(nodes, function(d){ return d.name; });

            //获取节点的enter部分
            var nodeEnter = nodeUpdate.enter();

            //获取节点的exit部分
            var nodeExit = nodeUpdate.exit();

            //1. 节点的 Enter 部分的处理办法
            var enterNodes = nodeEnter.append("g")
                .attr("class","node")
                .attr("transform", function(d) { return "translate(" + source.y0 + "," + source.x0 + ")"; })
                .on("click", function(d) { toggle(d); redraw(d); }) //节点的开关按钮点击开关执行重绘函数
                .on("mouseover",function (d) {  //节点鼠标悬浮则，执行显示文字
                    // console.log(d.name);
                    myMess1 = document.getElementById("mess1");
                    myMess1.style.visibility="visible";
                    myMess1.innerHTML = "节点信息：" + d.name;

                    myMess2 = document.getElementById("mess2");
                    myMess2.style.visibility="visible";
                    myMess2.innerHTML = "跳转动作：" + d.skip;

                })
                .on("mouseout",function (d) {  //节点鼠标移开，悬浮结束
                    myMess3 = document.getElementById("mess1");
                    myMess3.style.visibility="visible";
                    myMess3.innerHTML = "节点信息：";

                    myMess4 = document.getElementById("mess2");
                    myMess4.style.visibility="visible";
                    myMess4.innerHTML = "跳转动作：";
                });

            enterNodes.append("circle")
                .attr("r", 10)
                .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; });

            enterNodes.append("text")
                .attr("x", function(d) { return d.children || d._children ? -14 : 14; })
                .attr("dy", ".35em")
                .attr("text-anchor", function(d) { return d.children || d._children ? "end" : "start"; })
                .text(function(d){
                    if(d.name.length >10){
                        return d.name.substring(0,10)+"...";
                    }
                    else{
                        return d.name
                    }
                    })
                .style("fill-opacity", 0);


            //2. 节点的 Update 部分的处理办法
            var updateNodes = nodeUpdate.transition()
                .duration(2000)
                .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; });

            updateNodes.select("circle")
                .attr("r", circleWidth)//设置圆圈半径
                .style("fill", function(d) { return d._children ? "black" : "#fff"; });

            updateNodes.select("text")
                .style("fill-opacity", 1);

            //3. 节点的 Exit 部分的处理办法
            var exitNodes = nodeExit.transition()
                .duration(2000)
                .attr("transform", function(d) { return "translate(" + source.y + "," + source.x + ")"; })
                .remove();

            exitNodes.select("circle")
                .attr("r", 0);

            exitNodes.select("text")
                .style("fill-opacity", 0);

            /*
            （3） 连线的处理
            */

            //获取连线的update部分
            var linkUpdate = svg.selectAll(".link")
                .data(links, function(d){ return d.target.name; });

            //获取连线的enter部分
            var linkEnter = linkUpdate.enter();

            //获取连线的exit部分
            var linkExit = linkUpdate.exit();

            //1. 连线的 Enter 部分的处理办法
            linkEnter.insert("path",".node")
                .attr("class", "link")
                .attr("d", function(d) {
                    var o = {x: source.x0, y: source.y0};
                    return diagonal({source: o, target: o});
                })
                .transition()
                .duration(2000)
                .attr("d", diagonal);


            //2. 连线的 Update 部分的处理办法
            linkUpdate.transition()
                .duration(2000)
                .attr("d", diagonal);

            //3. 连线的 Exit 部分的处理办法
            linkExit.transition()
                .duration(2000)
                .attr("d", function(d) {
                    var o = {x: source.x, y: source.y};
                    return diagonal({source: o, target: o});
                })
                .remove();


            /*
            （4） 将当前的节点坐标保存在变量x0、y0里，以备更新时使用
            */

            nodes.forEach(function(d) {
                num = num + 1;
                d.x0 = d.x;
                d.y0 = d.y;
            });

        }

        //切换开关，d 为被点击的节点
        function toggle(d){
            if(d.children){ //如果有子节点
                d._children = d.children; //将该子节点保存到 _children
                d.children = null;  //将子节点设置为null
            }else{  //如果没有子节点
                d.children = d._children; //从 _children 取回原来的子节点
                d._children = null; //将 _children 设置为 null
            }
            document.getElementsByTagName("img").src=d.proof;
            var imgSrc = document.getElementsByTagName("img").src;
            var img = d3.select("body").select(".footer").select(".imageShow").select("img");
            var para = d3.select("body").select(".footer").select(".imageShow").select("#randimgF");
            img.remove();
            para.append("img")
                .attr("class","photo")
                .attr("src",imgSrc)
                .on("mouseover",function () {  //节点鼠标悬浮则，执行图片放大
                    var img1 = d3.select("body").select("img");
                    img1.style({'align':'center','border': '1px', 'width': "100%","height":"100%"});
                })
                .on("mouseout",function () {  //节点鼠标移开，图片恢复
                    var img2 = d3.select("body").select("img");
                    img2.style({'align':'center','border': '1px', 'width': "200px","height":"200px"});
                });
            console.log("img");
            console.log(imgSrc);
        }
    });
</script>
</body>
</html>
        		'''
                             )

        self.setCentralWidget(self.browser)
        # 加载外部页面
        # self.browser.load(QUrl('./json_html/mindV.html'))
        # self.setCentralWidget(self.browser)
        # url = f'./json_html/mindV.html'
        # url = f'./json_html/test.html'
        # self.browser.load(QUrl(url))
        # self.setCentralWidget(self.browser)
