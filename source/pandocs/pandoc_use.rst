pandoc使用
==========

word转rst
---------

例如一个word的文档为 ``test.docx``, 则该文档转换成rst输入下面該命令即可::

  >> pandoc -s test.docx -o test.rst --extract-media=test_docx_pic


.. attention::
     其中，-s表示源文件；-o表示输出指定格式的目标文件，--extract-media=test_docx_pic 表示word文档的图片输出到指定的文件夹，这里示例为test_docx_pic。


如果文件过长，输出过长时间未有发应，请重式或者把word文档按章节细拆分后再转换。转换完成后，请把转换生成的rst文件拷贝到指定的项目中，按照本文介绍的把该RST文件简单生成html文件的方法生成一个html文件看看效果，根据效果，细调表格，图片，引用，超链接，标题，代码块的效果。
	 



