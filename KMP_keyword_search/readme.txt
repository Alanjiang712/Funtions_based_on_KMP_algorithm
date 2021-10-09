从 keyword_search 文件中导入 keyword_search 函数即可使用。
如果使用中文文本则需要在调用本函数的文件头部添加一行 # encoding: utf-8

keyword_search函数需要两个参数，第一个是需要被检索的字段（str），第二个是关键字词典的代号（str）。
默认的关键字词典是 symptomDict 文件与 evaluateDcit 文件，分别对应SYMPTOM和EVALUATE字符串（注意区分大小写）。
函数的输出（返回值）[0]是一个包括了关键字本身、它在文中出现位置和它键值的列表。
函数的输出（返回值）[1]则是包括了所有关键字的列表，如果某关键字出现多次仍只在此列表中出现一次。
