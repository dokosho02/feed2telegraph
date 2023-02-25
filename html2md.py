# import markdownify
import markdownify


# create html
html = """
		<h1> <strong>Geeks</strong>
		for<br>
		Geeks
		</h1>
		"""

html  = """
<p>
【24】<a class="ALink_default_2ibt1" href="https://weibo.com/u/6635013376">@快乐星球宿管阿姨</a> 
</p>
<div class="detail_wbtext_4CRf9">
啊啊啊啊啊啊哈哈哈哈哈哈笑晕
</div>
<p>
<img alt="" src="https://www.dapenti.com:99/dapenti/a63fd778/b905a2c8.jpg" /> 
</p>

"""

# print HTML
print(html)

# convert html to markdown
h = markdownify.markdownify(html, heading_style="ATX")

print(h)
