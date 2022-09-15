# 计网第二次软工作业

## 题目

论文查重

## 要求

### PSP

详见 [附录一](#附录一)

### 设计文档

- 结构
  - src/main.py
    - 从命令行参数读取文件路径
    - 读取文件
    - 计算相似度
      - 分词
      - 计算SimHash
    - 关闭文件
    - 输出计算结果
  - test/test.py
    - 使用unittest测试各函数
- 性能分析
- 优化性能
- 完成

### 性能改进

### 单元测试

### 异常处理

## 附录

### 附录一

|PSP2.1|Personal Software Process Stages|预估耗时（分钟）|实际耗时（分钟）|
|:--|:--|:--|:--|
|Planning|计划|-|-|
|· Estimate|· 估计这个任务需要多少时间|420||
|Development|开发|-|-|
|· Analysis|· 需求分析 (包括学习新技术)|120||
|· Design Spec|· 生成设计文档|30|3.6|
|· Design Review|· 设计复审|10||
|· Coding Standard|· 代码规范 (为目前的开发制定合适的规范)|10||
|· Design|· 具体设计|30|2|
|· Coding|· 具体编码|60|49.4|
|· Code Review|· 代码复审|10||
|· Test|· 测试（自我测试，修改代码，提交修改）|120||
|Reporting|报告|-|-|
|· Test Repor|· 测试报告|60||
|· Size Measurement|· 计算工作量|10||
|· Postmortem & Process Improvement Plan|· 事后总结, 并提出过程改进计划|10||
|Total|合计|470||
